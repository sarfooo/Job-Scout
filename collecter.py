import helper
import parser

from sources import Sources

class Collecter:
    def __init__(self, session_id):
        self.source = Sources(session_id)

    def get_simplify_positions(self):
        body = self.source.get_simplify_readme()

        tables = parser.extract_position_table(body)

        positions = parser.extract_position_rows(tables)

        return positions

    def get_sudo_stories(self):
        pass



if __name__ == "__main__":
    positions = Collecter().get_simplify_positions()
    print(positions[0])