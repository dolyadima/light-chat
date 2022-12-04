import datetime
import json
from flask import Flask, request


from env import HOST, PORT, DEBUG


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Glory to Ukraine</title>
    <link rel="icon" type="image/x-icon" href="/static/img/ukraine.ico">
    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />

    <!-- fonts google com -->    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap" rel="stylesheet">
    
    <script type="text/javascript" src="/static/js/jquery-3.6.1.min.js"></script>
    <script type="text/javascript" src="/static/js/main.js"></script>
</head>
<body>
    <div class="content">
        <img src="/static/img/trident_ua.png"> <br />
        
        <div class="nickname" id="nickname_div">
            <label for="id_nickname">Nickname:</label>
            <input type="text" id="id_nickname">
            <input type="button" id="id_btn_nickname" onclick="set_nickname()" value=" Apply ">
            <input type="hidden" id="nickname_hidden" value="">
        </div>
        
        <div class="chat" id="chat_div">
            <label for="id_list_messages">List messages:</label> <br />
            <textarea id="id_list_messages" rows="20" cols="44"></textarea> <br />
            <label for="id_text_message">Message:</label>
            <input type="text" id="id_text_message">
            <input type="button" id="id_btn_send" onclick="send_message()" value=" Send ">
        </div>
    </div>
</body>
</html>
    '''


@app.route('/list_messages', methods=['GET'])
def list_messages():
    with open(f'./list_messages.txt', 'r') as fr:
        lines: list = fr.readlines()
        lines = lines[-50:] if len(lines) > 50 else lines
        result: dict = {
            'list_messages': '\n'.join([s.strip() for s in lines])
        }
    return json.dumps(result, indent=4)


@app.route('/new_message', methods=['POST'])
def new_message():
    data: dict = request.json
    if data.get('message', ''):
        with open(f'./list_messages.txt', 'a') as fw:
            fw.write(f'{datetime.datetime.now().strftime("%H:%M:%S")} {data["message"]}\n')
        return '{ "status": "200 OK" }'
    else:
        return '{ "status": "ERROR" }'


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
