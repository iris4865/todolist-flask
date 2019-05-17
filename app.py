from flask import Flask, jsonify, request
from flask_cors import CORS

TODOLIST = [
    {
        'id': 0,
        'title': 'title1',
        'contents': '1111',
        'priority': 0,
        'create_date': '2019.05.17 17:00:00',
        'end_date': '2019.05.18 17:00:00',
        'complete': True
    },
    {
        'id': 1,
        'title': 'title2',
        'contents': '2222',
        'priority': 1,
        'create_date': '2019.05.17 21:00:00',
        'end_date': '2019.05.18 18:00:00',
        'complete': False
    },
]

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/todolist', methods=['GET'])
def ping_pong():
    return jsonify(TODOLIST)


if __name__ == '__main__':
    app.run()
