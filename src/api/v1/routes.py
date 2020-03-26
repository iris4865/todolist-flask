import json

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

from src.app import app, db
from src.models.task import Task

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/api/task/', methods=['GET'])
def get_all_task():
    tasks = [task.to_dict() for task in Task.query.all()]
    return make_response(json.dumps(tasks, ensure_ascii=False), 200)


@app.route('/api/task/', methods=['POST'])
def add_task():
    json_data = request.get_json()

    title = json_data['title']
    description = json_data['description']
    priority = db.session.query(db.func.max(Task.priority)).scalar()
    print(priority)
    priority = 1 if priority == None else priority + 1
    end_date = json_data['end_date']
    complete = json_data['complete']

    task = Task(title=title, description=description, priority=priority, end_date=end_date, complete=complete)

    db.session.add(task)
    db.session.commit()

    return make_response(json.dumps({'message': 'Task created!'}, ensure_ascii=False), 200)


@app.route('/api/task/<id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    
    json_data = request.get_json()
    
    task.title = json_data.get('title', task.title)
    task.description = json_data.get('description', task.description)
    task.end_date = json_data.get('end_date', task.end_date)
    task.priority = json_data.get('priority', task.priority)
    task.complete = json_data.get('complete', task.complete)
    db.session.commit()

    return make_response(json.dumps({'message': 'Task updated!'}, ensure_ascii=False), 200)


@app.route('/api/task/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return make_response(json.dumps({'message': 'Task deleted!'}, ensure_ascii=False), 200)
