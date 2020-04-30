
class Message:
    def __init__(self, data):
        self.application_id = data['application_id']
        self.session_id = data['session_id']
        self.message_id = data['message_id']
        self.participants = data['participants']
        self.content = data['content']

    def get_application_id(self):
        return self.application_id

    def get_session_id(self):
        return self.session_id

    def get_message_id(self):
        return self.message_id

    def get_content(self):
        return self.content

    def get_all_properties(self):
        return f'''{str(self.application_id)}, "{self.session_id}", "{self.message_id}",
        "{self.participants}", "{self.content}"'''