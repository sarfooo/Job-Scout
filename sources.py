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
        return re.findall(r"<table\b[^>]*>[\s\S]*?<\/table>", response.text)

    def get_sudo_story(self):
        # todo
        pass

if __name__ == "__main__":
    html_list = Sources("").get_simplify_readme()
    html = html_list[0]
    data = parser.extract_simplify_postings(html)
    previous_company = None
    for position in data:
        information = parser.get_position_information(position)
        previous_company = information["company"]
        print(information)