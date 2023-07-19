from app.database import db

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def save(self):
        db.tasks.insert_one(self.__dict__)

    @staticmethod
    def find_all():
        return list(db.tasks.find())

    @staticmethod
    def find_by_id(task_id):
        return db.tasks.find_one({"_id": task_id})

    def update(self):
        db.tasks.update_one({"_id": self._id}, {"$set": self.__dict__})

    def delete(self):
        db.tasks.delete_one({"_id": self._id})
