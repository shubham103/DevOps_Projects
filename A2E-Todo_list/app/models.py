from flask_mongoengine import MongoEngine

db = MongoEngine()

class Task(db.Document):
    description = db.StringField(required=True)
    completed = db.BooleanField(default=False)

