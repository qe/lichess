

# from .utils import *
import requests
import urllib


_ROOT_URL = "https://lichess.org/"


class Client:
    def __init__(self):
        self.url = _ROOT_URL

    def request(self, path, post_data=None, params=None, *args, **kwargs):
        full_url = urllib.parse.urljoin(self.url, path)

        # GET method
        if not post_data:
            response = requests.get(full_url)
        #
        else:
            print("POST method!!!")
            return

        # print("response.status_code", response.status_code)

        # remove this below eventually
        # call format.py or formats.py file to convert to JSON
        # https://docs.python-requests.org/en/latest/user/quickstart/#json-response-content
        # may get 204 (No Content)
        # if the response contains invalid JSON, attempting r.json() raises requests.exceptions.JSONDecodeError
        if response.status_code == 200:
            response2json = response.json()
            # if isinstance(response2json, list):
            #     return response2json[0]
            return response2json
        else:
            # There is some error in response
            print("ERROR!", response.status_code)
            return

    def get(self, path, params=None, *args, **kwargs):
        # may need to take authorization and format into account
        return self.request(path)

    # def post(self, path, post_data=None, params=None, *args, **kwargs):
    #     pass


client = Client()


# -- Users ----------------------------------------------------------------

def get_status(*users, with_game_ids=False):
    """
    Get real-time users status

    :return:
    """
    endpoint = "api/users/status"
    path = endpoint + "?ids=" + ','.join(users)

    if with_game_ids:
        path += "&withGameIds=true"

    return client.get(path=path)


def get_top_ten():
    """
    Get all top 10

    :return:
    """
    endpoint = "player"
    pass


def get_leaderboard():
    """
    Get one leaderboard

    :return:
    """
    endpoint = "player/top/{nb}/{perfType}"
    pass


def get_data(username):
    """
    Get user public data

    :param username:
    :return:
    """
    endpoint = "api/user/{username}"
    path = endpoint.format(username=username)
    # print(path)
    return client.get(path=path)


def get_rating_history():
    """
    Get rating history of a user

    :return:
    """
    endpoint = "api/user/{username}/rating-history"
    pass


def get_stats():
    """
    Get performance statistics of a user

    :return:
    """
    endpoint = "api/user/{username}/perf/{perf}"
    pass


def get_activity():
    """
    Get user activity

    :return:
    """
    endpoint = "api/user/{username}/activity"
    pass


def get_by_id():
    """
    Get users by ID

    :return:
    """
    endpoint = "api/users"
    pass


def get_team_members():
    """
    Get members of a team

    :return:
    """
    endpoint = "api/team/{teamId}/users"
    pass


def get_live_streamers():
    """
    Get live streamers

    :return:
    """
    endpoint = "streamer/live"
    pass


def get_crosstable():
    """
    Get crosstable

    :return:
    """
    endpoint = "api/crosstable/{user1}/{user2}"
    pass


# # CUSTOM
# def get_followers():
#     endpoint =
#     pass
#
# # CUSTOM
# def get_following():
#     endpoint =
#     pass


# -- Account --------------------------------------------------------------
# -- Relations ------------------------------------------------------------
# -- Games ----------------------------------------------------------------
# -- TV -------------------------------------------------------------------
# -- Puzzles --------------------------------------------------------------
# -- Teams ----------------------------------------------------------------
# -- Board ----------------------------------------------------------------
# -- Bot ------------------------------------------------------------------
# -- Challenges -----------------------------------------------------------
# -- Bulk pairings --------------------------------------------------------
# -- Arena tournaments ----------------------------------------------------
# -- Swiss Tournaments ----------------------------------------------------
# -- Simuls ---------------------------------------------------------------
# -- Studies --------------------------------------------------------------
# -- Messaging ------------------------------------------------------------
# -- Broadcasts -----------------------------------------------------------
# -- Analysis -------------------------------------------------------------
# -- Opening Explorer -----------------------------------------------------
# -- Tablebase ------------------------------------------------------------
# -- OAuth ----------------------------------------------------------------

