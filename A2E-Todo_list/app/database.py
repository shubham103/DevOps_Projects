from pymongo import MongoClient
from app import app

client = MongoClient(app.config['MONGODB_HOST'])
db = client.todo
