from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot de Trading corriendo"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Señal recibida:", data)

    if data.get('signal') == 'buy':
        print("Ejecutar orden de COMPRA simulada")
    elif data.get('signal') == 'sell':
        print("Ejecutar orden de VENTA simulada")
    else:
        print("Señal desconocida")

    return jsonify({'status': 'señal recibida'}), 200

if __name__ == '__main__':
    app.run()
