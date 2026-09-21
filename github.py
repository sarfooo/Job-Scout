import requests

SIMPLIFY_README = "https://raw.githubusercontent.com/SimplifyJobs/Summer2027-Internships/refs/heads/dev/README.md"


class GitHub:
    def __init__(self):
        self.session = requests.Session()

    def get_simplify_readme(self):
        response = self.session.get("")