import auth
from API import setup_api
import sqlite3
import time

class Crawler:
    def __init__(self):
        self.api = setup_api()

    def store_matches(self, num_matches):
        connection = sqlite3.connect("dota-guru.db")
        c = connection.cursor()

        t = time.time()
        matches = api.get_match_history(matches=100)

        # parse out match_ids (and validation info?)

        # store them in the table "matches"

        connection.commit()
        connection.close()
