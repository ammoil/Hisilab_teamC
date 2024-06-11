# web/app.py

from flask import Flask
from .db import get_users
from .db import get_groupsschedule
from .db import get_groupssetting

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello World!'

    @app.route('/users')
    def users():
        return get_users() #URL変える

    @app.route('/groupsschedule')
    def groupsschedule():
        return get_groupsschedule() #URL変える

    @app.route('/groupssetting')
    def groupssetting():
        return get_groupssetting() #URL変える


    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

# from flask import Flask

# def create_app():
#     app = Flask(__name__)
#     # app configuration and routes setup here

#     return app

# app = create_app()

# from flask import Flask, jsonify
# import mysql.connector

# app = Flask(__name__)

# def conn_db():
#     conn = mysql.connector.connect(
#         host='mysql-container',
#         user='root',
#         password='root',
#         database='demo'
#     )
#     return conn

# @app.route('/')
# def hello():
#     return 'Hello World!'

# @app.route('/users')
# def get_users():
#     conn = conn_db()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM users')
#     rows = cursor.fetchall()
#     cursor.close()
#     conn.close()

#     users = [{'id': row[0], 'name': row[1], 'email': row[2]} for row in rows]
#     return jsonify(users)

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')




# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello World!'