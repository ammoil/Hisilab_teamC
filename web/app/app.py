# web/app.py

from flask import Flask, render_template, request, session, redirect,url_for, jsonify
from .db import get_users
from .db import get_groupsschedule
from .db import get_groupssetting, get_groupsschedule_by_group_id
from .db import groupssetting
from .db import create_schedule
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return render_template('index.html')

    @app.route('/users')
    def users():
        return get_users() #URL変える

    @app.route('/groupsschedule')
    def groupsschedule():
        return get_groupsschedule() #URL変える
    
    # グループ追加画面に進む
    @app.route('/add_group')
    def add_group():
        return render_template('addGroup.html')

    # グループ名が入力されて作成ボタンが押された場合の処理
    @app.route('/groupssetting',methods=['POST'])
    def groupSsetting():
        if request.method == 'POST':
            group_name = request.form['group_name'] # フォームから送信されたグループ名を取得
            groupssetting(group_name)   # グループを作成するgroupssetting関数の呼び出し
            # データを更新するために、"my_dict"にスケジュールとグループ名を入れる
            my_dict = {
                'events': get_groupsschedule(),
                'groups':get_groupssetting()
            }
            return render_template('calendar.html', my_dict=my_dict) # "my_dict"の情報をカレンダー画面に渡す       
        else :  # 例外処理
            return "グループの作成に失敗しました。"
    
    @app.route('/events')
    def events():
        return 'Hello World!'
    
    @app.route('/calendar', methods=['GET', 'POST'])
    def calendar():
        if request.method == 'POST':
            group_id = request.form.get('group_id')
            selected_group_events = get_groupsschedule_by_group_id(group_id)
            print(f"Selected group ID: {group_id}")
            print(f"Events: {selected_group_events}")
            my_dict = {
                'events': selected_group_events,
                'groups': get_groupssetting()
            }
        else:
            my_dict = {
                'events': get_groupsschedule(),
                'groups': get_groupssetting()
            }
        
        return render_template('calendar.html', my_dict=my_dict)

    @app.route('/add_schedule', methods=['GET'])
    def add_schedule_form():
        groups = get_groupssetting()
        return render_template('add.html', groups=groups)

    @app.route('/add_schedule', methods=['POST'])
    def add_schedule():
        schedulename = request.form['schedulename']
        date = request.form['date']
        groupnumber = request.form['groupnumber']
        studentnumber = request.form['studentnumber']

        create_schedule(schedulename, date, groupnumber, studentnumber)
        return redirect(url_for('calendar'))


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