import requests

def setup_api():
    import auth
    api = API(auth.key, test=False)

    return api

class API:
    def __init__(self, key, test=True):
        self.key = key

        if test:
            self.id = "205790"
        else:
            self.id = "570"

    def get_heroes(self):
        url = "http://api.steampowered.com/IEconDOTA2_{}/GetHeroes/v1".format(self.id)
        params = {
            "key": self.key,
            "language": "en-us"
        }

        r = requests.get(url, params=params)

        if not r.status_code == 200:
            print("Request error: {}".format(r.status_code))
            return None
        else:
            print("Success!")
            return r.json()["result"]["heroes"]

    def get_items(self):
        url = "http://api.steampowered.com/IEconDOTA2_{}/GetGameItems/v1".format(self.id)
        params = {
            "key": self.key,
            "language": "en-us"
        }

        r = requests.get(url, params=params)

        if not r.status_code == 200:
            print("Request error: {}".format(r.status_code))
            return None
        else:
            print("Success!")
            return r.json()["result"]["items"]

    def vanity_to_id(self, vanity, bit=32):
        if not (bit == 64 or bit == 32):
            print("Error: id must be 32-bit or 64-bit")
            return None

        url = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/"
        params = {
            "key": self.key,
            "vanityurl": vanity
        }

        r = requests.get(url, params=params)

        if not r.status_code == 200:
            print("Request error: {}".format(r.status_code))
            return None
        else:
            if r.json()["response"]["success"] == 1:
                if bit == 64:
                    return r.json()["response"]["steamid"]
                else:
                    return str(int(r.json()["response"]["steamid"]) - 76561197960265728)
            else:
                print("API error: {}".format(r.json()["response"]["message"]))
                return None

    def get_match_history(self, matches=25, user_id=None, before_id=None, hero_id=None):
        url = "http://api.steampowered.com/IDOTA2Match_{}/GetMatchHistory/v1".format(self.id)
        params = {
            "key": self.key,
            "matches_requested": matches
        }

        if user_id:
            params["account_id"] = user_id

        if hero_id:
            params["hero_id"] = hero_id

        if before_id:
            params["start_at_match_id"] = before_id - 1

        r = requests.get(url, params=params)

        if not r.status_code == 200:
            print("Request error: {}".format(r.status_code))
            return None
        else:
            print("Success!")
            return r.json()["result"]["matches"]

    def get_match_details(self, match_id):
        url = "http://api.steampowered.com/IDOTA2Match_{}/GetMatchDetails/v1".format(self.id)
        params = {
            "key": self.key,
            "match_id": match_id
        }

        r = requests.get(url, params=params)

        if not r.status_code == 200:
            print("Request error: {}".format(r.status_code))
            return None
        else:
            print("Success!")
            return r.json()["result"]
