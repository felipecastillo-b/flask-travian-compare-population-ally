import sqlite3
from flask import Flask, request, render_template, redirect, url_for, flash
from bs4 import BeautifulSoup

# Inicializar la aplicación Flask
app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necesario para mensajes flash

# Configuración de la base de datos
DATABASE = 'data.db'

# Funcion para obtener la conexion a la base de datos
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Crear tabla si no existe
def create_tables():
    conn = get_db_connection()
    
    # Tabla para datos actuales
    conn.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player TEXT UNIQUE NOT NULL,
            population INTEGER NOT NULL,
            villages INTEGER NOT NULL
        )
    ''')

    # Tabla para datos previos
    conn.execute('''
        CREATE TABLE IF NOT EXISTS previous_players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player TEXT UNIQUE NOT NULL,
            population INTEGER NOT NULL,
            villages INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Crear tablas al iniciar la aplicacion
create_tables()

# Funcion para filtrar datos usando BeautifulSoup
def filtrar_datos(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    players = []
    populations = []
    villages = []

    # Extraer jugadores, poblaciones y aldeas
    for td in soup.find_all('td', class_='player'):
        players.append(td.get_text(strip=True))
    for td in soup.find_all('td', class_='population'):
        populations.append(int(td.get_text(strip=True).replace(',', '')))
    for td in soup.find_all('td', class_='villages'):
        villages.append(int(td.get_text(strip=True).replace(',', '')))

    # Comprobar que las listas tengan la misma longitud
    if len(players) == len(populations) == len(villages):
        # Emparejar datos y ordenar alfabeticamente
        results = [(players[i], populations[i], villages[i]) for i in range(len(players))]
        results_sorted = sorted(results, key=lambda x: x[0].lower())
        return results_sorted
    else:
        return []

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Leer el archivo subido
        archivo = request.files['archivo']
        if not archivo:
            flash('No se ha seleccionado ningún archivo.', 'danger')
            return redirect(url_for('index'))

        # Leer el contenido del archivo
        html_content = archivo.read().decode('utf-8')

        # Filtrar datos usando BeautifulSoup
        datos_filtrados = filtrar_datos(html_content)

        if not datos_filtrados:
            flash('Error: El formato del archivo es incorrecto o las listas no coinciden.', 'danger')
            return redirect(url_for('index'))

        # Conectar a la base de datos
        conn = get_db_connection()

        # Mover datos actuales a la tabla de datos previos
        conn.execute('''
            INSERT OR REPLACE INTO previous_players (player, population, villages)
            SELECT player, population, villages FROM players
        ''')

        # Limpiar datos actuales
        conn.execute('DELETE FROM players')

        # Insertar o actualizar datos filtrados en la base de datos actual
        for player, population, villages in datos_filtrados:
            conn.execute('''
                INSERT INTO players (player, population, villages)
                VALUES (?, ?, ?)
                ON CONFLICT(player) DO UPDATE SET
                    population = excluded.population,
                    villages = excluded.villages
            ''', (player, population, villages))

        conn.commit()
        conn.close()

        flash('Archivo procesado exitosamente y base de datos actualizada.', 'success')
        return redirect(url_for('resultado'))

    return render_template('index.html')

# Ruta para ver los resultados y comparaciones
@app.route('/resultado')
def resultado():
    conn = get_db_connection()

    # Obtener datos actuales
    jugadores_actuales = conn.execute('SELECT * FROM players ORDER BY player ASC').fetchall()

    # Obtener datos previos
    jugadores_previos = conn.execute('SELECT * FROM previous_players ORDER BY player ASC').fetchall()

    # Diccionarios para comparación
    dict_actuales = {jugador['player']: (jugador['population'], jugador['villages']) for jugador in jugadores_actuales}
    dict_previos = {jugador['player']: (jugador['population'], jugador['villages']) for jugador in jugadores_previos}

    # Determinar diferencias
    diferencias = []

    # Comparar datos para jugadores actuales con datos previos
    for player in dict_actuales:
        pop_actual, vil_actual = dict_actuales[player]

        if player in dict_previos:
            pop_prev, vil_prev = dict_previos[player]

            # Comparar poblaciones y aldeas
            dif_poblacion = pop_actual - pop_prev
            dif_villages = vil_actual - vil_prev

            # Almacenar las diferencias
            diferencias.append({
                'player': player,
                'pop_actual': pop_actual,
                'vil_actual': vil_actual,
                'pop_prev': pop_prev,
                'vil_prev': vil_prev,
                'dif_poblacion': dif_poblacion,
                'dif_villages': dif_villages
            })
        else:
            # Si el jugador no está en datos previos, mostrar como 'Sin Datos Previos'
            diferencias.append({
                'player': player,
                'pop_actual': pop_actual,
                'vil_actual': vil_actual,
                'pop_prev': 'Sin Datos Previos',
                'vil_prev': 'Sin Datos Previos',
                'dif_poblacion': 'N/A',
                'dif_villages': 'N/A'
            })

    conn.close()

    return render_template('resultado.html', jugadores=jugadores_actuales, diferencias=diferencias)

# Ejecución del servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
