// Flag para exibir opções apenas uma vez
let comandosExibidos = false;

// Função para obter o timestamp atual
function obterTimestamp() {
  const agora = new Date();
  const horas = String(agora.getHours()).padStart(2, '0');
  const minutos = String(agora.getMinutes()).padStart(2, '0');
  return `${horas}:${minutos}`;
}

// Função para mostrar indicador de digitação
function mostrarIndicadorDeDigitacao() {
  const div = document.createElement("div");
  div.className = "msg bot";
  div.textContent = "FURIA está digitando...";
  document.getElementById("chat").appendChild(div);
  document.getElementById("chat").scrollTop = document.getElementById("chat").scrollHeight;
}

// Adiciona uma mensagem no chat com timestamp
function adicionarMensagem(classe, texto) {
  const div = document.createElement("div");
  div.className = "msg " + classe;

  const img = document.createElement("img");
  img.src = classe === "user" ? "/static/img/user.png" : "/static/img/furia.png";

  const msgTexto = document.createElement("span");
  msgTexto.textContent = texto;

  const timestamp = document.createElement("span");
  timestamp.className = "timestamp";
  timestamp.textContent = obterTimestamp();

  div.appendChild(img);
  div.appendChild(msgTexto);
  div.appendChild(timestamp);
  
  document.getElementById("chat").appendChild(div);
  document.getElementById("chat").scrollTop = document.getElementById("chat").scrollHeight;
}

// Envia a mensagem para o servidor
async function enviar() {
  const input = document.getElementById("mensagem");
  const texto = input.value.trim();
  if (texto === "") return;

  adicionarMensagem("user", "Você: " + texto);
  input.value = "";

  // Adiciona a mensagem "FURIA está digitando..."
  const digitandoDiv = document.createElement("div");
  digitandoDiv.className = "msg bot digitando fade-in";

  const img = document.createElement("img");
  img.src = "/static/img/furia.png";

  const typingText = document.createElement("span");
  typingText.textContent = "FURIA está digitando...";

  digitandoDiv.appendChild(img);
  digitandoDiv.appendChild(typingText);

  const chat = document.getElementById("chat");
  chat.appendChild(digitandoDiv);
  chat.scrollTop = chat.scrollHeight;

  // Espera 900 milissegundos (0,9s) ANTES de buscar a resposta
  await new Promise(resolve => setTimeout(resolve, 900));

  // Agora busca a resposta do servidor
  const resposta = await fetch("/mensagem", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mensagem: texto })
  }).then(r => r.json());

  // Remove "digitando..."
  digitandoDiv.remove();

  // Adiciona a resposta da FURIA
  adicionarMensagem("bot", "FURIA: " + resposta.resposta);
}

// Perguntas rápidas
const comandos = [
  "Quem somos?",
  "Quem é o time?",
  "Quais modalidades estamos?",
  "Onde posso assistir os jogos?",
  "Como posso apoiar a FURIA?"
];

// Exibe cada comando como um botão dentro do chat (com animação e delay)
function mostrarOpcoesComoBotoes() {
  const chat = document.getElementById("chat");
  comandos.forEach((comando, i) => {
    setTimeout(() => {
      const div = document.createElement("div");
      div.className = "msg bot";

      const img = document.createElement("img");
      img.src = "/static/img/furia.png";
      div.appendChild(img);

      const btn = document.createElement("button");
      btn.className = "comando-btn fade-in";
      btn.textContent = comando;
      btn.onclick = () => handleComandoClick(comando, btn);

      div.appendChild(btn);
      chat.appendChild(div);
      chat.scrollTop = chat.scrollHeight;
    }, i * 150);
  });
}

// Quando o usuário clica em um comando
async function handleComandoClick(comando, btn) {
  // Remove todo o container da mensagem (ícone + botão)
  const msgDiv = btn.closest('.msg.bot');
  msgDiv.remove();

  // Adiciona mensagem do usuário
  adicionarMensagem("user", "Você: " + comando);

  // Adiciona a mensagem "FURIA está digitando..."
  const digitandoDiv = document.createElement("div");
  digitandoDiv.className = "msg bot digitando fade-in";

  const img = document.createElement("img");
  img.src = "/static/img/furia.png";

  const typingText = document.createElement("span");
  typingText.textContent = "FURIA está digitando...";

  digitandoDiv.appendChild(img);
  digitandoDiv.appendChild(typingText);

  const chat = document.getElementById("chat");
  chat.appendChild(digitandoDiv);
  chat.scrollTop = chat.scrollHeight;

  // Espera 900 milissegundos (0,9s) ANTES de buscar a resposta
  await new Promise(resolve => setTimeout(resolve, 900));

  // Busca a resposta
  const resp = await fetch("/mensagem", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mensagem: comando })
  }).then(r => r.json());

  // Remove "digitando..."
  digitandoDiv.remove();

  // Adiciona a resposta da FURIA
  adicionarMensagem("bot", "FURIA: " + resp.resposta);
}

// Abre e fecha o chat
function toggleChat() {
  const chatContainer = document.getElementById("chat-container");
  const visivel = chatContainer.style.display === "block";

  if (visivel) {
    chatContainer.style.display = "none";
  } else {
    chatContainer.style.display = "block";
    if (!comandosExibidos) {
      mostrarOpcoesComoBotoes();
      comandosExibidos = true;
    }
  }
}

// Evento ao carregar a página
window.onload = function() {
  // Certifique-se de que o botão está presente no DOM antes de adicionar o evento
  var botaoEnviar = document.getElementById("send-button");

  if (botaoEnviar) {
    botaoEnviar.onclick = enviar;  // Adiciona o evento de clique
  } else {
    console.error("Botão de enviar não encontrado!");
  }
};
