from flask import Flask, request, jsonify
import sqlite3
from methods.post import Post
from methods.get import Get
from methods.delete import Delete
app = Flask(__name__)    

#create_database
# conn = sqlite3.connect('messages.db')
# with conn:
#     cur = conn.cursor()
#     cur.execute("""CREATE TABLE messages(
#         id INTEGER PRIMARY KEY AUTOINCREMENT, 
#         application_id INTEGER,
#         session_id TEXT, 
#         message_id TEXT, 
#         participants BOLB,
#         content TEXT
#     )""")
#     conn.commit()

@app.route('/AddMessage', methods = ['POST'])
def add_message():
    p = Post(request)
    return p.add_message()

@app.route('/GetMessage', methods = ['GET'])
def get_message():
    g = Get(request)
    list_of_messages = g.get_message()
    return jsonify(list_of_messages)

@app.route('/DeleteMessage', methods = ['DELETE'])
def delete_message():
    d = Delete(request)
    return d.delete_message()

if __name__ == '__main__':
    app.run(debug = True)