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