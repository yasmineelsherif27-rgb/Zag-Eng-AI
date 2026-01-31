from threading import Lock

class DataSync:
    def __init__(self):
        self.messages = []
        self.lock = Lock()  # Lock لمنع التعارض بين المستخدمين

    def add_message(self, user, message):
        with self.lock:
            self.messages.append((user, message))
            print(f"{user} added: {message}")

    def get_messages(self):
        return self.messages