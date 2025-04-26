from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dicionário para mapear perguntas a respostas
respostas = {
    "Quem somos?": "Somos um time de eSports muito famoso no Brasil e no mundo!",
    "Quem é o time?": "O time da FURIA é composto por jogadores de CS:GO, League of Legends, e muito mais!",
    "Quais modalidades estamos?": "Atualmente, estamos em CS:GO, League of Legends, Rainbow Six, e VALORANT!",
    "Onde posso assistir os jogos?": "Você pode assistir nossos jogos ao vivo na Twitch (FURIA TV) e no YouTube (Kings League Brasil).",
    "Como posso apoiar a FURIA?": "Você pode apoiar assistindo e compartilhando as transmissões, participando de nossos eventos e comprando produtos na loja oficial."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mensagem", methods=["POST"])
def mensagem():
    data = request.get_json()
    pergunta = data.get("mensagem", "")

    # Busca a resposta no dicionário, se não encontrar, fornece uma resposta padrão
    resposta = respostas.get(pergunta, "Desculpe, não entendi sua pergunta, estou aprendendo.")

    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
