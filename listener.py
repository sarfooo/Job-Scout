import helper

from filter import Filter
from collecter import Collecter

class Listener:
    def __init__(self, config_path = "./config/config.json"):
        self._config = helper.load_config(config_path)

        self._filter = Filter(self._config["max_posting_age"])
        self._collecter = Collecter(self._config["instagram_session_id"])

    def listen_for_simplify_internships(self):
        # work on decorator for this to autorun
        positions = self._collecter.get_simplify_positions()
        if positions is None:
            # handle none positions
            return

        positions = self._filter.filter_positions(positions)

        # send for further processing