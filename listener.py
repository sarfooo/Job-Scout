import helper
import parser

from sources import Sources

class Fetcher:
    def __init__(self, path = "./config"):
        self.config = helper.load_config(path)
        self.session_id = self.config["instagram_session_id"]
        self.max_posting_age = self.config["max_posting_age"]

        self.source = Sources(self.session_id)

    def fetch_simplify_internships(self):
        html = self.source.get_simplify_readme()
        positions = parser.get_position_information()
        previous_company = None

        for position in previous_company:
            position_information = parser.get_position_information(position)
            if position_information is None:
                # Implement some logging
                return
            previous_company = position_information["company"]



    def listen_for_stories(self):
        pass
