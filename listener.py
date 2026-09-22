import helper

class Listener:
    def __init__(self, path = "./config"):
        self.config = helper.load_config(path)
        self.session_id = self.config["instagram_session_id"]
        self.max_posting_age = self.config["max_posting_age"]

    def listen_for_postings(self):
        pass

    def listen_for_stories(self):
        pass
