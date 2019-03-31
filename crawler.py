import auth
from API import API
import sqlite3
import time

class Crawler:
    def __init__(self):
        self.api = API(auth.key, test=False)

    def crawl(self, vanity):
        connection = sqlite3.connect("{}.db".format(vanity))
        c = connection.cursor()

        user_id = self.api-vanity_to_id(vanity)
        time.sleep(1)

        result = api.get_match_history(user_id, matches=100)
        time.sleep(1)
        matches = result["matches"]

        match_ids = []
        heroes = []
        teammates = []
        enemies = []

        for match in matches:
            match_ids.append(match["match_id"])
            is_radiant = True
            radiant = []
            dire = []

            """FUCKED UP"""
            for player in match["players"]:
                if player["player_slot"] < 5:
                    radiant.append(player["hero_id"])
                else:
                    dire.append(player["hero_id"])
                    if player["account_id"] == user_id:
                        is_radiant = False

            if is_radiant:
                teammates += radiant



        c.execute(
        """
            CREATE TABLE matches (
                match_id integer PRIMARY KEY,
                hero integer,
                teammate_1 integer,
                teammate_2 integer,
                teammate_3 integer,
                teammate_4 integer,
                enemy_1 integer,
                enemy_2 integer,
                enemy_3 integer,
                enemy_4 integer,
                enemy_5 integer,
                win integer
            )
        """
        )

        c.executemany(
        """
            INSERT INTO matches VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,

        )

        connection.commit()
        connection.close()
