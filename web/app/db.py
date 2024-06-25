# web/db.py

import mysql.connector
from flask import jsonify

def conn_db():
    conn = mysql.connector.connect(
        host='mysql-container',
        user='root',
        password='root',
        database='demo'
    )
    return conn

def get_users():
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    users = [{'id': row[0], 'name': row[1], 'studentnumber': row[2]} for row in rows]
    return jsonify(users)

def get_groupsschedule():
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM groupsschedule')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # groupsschedule = [{'id': row[0], 'schedulename': row[1], 'groupnumber': row[2], 'date': row[3], 'usersid': row[4]} for row in rows]
    # return jsonify(groupsschedule)
    groupsschedule = [{'id': row[0], 'schedulename': row[1], 'groupnumber': row[2], 'date': row[3], 'usersid': row[4]} for row in rows]
    return groupsschedule

def get_groupssetting():
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM groupssetting')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    groupssetting = [{'id': row[0], 'groupname': row[1]} for row in rows]
    return groupssetting

def get_groupsschedule_by_group_id(group_id):
    conn = conn_db()
    cursor = conn.cursor()
    query = 'SELECT * FROM groupsschedule WHERE groupnumber = %s'
    cursor.execute(query, (group_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    groupsschedule = [{'id': row[0], 'schedulename': row[1], 'groupnumber': row[2], 'date': row[3], 'usersid': row[4]} for row in rows]
    return groupsschedule

# グループを作成する関数
def groupssetting(group_name):
    conn = conn_db()    # データベースに接続
    cursor = conn.cursor()  # カーソルオブジェクトを作成
    cursor.execute('INSERT INTO groupssetting (groupname) VALUES (%s)', (group_name,))   # SQLクエリの実行
    # cursor.execute()では、INSERT INTO文を使って、新しいグループ名を"groupssetting"テーブルに挿入するSQLクエリを実行
    conn.commit()   # データベース対する変更を確定
    group_id = cursor.lastrowid # lastrowid属性を使用して自動生成されたIDを取得
    cursor.close()  # カーソルオブジェクトを閉じる
    conn.close()    # データベース接続を閉じる
    #return group_id, group_name  # IDとグループ名を返す
    return group_id

# 新しい予定を作成する関数
def create_schedule(schedulename, date, groupnumber, studentnumber):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO groupsschedule (schedulename, groupnumber, date, usersid) VALUES (%s, %s, %s, (SELECT id FROM users WHERE studentnumber = %s))', (schedulename, groupnumber, date, studentnumber))
    conn.commit()
    cursor.close()
    conn.close()