

from .enums import *
from .utils import *
from .exceptions import *
import requests
import urllib
import logging


logger = logging.getLogger(__name__)
VALID_PERF_TYPES = [_.value for _ in PerfType]


class Client:
    def __init__(self, token=None):
        self.url = "https://lichess.org/"
        self.s = requests.Session()  # keep session alive to improve performance <3
        if token:
            self.token = token
            # self.s.headers.update(token)

    def request(self, path, oauth=False, post_data=None, *args, **kwargs):
        full_url = urllib.parse.urljoin(self.url, path)
        print("hitting this URL:", full_url)

        try:
            if oauth:
                print("OAUTH status:", oauth)
                response = self.s.get(full_url, headers={"Authorization": f"Bearer {self.token}"})
            else:
                response = self.s.get(full_url)
            # res = requests.get(address, timeout=30)  # add timeout
        except requests.exceptions.RequestException as err:
            logger.error(err)
            raise

        # print(response.content)
        # print(response.text)

        # print("response.status_code", response.status_code)

        # remove this below eventually
        # call format.py or formats.py file to convert to JSON
        # https://docs.python-requests.org/en/latest/user/quickstart/#json-response-content
        # may get 204 (No Content)
        # if the response contains invalid JSON, attempting r.json() raises requests.exceptions.JSONDecodeError
        if response.status_code == 200:
            response2json = response.json()
            print(type(response2json))
            # if isinstance(response2json, list):
            #     return response2json[0]
            return response2json
        else:
            # There is some error in response
            print("ERROR!", response.status_code)
            return

    # -- Account --------------------------------------------------------------

    def get_profile(self):
        """Get your public profile information

        :return: A dictionary with your public information
        :rtype: dict
        """
        endpoint = "api/account"
        return self.request(path=endpoint, oauth=True)

    def get_email(self):
        """Get your email address

        :return: A dictionary with your email address
        :rtype: dict
        """
        endpoint = "api/account/email"
        return self.request(path=endpoint, oauth=True)

    def get_preferences(self):
        """Get your preferences

        :return: A dictionary with your preferences
        :rtype: dict
        """
        endpoint = "api/account/preferences"
        return self.request(path=endpoint, oauth=True)

    def get_kid_mode(self):
        """Get your kid mode status

        :return: A dictionary with your kid mode status
        :rtype: dict
        """
        endpoint = "api/account/kid"
        return self.request(path=endpoint, oauth=True)

    """
    Implement post ability in client.py
    """
    # def set_kid_mode(self):
    #     """Set your kid mode status
    #
    #     :return:
    #     :rtype:
    #     """
    #     endpoint = "api/account/kid"
    #     # POST
    #     pass

    # -- Users ----------------------------------------------------------------

    def get_status(self, *users, with_game_ids=False):
        """Get real-time status of one or more users

        :param users: User to query their real-time status
        :type users: str
        :param with_game_ids: Flag to know whether or not include the ID of games being played, if any, for each player
        :type with_game_ids: bool, optional
        :return: A list with a nested dictionary containing the real-time status of one or more users
        :rtype: list
        """
        invalid_inputs = [usr for usr in users if not valid_input(usr)]
        if invalid_inputs:
            raise ArgumentValueError("One or more usernames are invalid.")

        endpoint = "api/users/status"
        path = endpoint + "?ids=" + ','.join(users)

        if with_game_ids:
            path += "&withGameIds=true"

        return self.request(path=path)

    """
    Create function in utils.py to manually parse these two responses (JSON problems)
    """
    # def get_top_ten(self):
    #     """Get the top 10 players for each speed and variant
    #
    #     :return:
    #     """
    #     endpoint = "player"
    #     return self.request(path=endpoint)
    #
    # def get_leaderboard(self, perf_type, num_users):
    #     """Get leaderboard of an individual speed or variant
    #
    #     :return:
    #     """
    #     if perf_type not in VALID_PERF_TYPES:
    #         raise ArgumentValueError("Value of perf_type is invalid.")
    #     if (num_users <= 0) or (200 < num_users):
    #         raise ArgumentValueError("Value of num_users is invalid. Valid range includes any integer from 1 to 200")
    #
    #     endpoint = "player/top/{nb}/{perfType}"
    #     path = endpoint.format(nb=num_users, perfType=perf_type)
    #     return self.request(path=path)

    def get_data(self, user):
        """Get public data of an individual user

        :param user: User to query their public data
        :type user: str
        :return: A dictionary with the public data of the user
        :rtype: dict
        """
        if not valid_input(user):
            raise ArgumentValueError("Value of user is invalid.")

        endpoint = "api/user/{username}"
        path = endpoint.format(username=user)
        return self.request(path=path)

    def get_rating_history(self, user):
        """Get rating history of an individual user

        :param user: User to query their public data
        :type user: str
        :return: A list with a nested dictionary containing the rating history of the user
        :rtype: list
        """
        if not valid_input(user):
            raise ArgumentValueError("Value of user is invalid.")

        endpoint = "api/user/{username}/rating-history"
        path = endpoint.format(username=user)
        return self.request(path=path)

    """
    Possibly add Enum for PerfType (also related to the get_leaderboard() method)
    """
    def get_stats(self, user, perf_type):
        """Get performance statistics of an individual user

        :param user: User to query their performance statistics
        :type user: str
        :param perf_type: Type of speed or variant to query
        :type user: str
        :return: A dictionary with the performance statistics of the user
        :rtype: dict
        """
        if not valid_input(user):
            raise ArgumentValueError("Value of user is invalid.")
        if perf_type not in VALID_PERF_TYPES:
            raise ArgumentValueError("Value of perf_type is invalid.")

        endpoint = "api/user/{username}/perf/{perf}"
        path = endpoint.format(username=user, perf=perf_type)
        return self.request(path=path)

    def get_activity(self, user):
        """Get the activity feed of an individual user

        :param user: User to query their activity feed
        :type user: str
        :return: A list with a nested dictionary containing the activity feed of the user
        :rtype: list
        """
        if not valid_input(user):
            raise ArgumentValueError("Value of user is invalid.")

        endpoint = "api/user/{username}/activity"
        path = endpoint.format(username=user)
        return self.request(path=path)

    def get_by_id():
        """
        Get users by ID

        :return:
        """
        endpoint = "api/users"
        pass


    # def get_team_members():
    #     """
    #     Get members of a team
    #
    #     :return:
    #     """
    #     endpoint = "api/team/{teamId}/users"
    #     pass
    #
    #
    # def get_live_streamers():
    #     """
    #     Get live streamers
    #
    #     :return:
    #     """
    #     endpoint = "streamer/live"
    #     pass
    #
    #
    # def get_crosstable():
    #     """
    #     Get crosstable
    #
    #     :return:
    #     """
    #     endpoint = "api/crosstable/{user1}/{user2}"
    #     pass


    # # CUSTOM
    # def get_followers():
    #     endpoint =
    #     pass
    #
    # # CUSTOM
    # def get_following():
    #     endpoint =
    #     pass

    # -- Relations ------------------------------------------------------------

    def relations(self):
        endpoint = "api/rel/following"
        return self.request(path=endpoint, oauth=True)

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

