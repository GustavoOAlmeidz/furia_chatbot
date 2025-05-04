# 🤖 FURIA Chatbot

Chatbot interativo desenvolvido para fãs do time de CS2 da FURIA, com visual personalizado e preparado para integração com funcionalidades futuras como coleta de dados de fãs.

---

## 📌 Sumário

- [🎯 Objetivo](#-objetivo)
- [⚙️ Funcionalidades](#️-funcionalidades)
- [🖥️ Instalação e Execução](#️-instalação-e-execução)
- [🛠 Estrutura do Projeto](#-estrutura-do-projeto)
- [✅ Requisitos](#-requisitos)
- [💡 Próximos passos](#-proximos-passos)
- [🤝 Contribuindo](#-contribuindo)
- [📄 Licença](#-licença)

---

## 🎯 Objetivo

O objetivo principal do projeto é **engajar a comunidade de fãs da FURIA** por meio de uma experiência conversacional amigável e visualmente atrativa. A solução faz parte de um desafio prático de design e desenvolvimento de protótipos funcionais com foco em interatividade, visual e usabilidade.

---

## ⚙️ Funcionalidades

- Interface com identidade visual da FURIA
- Avatares do usuário e do bot
- Layout responsivo para dispositivos móvei
- Preparado para integração com coleta de dados via chat
- Estrutura preparada para evolução (ex: IA, integração com APIs)

---

## 🖥️ Instalação e Execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/GustavoOAlmeidz/furia_chatbot.git
   cd furia_chatbot
   ```

2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o app:
   ```bash
   python app.py
   ```

Acesse no navegador: [http://localhost:5000](http://localhost:5000)

---

## ✅ Requisitos

- Python 3.8 ou superior
- Flask

---

## 🛠 Estrutura do Projeto

```
furia_chatbot/
├── app.py              # Arquivo principal do Flask
├── requirements.txt    # Dependências do projeto
├── Procfile            # Configuração para deploy no Heroku
├── .gitignore
├── README.md
├── static
|  ├─img
|  | ├─ user.png
|  | └─ furia.png
|  ├─ script.js
|  └─ styke.css
├── templates
|  └─ index.html
└──venv
```

---

## 💡 Próximos passos

- Integração com coleta de dados de fãs (Know Your Fan)
- Upload de documentos com IA
- Validação de perfis de eSports

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para começar:

1. Fork o repositório
2. Crie uma branch (`git checkout -b feature/minha-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/minha-feature`)
5. Crie um Pull Request

---

## 📄 Licença

Este projeto está aberto use-o como quiser
