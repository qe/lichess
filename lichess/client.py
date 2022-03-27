

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

# post_data
    def request(self, path, payload=None, oauth=False):
        parsed_url = urllib.parse.urljoin(self.url, path)

        try:
            if oauth:
                print("OAUTH status:", oauth)
                # PPOF: order of parameters ("headers" and "params" parameters)
                response = self.s.get(parsed_url, headers={"Authorization": f"Bearer {self.token}"}, params=payload)
                print("hitting this URL:", response.url)
            else:
                response = self.s.get(parsed_url, params=payload)
                print("hitting this URL:", response.url)
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
    POST
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

        :param str users: Users to query their real-time status
        :param Optional[bool] with_game_ids: Flag to include the ID of games being played, if any, for each player
        :return: A list with a nested dictionary containing the real-time status of one or more users
        :rtype: list
        """
        invalid_inputs = [usr for usr in users if not valid_input(usr)]
        if invalid_inputs:
            raise ArgumentValueError("One or more usernames are invalid.")

        endpoint = "api/users/status"

        payload = {
            "ids": ','.join(users),
            "withGameIds": with_game_ids,
        }

        return self.request(path=endpoint, payload=payload)

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

        :param str user: User to query their public data
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

        :param str user: User to query their public data
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

        :param str user: User to query their performance statistics
        :param str perf_type: Type of speed or variant to query
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

        :param str user: User to query their activity feed
        :return: A list with a nested dictionary containing the activity feed of the user
        :rtype: list
        """
        if not valid_input(user):
            raise ArgumentValueError("Value of user is invalid.")

        endpoint = "api/user/{username}/activity"
        path = endpoint.format(username=user)
        return self.request(path=path)

    """
    POST
    """
    # def get_by_id():
    #     """
    #     Get users by ID
    #
    #     :return:
    #     """
    #     endpoint = "api/users"
    #     pass

    """
    ndjson
    """
    # def get_team_members():
    #     """
    #     Get members of a team
    #
    #     :return:
    #     """
    #     endpoint = "api/team/{teamId}/users"
    #     pass

    def get_live_streamers(self):
        """Get the current live streamers

        :return: A list with a nested dictionary containing the current live streamers
        :rtype: list
        """
        endpoint = "streamer/live"
        return self.request(path=endpoint)

    def get_crosstable(self, user1, user2, matchup=False):
        """Get the crosstable of two users

        :param str user1: First user to compare with second user
        :param str user2: Second user to compare with first user
        :param Optional[bool] matchup: Flag to get current match data, if the two users are currently playing
        :return: A dictionary with the crosstable (total number of games and current score of the two users)
        :rtype: dict
        """
        endpoint = "api/crosstable/{user1}/{user2}"
        path = endpoint.format(user1=user1, user2=user2)

        if matchup:
            payload = {"matchup": True,}
            return self.request(path=path, payload=payload)
        else:
            return self.request(path=path)

    # -- Relations ------------------------------------------------------------

    """
    ndjson
    """
    # def following(self):
    #     """Get users who you are following
    #
    #     :return:
    #     :rtype:
    #     """
    #     endpoint = "api/rel/following"
    #     return self.request(path=endpoint, oauth=True)

    """
    POST
    """
    # def follow(self, player):
    #     """Follow a player
    #
    #     :param str player:
    #     :return:
    #     :rtype:
    #     """
    #     pass

    """
    POST
    """
    # def unfollow(self, player):
    #     """Unfollow a player
    #
    #     :param str player:
    #     :return:
    #     :rtype:
    #     """
    #     pass

    # -- Games ----------------------------------------------------------------

    def export_game(self, game_id, moves=True, pgn_in_json=False, tags=True, clocks=True, evals=True, opening=True, literate=False, players=None):
        """Download a game in either JSON or PGN format

        :param str game_id: ID of game to export
        :param Optional[bool] moves:
        :param Optional[bool] pgn_in_json:
        :param Optional[bool] tags:
        :param Optional[bool] clocks:
        :param Optional[bool] evals:
        :param Optional[bool] opening:
        :param Optional[bool] literate:
        :param Optional[str] players:
        :return:
        :rtype:
        """
        endpoint = "game/export/{gameId}"
        path = endpoint.format(gameId=game_id)

        payload = {
            "moves": moves,
            "pgnInJson": pgn_in_json,
            "tags": tags,
            "clocks": clocks,
            "evals": evals,
            "opening": opening,
            "literate": literate,
            "players": players,
        }
        return self.request(path=path, payload=payload)

    def export_ongoing(self, user, moves=True, pgn_in_json=False, tags=True, clocks=True, evals=True, opening=True, literate=False, players=None):
        """Download the ongoing game of a user in either JSON or PGN format

        :param str user: User whose ongoing game you want to export
        :param Optional[bool] moves:
        :param Optional[bool] pgn_in_json:
        :param Optional[bool] tags:
        :param Optional[bool] clocks:
        :param Optional[bool] evals:
        :param Optional[bool] opening:
        :param Optional[bool] literate:
        :param Optional[str] players:
        :return:
        :rtype:
        """
        endpoint = "api/user/{username}/current-game"
        path = endpoint.format(username=user)

        payload = {
            "moves": moves,
            "pgnInJson": pgn_in_json,
            "tags": tags,
            "clocks": clocks,
            "evals": evals,
            "opening": opening,
            "literate": literate,
            "players": players,
        }
        return self.request(path=path, payload=payload)

    def export_games(self, user, since=None, until=None, max_games=None, vs=None, rated=None, perf_type=None, color=None, analyzed=None, moves=True, pgn_in_json=False, tags=True, clocks=True, evals=True, opening=True, ongoing=False, finished=True, players=None, sort="dateDesc"):
        """Download all games of a user in PGN or ndjson format

        :param str user:
        :param Optional[int] since:
        :param Optional[int] until:
        :param Optional[int] max_games:
        :param Optional[str] vs:
        :param Optional[bool] rated:
        :param Optional[str] perf_type:
        :param Optional[str] color:
        :param Optional[bool] analyzed:
        :param Optional[bool] moves:
        :param Optional[bool] pgn_in_json:
        :param Optional[bool] tags:
        :param Optional[bool] clocks:
        :param Optional[bool] evals:
        :param Optional[bool] opening:
        :param Optional[bool] ongoing:
        :param Optional[bool] finished:
        :param Optional[str] players:
        :param Optional[str] sort:
        :return:
        :rtype:
        """
        endpoint = "api/user/{username}/current-game"
        path = endpoint.format(username=user)

        payload = {
            "since": since,
            "until": until,
            "max": max_games,
            "vs": vs,
            "rated": rated,
            "perfType": perf_type,
            "color": color,
            "analysed": analyzed,
            "moves": moves,
            "pgnInJson": pgn_in_json,
            "tags": tags,
            "clocks": clocks,
            "evals": evals,
            "opening": opening,
            "ongoing": ongoing,
            "finished": finished,
            "players": players,
            "sort": sort,
        }
        return self.request(path=path, payload=payload)

    """
    Export games by IDs
    
    Stream games of users
    
    Get my ongoing games
    
    Stream moves of a game
    
    Import one game    
    """

    # -- TV -------------------------------------------------------------------

    def get_games_channels(self):
        """Get the best games currently being played for each speed/variant, including computer games and bot games

        :return: A dictionary with info on the current TV games
        :rtype: dict
        """
        endpoint = "api/tv/channels"
        return self.request(path=endpoint)

    """
    ndjson
    """
    def stream_tv_game(self):
        """Stream positions and moves of the current TV game

        :return:
        :rtype:
        """
        endpoint = "api/tv/feed"
        return self.request(path=endpoint)

    """
    ndjson
    """
    def get_games_channel(self, channel, num_games=10, moves=True, pgn_in_json=False, tags=True, clocks=True, opening=True):
        """Get the best games currently being played for a specific speed/variant, including computer games and bot games

        :param str channel:
        :param Optional[bool] num_games:
        :param Optional[bool] moves:
        :param Optional[bool] pgn_in_json:
        :param Optional[bool] tags:
        :param Optional[bool] clocks:
        :param Optional[bool] opening:
        :return:
        :rtype:
        """
        endpoint = "api/tv/{channel}"
        path = endpoint.format(channel=channel)

        payload = {
            "nb": num_games,
            "moves": moves,
            "pgnInJson": pgn_in_json,
            "tags": tags,
            "clocks": clocks,
            "opening": opening,
        }
        return self.request(path=path, payload=payload)

    # -- Puzzles --------------------------------------------------------------
    def get_daily_puzzle(self):
        """Get the daily Lichess puzzle in JSON format

        :return:
        :rtype:
        """
        endpoint = "api/puzzle/daily"
        return self.request(path=endpoint)

    """
    ndjson
    """
    def get_puzzle_activity(self, max_entries=None):
        """Get your puzzle activity as NDJSON

        :param Optional[int] max_entries: Number of entries to download (leave empty to download all activity)
        :return:
        :rtype:
        """
        endpoint = "api/puzzle/activity"
        payload = {"max": max_entries,}
        return self.request(path=endpoint, payload=payload, oauth=True)

    def get_puzzle_dashboard(self, days):
        """Get your puzzle dashboard as JSON

        :param int days: Number of days to look back when aggregating puzzle results
        :return:
        :rtype:
        """
        endpoint = "api/puzzle/dashboard/{days}"
        path = endpoint.format(days=days)
        return self.request(path=path, oauth=True)

    def get_storm_dashboard(self, user, days=30):
        """Get the storm dashboard of any player as JSON

        :param str user: User to query their storm dashboard data
        :param Optional[int] days: Number of days of history to return (set to zero for only highscores)
        :return: A dictionary with the storm dashboard data of the user
        :rtype: dict
        """
        endpoint = "api/storm/dashboard/{username}"
        path = endpoint.format(username=user)
        payload = {"days": days, }
        return self.request(path=endpoint, payload=payload)

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

