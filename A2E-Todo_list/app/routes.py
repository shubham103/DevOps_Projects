from app import app
from app.controllers import *

app.add_url_rule('/tasks', 'get_tasks', get_tasks, methods=['GET'])
app.add_url_rule('/tasks', 'create_task', create_task, methods=['POST'])
app.add_url_rule('/tasks/<task_id>', 'get_task', get_task, methods=['GET'])
app.add_url_rule('/tasks/<task_id>', 'update_task', update_task, methods=['PUT'])
app.add_url_rule('/tasks/<task_id>', 'delete_task', delete_task, methods=['DELETE'])

