import helper
import parser

from sources import Sources

class Fetcher:
    def __init__(self, path = "./config/config.json"):
        self.config = helper.load_config(path)
        self.session_id = self.config["instagram_session_id"]
        self.max_posting_age = self.config["max_posting_age"]

        self.source = Sources(self.session_id)

    def fetch_simplify_internships(self):
        positions = []
        previous_company = None

        html = self.source.get_simplify_readme()
        postings = parser.extract_simplify_postings(html)
        if postings is None:
            # Logging should go here
            return

        for position in postings:
            position_information = parser.get_position_information(position, previous_company)
            if position_information is None:
                # Implement some logging
                return
            previous_company = position_information["company"]
            positions.append(position_information)

        positions = helper.filter_positions(positions, self.max_posting_age)
        return positions

    def listen_for_stories(self):
        pass
if __name__ == "__main__":
    positions = Fetcher().fetch_simplify_internships()
    print(positions[0])