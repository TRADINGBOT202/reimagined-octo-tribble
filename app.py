from flask import Flask, request, jsonify
from registro_trader import RegistroTrader
registro = RegistroTrader()
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
        registro.registrar_operacion('BTC/USDT', 'compra', 28000.0, 28500.0)
    else:
        print("Señal desconocida")

    return jsonify({'status': 'señal recibida'}), 200

if __name__ == '__main__':
    app.run()
    Agregué el import del registro de operaciones
