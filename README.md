<div align="center">
  <h1>Asistente de Investigación Digital</h1> 
</div>


## Descripción
Este proyecto es una aplicación web interactiva desarrollada con Streamlit que funciona como un asistente de investigación digital. Permite a los usuarios ingresar un tema de interés, realizar una búsqueda de información en tiempo real utilizando la API de Tavily, generar un resumen automático del contenido con OpenAI y visualizar las palabras más frecuentes en una nube de palabras.

---

## Funcionalidades

- **Búsqueda de información:** El usuario puede ingresar un tema de investigación, y la aplicación buscará información relevante en la web utilizando la API de Tavily.
- **Generación de resúmenes:** La aplicación genera un resumen ejecutivo del contenido encontrado utilizando el modelo **GPT-4 mini** de OpenAI.
- **Visualización de palabras clave:** Se genera una nube de palabras (WordCloud) a partir del contenido relevante encontrado.
- **Interfaz interactiva:** La interfaz es desarrollada en **Streamlit**, lo que permite a los usuarios interactuar fácilmente con la aplicación.

---

## Instrucciones para ejecutar

### Requisitos
Para ejecutar este proyecto, necesitarás tener instaladas las siguientes dependencias:
- Python 3.x
- pip para la instalación de dependencias

### Instalación

### 1. Crea un entorno virtual:

   ```
   python -m venv myenv
   ```
   ```
   source venv/bin/activate # En Linux/macOS
   .\myenv\Scripts\Activate.ps1 # En Windows
   ```

### 2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

### 3. Configura las claves de API:
   ```
   TAVILY_API_KEY=tu_clave_de_api_tavily
   OPENAI_API_KEY=tu_clave_de_api_openai
   ```

### 4. Ejecutar la aplicación:
   ```
   streamlit run app.py
   ```
* Abre tu navegador y ve a http://localhost:8501 para interactuar con la aplicación.
---

## Estructura del proyecto
El proyecto está dividido en los siguientes módulos:

### 1. app.py:
- Este archivo contiene la interfaz principal de la aplicación, donde se maneja la entrada del usuario, se realiza la búsqueda de información, y se muestran los resultados y la nube de palabras.

### 2. modulos/busqueda.py:
- En este módulo se encuentra la función buscar_informacion(), que usa la API de Tavily para realizar la búsqueda de información basada en el tema ingresado por el usuario.

### 3. modulos/procesamiento.py:
- Este módulo contiene la función generar_resumen(), que utiliza OpenAI para generar un resumen ejecutivo del contenido encontrado.

### 4. modulos/visualizacion.py:
- En este archivo se encuentra la función crear_wordcloud(), que genera una nube de palabras a partir del contenido encontrado, usando la librería WordCloud y matplotlib para la visualización.

---

## Reflexión sobre el uso de IA para la búsqueda y procesamiento de información
El uso de inteligencia artificial (IA) en la búsqueda y procesamiento de información tiene el potencial de transformar la forma en que interactuamos con grandes volúmenes de datos. En este proyecto, la IA se utiliza para realizar búsquedas relevantes, generar resúmenes automáticos y visualizar patrones de palabras clave. Aunque este enfoque tiene muchas ventajas, como la velocidad y la capacidad de manejar grandes cantidades de datos, también plantea varios desafíos éticos y prácticos:

- **Sesgo en los modelos de IA:** Los modelos de lenguaje, como los utilizados en este proyecto (GPT-4), pueden estar sesgados por los datos con los que fueron entrenados. Esto puede llevar a la generación de resúmenes que omiten o malinterpretan ciertos aspectos de la información.
- **Dependencia de fuentes externas:** El sistema depende de las APIs de Tavily y OpenAI para obtener y procesar la información. Esto significa que la calidad de los resultados dependerá de las fuentes de datos externas y de la fiabilidad de los servicios utilizados.
- **Privacidad y seguridad:** Al procesar datos en línea, siempre existe el riesgo de que la información sensible pueda ser expuesta. Es fundamental implementar medidas de seguridad y privacidad para proteger los datos de los usuarios.

  En general, este proyecto demuestra cómo la IA puede ser utilizada de manera efectiva para apoyar la investigación digital, pero también subraya la importancia de abordar los problemas éticos y prácticos asociados   con el uso de estas tecnologías.
---

## Contacto
* Estudiantes:
  - Fernando Hernández - her23645@uvg.edu.gt
  - Fernando Rueda - rue23748@uvg.edu.gt
