import re
import parser
import requests

SIMPLIFY_README = "https://raw.githubusercontent.com/SimplifyJobs/Summer2027-Internships/refs/heads/dev/README.md"

class Sources:
    def __init__(self, session_id):
        self.session_id = session_id
        self.session = requests.Session()

    def get_simplify_readme(self):
        response = self.session.get(SIMPLIFY_README)
        response.raise_for_status()
        return re.findall(r"<table\b[^>]*>[\s\S]*?<\/table>", response.text)[0]

    def get_sudo_story(self):
        # todo
        pass