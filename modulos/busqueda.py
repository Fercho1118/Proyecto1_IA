from langchain_community.tools.tavily_search import TavilySearchResults
import os


def buscar_informacion(tema: str):
    tavily_key = os.getenv("TAVILY_API_KEY")

    #Configurar herramienta de búsqueda directa sin agente
    search = TavilySearchResults(tavily_api_key=tavily_key, max_results=5)

    #Ejecutar búsqueda directamente
    resultados_raw = search.invoke({"query": tema})

    #Formatear resultados
    return [{
        "title": res["title"],
        "content": res["content"],
        "url": res["url"]
    } for res in resultados_raw]