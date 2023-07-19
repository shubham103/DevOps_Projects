from app import app
from app.models import db

def initialize_database():
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb://localhost/todo'
    }
    db.init_app(app)

