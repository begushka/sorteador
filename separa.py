import random
from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "chave-secreta"

@app.route("/")
def inicio():
    session.clear()
    session["tentativas"] = 0
    return render_template(
        "index.html",
        resultados=None,
        tentativas=0
    )


@app.route("/sortear", methods=["POST"])
def sortear():
    tentativas = session.get("tentativas", 0)
    if tentativas >= 3:
        return render_template(
            "index.html",
            resultados=session.get("resultados"),
            tentativas=tentativas,
            erro="Impossível girar de novo!"
        )
    pessoas = ["Moisés", "Pablo", "Miguel"]
    topicos = ["Conceito", "Classificação", "Radiciação"]
    random.shuffle(topicos)
    resultados = []
    for pessoa, topico in zip(pessoas, topicos):
        resultados.append({
            "pessoa": pessoa,
            "topico": topico
        })
    tentativas += 1
    session["tentativas"] = tentativas
    session["resultados"] = resultados
    return render_template(
        "index.html",
        resultados=resultados,
        tentativas=tentativas
    )


if __name__ == "__main__":
    app.run(debug=True)



"""
import random
from colorama import init, Fore

init(autoreset=True)

pessoas = ["Moisés", "Pablo", "Miguel"]
topicos = ["Conceito", "Classificação", "Radiciação"]
random.shuffle(topicos)

for pessoa, topico in zip(pessoas, topicos):
    print(f"\n{pessoa} ficou com: {topico}")
"""