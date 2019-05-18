from flask import Flask, jsonify, request
from flask_cors import CORS

TODOLIST = [
    {
        'id': 0,
        'title': 'title1',
        'description': '1111',
        'priority': 0,
        'create_date': '2019-05-17',
        'end_date': '2019-05-18',
        'complete': True
    },
    {
        'id': 1,
        'title': 'title2',
        'description': '2222',
        'priority': 1,
        'create_date': '2019-05-17',
        'end_date': '2019-05-18',
        'complete': False
    },
]

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/api/task/', methods=['GET'])
def get_all_task():
    print('get all task.')
    return jsonify(TODOLIST)


@app.route('/api/task/', methods=['POST'])
def add_task():
    response_object = {'status': 'success'}
    title = request.get_json()['title']
    description = request.get_json()['description']
    end_date = request.get_json()['end_date']
    complete = request.get_json()['complete']

    TODOLIST.append(
        {
            'id': 2,
            'title': title,
            'description': description,
            'priority': 1,
            'create_date': '2019-05-17',
            'end_date': end_date,
            'complete': complete
        }
    )
    response_object['message'] = 'Task created!'
    return jsonify(response_object)


@app.route('/api/task/<id>', methods=['PUT'])
def update_task(id):
    print(request.get_json())
    print('update task')
    response_object = {'status': 'success'}
    response_object['message'] = 'Task updated!'

    id = int(id)
    TODOLIST[id]['title'] = request.get_json()['title']
    TODOLIST[id]['description'] = request.get_json()['description']
    TODOLIST[id]['end_date'] = request.get_json()['end_date']
    TODOLIST[id]['complete'] = request.get_json()['complete']
    return jsonify(response_object)


@app.route('/api/task/<id>', methods=['DELETE'])
def delete_task(id):
    print('delete task')
    response_object = {'status': 'success'}
    response_object['message'] = 'Task Deleted!'

    id = int(id)
    del TODOLIST[id]
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
