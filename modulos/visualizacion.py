from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io


def crear_wordcloud(resultados):
    texto = " ".join([res["content"] for res in resultados])

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        stopwords=["el", "la", "los", "de", "en"]
    ).generate(texto)

    #Convertir a imagen para Streamlit
    img = io.BytesIO()
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(img, format="png")
    img.seek(0)

    return img