from flask import jsonify, request
from app.models import Task

def get_tasks():
    tasks = Task.objects()
    return jsonify(tasks)

def create_task():
    data = request.get_json()
    description = data.get('description')
    task = Task(description=description)
    task.save()
    return jsonify(task)

def get_task(task_id):
    task = Task.objects.get_or_404(id=task_id)
    return jsonify(task)

def update_task(task_id):
    task = Task.objects.get_or_404(id=task_id)
    data = request.get_json()
    description = data.get('description')
    completed = data.get('completed')
    task.description = description if description is not None else task.description
    task.completed = completed if completed is not None else task.completed
    task.save()
    return jsonify(task)

def delete_task(task_id):
    task = Task.objects.get_or_404(id=task_id)
    task.delete()
    return jsonify({'message': 'Task deleted successfully'})

