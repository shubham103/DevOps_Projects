from flask import jsonify, request
from bson import ObjectId
from app.models import Task

def get_tasks():
    tasks = Task.find_all()
    return jsonify(tasks)

def create_task():
    data = request.get_json()
    description = data.get('description')
    task = Task(description=description)
    task.save()
    return jsonify(task.__dict__)

def get_task(task_id):
    task = Task.find_by_id(ObjectId(task_id))
    return jsonify(task)

def update_task(task_id):
    data = request.get_json()
    description = data.get('description')
    completed = data.get('completed')
    task = Task.find_by_id(ObjectId(task_id))
    task.description = description if description is not None else task.description
    task.completed = completed if completed is not None else task.completed
    task.update()
    return jsonify(task)

def delete_task(task_id):
    task = Task.find_by_id(ObjectId(task_id))
    task.delete()
    return jsonify({'message': 'Task deleted successfully'})
