from flask import Flask, request, jsonify
from registro_trader import RegistroTrader

app = Flask(__name__)
registro = RegistroTrader()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Alerta recibida:", data)

    # Extraer datos desde TradingView
    par = data.get('par', 'BTC/USDT')
    tipo = data.get('tipo', 'compra')
    entrada = float(data.get('precio_entrada', 0))
    salida = float(data.get('precio_salida', 0))

    # Registrar la operación
    registro.registrar_operacion(par, tipo, entrada, salida)
    return jsonify({"status": "registrado"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
