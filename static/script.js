const chat = document.getElementById('chat');
const usuario = "cliente"; // Simples ID de usuário

function adicionarMensagem(texto, classe) {
    const p = document.createElement('p');
    p.className = `mensagem ${classe}`;
    p.innerText = texto;
    chat.appendChild(p);
    chat.scrollTop = chat.scrollHeight;
}

function enviarMensagem() {
    const input = document.getElementById('mensagem');
    const texto = input.value.trim();
    if (!texto) return;

    adicionarMensagem(`Você: ${texto}`, 'cliente');
    input.value = '';

    fetch('/mensagem', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ usuario, mensagem: texto })
    })
    .then(response => response.json())
    .then(data => adicionarMensagem(`Bot: ${data.resposta}`, 'bot'));
}
