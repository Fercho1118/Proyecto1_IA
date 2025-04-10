from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os


def generar_resumen(resultados):
    contenido = "\n".join([res["content"][:1000] for res in resultados])

    prompt_template = ChatPromptTemplate.from_template(
        "Genera un resumen ejecutivo en español de máximo 200 palabras "
        "basado en esta información:\n\n{texto}\n\nResumen:"
    )

    llm = ChatOpenAI(
        temperature=0.2,
        model="gpt-4o-mini",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    cadena = prompt_template | llm
    return cadena.invoke({"texto": contenido}).content