import MessageClass
import sqlite3
import json
Message = MessageClass.Message

class Post:
    def __init__(self, request):
        self.request = request
        self.properties = ["application_id", "session_id", "message_id", "participant", "content"]
        self.conn = sqlite3.connect('messages.db')

    def __contains_all_prop(self):
        list_of_keys = str(self.request.get_json())
        for p in self.properties:
            if p not in list_of_keys:
                return False
        return True
    
    def __are_ssn_and_msg_unique(self):
        cur = self.conn.cursor()
        data = self.request.get_json()
        ssn_id = data["session_id"]
        msg_id = data["message_id"]
        if msg_id == None or ssn_id == None:
            print(msg_id,ssn_id)
            return False
        sql_ssn = f'SELECT session_id FROM messages WHERE session_id = "{ssn_id}"'
        sql_msg = f'SELECT message_id FROM messages WHERE message_id = "{msg_id}"'
        cur.execute(sql_ssn)
        if cur.fetchone() != None:
            return False
        self.conn.commit()
        cur.execute(sql_msg)
        if cur.fetchone() != None:
            return False
        self.conn.commit()
        return True
    
    def add_message(self):
        if not self.__contains_all_prop() or not self.__are_ssn_and_msg_unique():
            if not self.__contains_all_prop():
                return "Data is not valid, it does'nt contain all properties."
            else:
                return "Message_id or Session_id are not unique"
        with self.conn:
            data = self.request.get_json()  #recieve message data as json from post request
            msg = Message(data)  #create a message obj from data 
            sql = f'''INSERT INTO messages(application_id, session_id, message_id, participants, content)                    
            VALUES({msg.get_all_properties()})'''
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
        return 'success'