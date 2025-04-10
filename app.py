import streamlit as st
from dotenv import load_dotenv
from modulos.busqueda import buscar_informacion
from modulos.procesamiento import generar_resumen
from modulos.visualizacion import crear_wordcloud

load_dotenv()

st.set_page_config(page_title="Asistente de Investigación", layout="wide")
st.title("Asistente de Investigación Digital")

#Entrada del usuario
tema = st.text_input("Ingresa un tema de investigación:")

if tema:
    with st.spinner("Buscando información..."):
        resultados = buscar_informacion(tema)

    if resultados:
        #Mostrar resultados de búsqueda
        st.subheader("Resultados encontrados")
        for resultado in resultados[:3]:  #Muestra los primeros 3 resultados
            with st.expander(resultado["title"]):
                st.markdown(f"**Contenido:** {resultado['content'][:500]}...")
                st.markdown(f"**Enlace:** [{resultado['url']}]({resultado['url']})")

        #Generar resumen
        st.subheader("Resumen ejecutivo")
        resumen = generar_resumen(resultados)
        st.info(resumen)

        #Generar nube de palabras
        st.subheader("Nube de palabras clave")
        wordcloud = crear_wordcloud(resultados)
        st.image(wordcloud, use_container_width=True)
    else:
        st.warning("No se encontraron resultados para este tema.")