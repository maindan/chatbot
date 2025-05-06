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
    
    chat_id = data['payload']['from']
    event = data['event']
    received_message = data['payload']['body'];

    is_group = '@g.us' in chat_id
    is_status = 'status@broadcast' in chat_id
    is_event = 'session.status' in event

    is_ai_content = 'chatbot_ai' in received_message

    if is_group or is_status or is_event:
        return jsonify({'status': 'success', 'message':'Mensagem de grupo/status ignorada'}), 200
    
    if is_ai_content:
        waha = Waha()
        ai_bot = AiBot()

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