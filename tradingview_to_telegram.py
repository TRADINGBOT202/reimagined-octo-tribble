from flask import Flask, request
import requests

app = Flask(__name__)

# Token y chat ID personalizados
TELEGRAM_TOKEN = '7887485585:AAHxtAUSoCsDbP7FQ90KuQlt5Y4UsPmlZlk'
CHAT_ID = '74316106'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    alert_message = data.get('message', 'Alerta sin mensaje')
    send_telegram_message(f"Alerta de TradingView: {alert_message}")
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000
