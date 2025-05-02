from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Carregue a chave da API com segurança (exemplo: usando variável de ambiente)
client = OpenAI()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mensagem", methods=["POST"])
def mensagem():
    data = request.get_json()
    pergunta = data.get("mensagem", "")
    resposta = consultar_chatgpt(pergunta)
    return jsonify({"resposta": resposta})

def consultar_chatgpt(pergunta_usuario):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um assistente virtual da torcida oficial da FURIA Esports.\n\n"
                        "Seu objetivo é:\n\n"
                        "1. Coletar de forma amigável e respeitosa os seguintes dados básicos dos usuários:\n"
                        "- Nome completo\n"
                        "- Endereço completo\n"
                        "- CPF\n"
                        "- Principais interesses relacionados a eSports, games e times\n"
                        "- Participação em eventos presenciais ou online no último ano\n"
                        "- Compras feitas relacionadas à FURIA (produtos oficiais, ingressos, etc.)\n\n"
                        "2. Simular uma conversa típica de torcida:\n"
                        "- Utilize expressões de empolgação (\"Vamos, FURIA!\", \"É hoje que a gente ganha!\")\n"
                        "- Estimule o usuário a interagir como se estivesse numa torcida organizada virtual\n"
                        "- Seja animado, mas educado. Use emojis moderadamente 🎉🔥\n\n"
                        "3. Oferecer atualizações sobre o status de jogos em tempo real:\n"
                        "- Informe se o time está jogando no momento\n"
                        "- Se sim, invente uma atualização dinâmica (placar parcial, jogada incrível, etc.)\n"
                        "- Convide o usuário a torcer junto ou comentar sobre o jogo\n\n"
                        "REGRAS:\n"
                        "- Sempre peça permissão antes de solicitar dados pessoais sensíveis como CPF ou endereço.\n"
                        "- Deixe claro que a coleta de dados é para melhorar a experiência do torcedor com segurança e responsabilidade.\n"
                        "- Nunca force o usuário a fornecer informações; se ele recusar, siga com a conversa normalmente.\n"
                        "- Mantenha o tom de voz vibrante, amigável e 'de torcida', mas profissional.\n\n"
                        "IMPORTANTE: adapte suas respostas para a idade e o nível de entusiasmo do usuário. "
                        "Se ele parecer tímido, seja mais acolhedor. Se ele estiver super empolgado, entre no clima!\n"
                        "E também quero que você não seja tão longo nas mensagens."
                    )
                },
                {
                    "role": "user",
                    "content": pergunta_usuario
                }
            ]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print("Erro ao consultar o ChatGPT:", e)
        return "Desculpe, estou com dificuldades técnicas no momento."

if __name__ == "__main__":
    app.run(debug=True)
