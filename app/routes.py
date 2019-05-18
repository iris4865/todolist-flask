import json

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

from app import app, db
from app.models import Task

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/api/task/', methods=['GET'])
def get_all_task():
    tasks = [task.to_dict() for task in Task.query.all()]
    return make_response(json.dumps(tasks, ensure_ascii=False), 200)


@app.route('/api/task/', methods=['POST'])
def add_task():
    task = get_task(request.get_json())
    db.session.add(task)
    db.session.commit()

    return make_response(json.dumps({'message': 'Task created!'}, ensure_ascii=False), 200)


@app.route('/api/task/<id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    task = get_task(request.get_json(), task)
    db.session.commit()

    return make_response(json.dumps({'message': 'Task updated!'}, ensure_ascii=False), 200)


@app.route('/api/task/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return make_response(json.dumps({'message': 'Task deleted!'}, ensure_ascii=False), 200)


def get_task(json_data, task=None):
    title = json_data['title']
    description = json_data['description']
    end_date = json_data['end_date']
    complete = json_data['complete']

    if task == None:
        return Task(title=title, description=description, end_date=end_date, complete=complete)
    else:
        task.title = title
        task.description = description
        task.end_date = end_date
        task.complete = complete
        return task
