# Comparador de Poblacion de Alianza Travian Legends

## Descripción

Este proyecto es una aplicación web para comparar datos de jugadores en un formato de archivo HTML. Utiliza Flask como framework web y SQLite como base de datos para gestionar y almacenar los datos de los jugadores. La aplicación permite cargar archivos, comparar datos actuales con datos previos, y visualizar las diferencias con la fecha de la última actualización. También incluye una funcionalidad de modo oscuro para una mejor experiencia de usuario.

## Funcionalidades

- **Carga de Datos:** Permite subir archivos HTML con datos de jugadores, incluyendo poblaciones y aldeas.
- **Comparación de Datos:** Compara los datos actuales con los datos previos almacenados en la base de datos.
- **Visualización de Diferencias:** Muestra las diferencias en poblaciones y aldeas entre los datos actuales y previos.
- **Modo Oscuro:** Alterna entre el modo oscuro y el modo claro para la interfaz de usuario.
- ~~Fecha de Última Actualización~~: Muestra la fecha y hora de la última actualización de los datos.
- **Persistencia de Datos:** Los datos previos se mantienen en la base de datos para futuras comparaciones.

## Instalación y Ejecución

Para ejecutar esta aplicación localmente, sigue estos pasos:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git

2. **Navega al directorio del proyecto:**

   ```bash
   cd flask-travian-compare-population-ally

3. **Instala Flask:**

   ```bash
   pip install Flask

4. **Ejecuta la aplicación**

   ```bash
   python app.py

5. **Accede a la aplicación en tu navegador:**

   ```bash
   Abre http://127.0.0.1:5000 en tu navegador

## Como Usarlo

1. **Carga de Datos:**
   - Navega a la página principal.
   - Usa el formulario para subir un archivo HTML que contenga los datos de los jugadores.
   - Los datos se procesarán y actualizarán en la base de datos.

2. **Visualización de Resultados:**
   - Después de cargar los datos, se te redirigirá a la página de resultados.
   - Aquí podrás ver los datos actuales y las diferencias comparadas con los datos anteriores.

3. **Modo Oscuro:**
   - Usa el botón de alternancia en la esquina superior derecha para cambiar entre el modo claro y el modo oscuro.

## Tecnologías

- **Flask:** Framework web en Python.
- **SQLite:** Base de datos ligera para almacenamiento local.
- **Bootstrap:** Framework CSS para estilos.
- **BeautifulSoup:** Biblioteca para extraer datos de archivos HTML.

## Contribuciones al Codigo / Proyecto

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tus cambios.
3. Realiza tus modificaciones.
4. Envía un pull request con una descripción clara de tus cambios.

## Contribuciones y Apoyo

Si encuentras útil este proyecto y deseas apoyarlo, puedes hacerlo de varias maneras:

- **Donaciones:** Si te gustaría apoyar el desarrollo continuo y la mejora de este proyecto, puedes hacer una donación en [Buy Me a Coffee](https://buymeacoffee.com/felipecastillo). Tu contribución ayudará a cubrir los costos de desarrollo y mantener el proyecto actualizado.
- **Comparte el Proyecto:** Ayuda a difundir el proyecto compartiéndolo con otros. Cuantos más usuarios lo conozcan, más útil será para la comunidad.
- **Feedback:** Si tienes comentarios o sugerencias, no dudes en contactarme. Siempre estoy buscando maneras de mejorar el proyecto.

Cada aporte es muy apreciado y contribuye directamente a la calidad y sostenibilidad del proyecto. ¡Gracias por tu apoyo!

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles
