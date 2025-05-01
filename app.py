from flask import Flask, request, jsonify
import time
import random
from bot.ai_bot import AiBot

app = Flask(__name__)

from services.waha import Waha

@app.route('/chatbot/webhook/', methods=['POST'])
def webhook():
    data = request.json
    print(f'EVENTO RECEBIDO {data}')
    waha = Waha()
    ai_bot = AiBot()

    event = data.get('event', {})

    if event and event != 'session.status':

        chat_id = data['payload']['from']
        received_message = data['payload']['body'];
        waha.start_typing(chat_id)
        time.sleep(3)

        response = ai_bot.invoke(question=received_message)
        waha.send_message(
            chat_id=chat_id,
            message=response
        )

        waha.stop_typing(chat_id)



    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)