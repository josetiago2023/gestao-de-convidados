from flask import Flask, render_template, request

app = Flask(__name__)

# Lista de convidados
lista_convidados = ["Ana", "Bruno", "Carlos", "Débora", "Eduarda"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/verificar", methods=["POST"])
def verificar():
    nome = request.form.get("nome")
    if nome in lista_convidados:
        mensagem = f"{nome} está na lista de convidados!"
    else:
        mensagem = f"{nome} NÃO está na lista de convidados."
    return render_template("resultado.html", mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)
