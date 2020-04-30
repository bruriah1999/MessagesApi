import MessageClass
import sqlite3
import json
Message = MessageClass.Message

class Get:
    def __init__(self, request):
        self.request = request
        self.app_id = self.request.args.get("application_id")
        self.ssn_id = self.request.args.get("session_id")
        self.msg_id = self.request.args.get("message_id")
        self.conn = sqlite3.connect('messages.db')
    
    def __only_one_arg(self):     
        list_of_all = [self.app_id, self.ssn_id, self.msg_id]
        if(list_of_all.count(None)  != 2):
            return False
        return True

    def __get_argument(self):
        if self.app_id != None:
            return ('application_id', self.app_id)
        elif self.ssn_id != None:
            return ('session_id', self.ssn_id)
        else:
            return ('message_id', self.msg_id)

    def get_message(self):
        if not self.__only_one_arg():
            return 'There are more than one argument'
        get_message_by = self.__get_argument()
        sql = f"SELECT content FROM messages WHERE {get_message_by[0]} = '{get_message_by[1]}'"
        with self.conn:
            cur = self.conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            self.conn.commit()
            if len(rows) == 0:
                return "There is no data regarding to your request"
            return rows