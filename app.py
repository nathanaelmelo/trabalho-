from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
pedidos_usuarios = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensagem', methods=['POST'])
def mensagem():
    dados = request.get_json()
    usuario = dados.get('usuario', 'cliente')
    mensagem = dados.get('mensagem', '').strip().lower()

    if usuario not in pedidos_usuarios:
        pedidos_usuarios[usuario] = []

    if mensagem == "meus pedidos":
        if pedidos_usuarios[usuario]:
            resposta = "Seus pedidos:\n" + "\n".join(f"- {p}" for p in pedidos_usuarios[usuario])
        else:
            resposta = "Você ainda não fez nenhum pedido."
    elif mensagem.startswith("quero") or mensagem.startswith("pedido"):
        pedido = mensagem.replace("quero", "").replace("pedido", "").strip()
        if pedido:
            pedidos_usuarios[usuario].append(pedido)
            resposta = f"Pedido registrado: {pedido}"
        else:
            resposta = "Desculpe, não entendi o que você quer pedir."
    else:
        resposta = "Olá! Você pode digitar algo como:\n- 'Quero 1 pizza'\n- 'Meus pedidos'"

    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)
