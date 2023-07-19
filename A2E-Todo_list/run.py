from app import app, database

if __name__ == '__main__':
    database.initialize_database()
    app.run(debug=True, host='0.0.0.0', port='5000')

