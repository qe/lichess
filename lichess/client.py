from .enums import *
from .utils import *
from .exceptions import *
import logging
import requests
import urllib


logger = logging.getLogger(__name__)
VALID_PERF_TYPES = [_.value for _ in PerfType]


class Client:
    def __init__(self, token=None):
        self.url = "https://lichess.org/"
        self.s = requests.Session()
        if token:
            self.token = token

    # post_data
    def request(self, path, payload=None, oauth=False, **kwargs):
        parsed_url = urllib.parse.urljoin(self.url, path)

        try:
            if oauth:
                # print("OAUTH status:", oauth)
                try:
                    response = self.s.get(parsed_url, headers={"Authorization": f"Bearer {self.token}"}, params=payload)
                except AttributeError:
                    raise APIKeyError("Missing API key. Generate one at: https://lichess.org/account/oauth/token")
                # print("hitting this URL:", response.url)
            else:
                response = self.s.get(parsed_url, params=payload)
                # print("hitting this URL:", response.url)
        except requests.exceptions.RequestException as err:
            logger.error(err)
            raise

        # print(response.content)
        # print(response.text)
        # print("response.status_code", response.status_code)

        if response.status_code == 200:
            if kwargs.get("parse"):
                return str(response.text)
            elif kwargs.get("ndjson"):
                return ndjson(response)
            # print(type(response.json()))
            return response.json()
        elif response.status_code == 401:
            raise APIKeyError(
                "Invalid or expired API key. Generate a new one at: https://lichess.org/account/oauth/token")
        else:
            raise ResponseError(response.status_code)

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

    def get_status(self, users, with_game_ids=False):
        """Get real-time status of one or more users

        :param list[str] users: Users to query their real-time status
        :param Optional[bool] with_game_ids: Flag to include the ID of games being played, if any, for each player
        :return: A list with dictionaries containing the real-time status of one or more users
        :rtype: list
        """
        invalid_inputs = [usr for usr in users if not valid_input(usr)]
        if invalid_inputs:
            logger.warning("One or more usernames are invalid.")

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
    #         logger.warning("")
    #     if (num_users <= 0) or (200 < num_users):
    #         raise ArgumentValueError("Value of num_users is invalid. Valid range includes any integer from 1 to 200")
    #         logger.warning("")
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
            logger.warning("Value of user is invalid.")

        endpoint = "api/user/{username}"
        path = endpoint.format(username=user)
        return self.request(path=path)

    def get_rating_history(self, user):
        """Get rating history of an individual user

        :param str user: User to query their public data
        :return: A list with dictionaries containing the rating history of the user
        :rtype: list
        """
        if not valid_input(user):
            logger.warning("Value of user is invalid.")

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
            logger.warning("Value of user is invalid.")
        if perf_type not in VALID_PERF_TYPES:
            logger.warning("Value of perf_type is invalid.")

        endpoint = "api/user/{username}/perf/{perf}"
        path = endpoint.format(username=user, perf=perf_type)
        return self.request(path=path)

    def get_activity(self, user):
        """Get the activity feed of an individual user

        :param str user: User to query their activity feed
        :return: A list with dictionaries containing the activity feed of the user
        :rtype: list
        """
        if not valid_input(user):
            logger.warning("Value of user is invalid.")

        endpoint = "api/user/{username}/activity"
        path = endpoint.format(username=user)
        return self.request(path=path)

    """
    POST
    """
    # def get_by_id(self):
    #     """Get users by ID
    #
    #     :return:
    #     :rtype:
    #     """
    #     endpoint = "api/users"
    #     pass

    def get_live_streamers(self):
        """Get the current live streamers

        :return: A list with dictionaries containing the current live streamers
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

    def following(self):
        """Get users who you are following

        :return: A list with dictionaries containing the information of users you are following
        :rtype: list
        """
        endpoint = "api/rel/following"
        return self.request(path=endpoint, oauth=True, ndjson=True)

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

    def export_by_id(self, game_id, moves=True, pgn_in_json=False, tags=True, clocks=True, evals=True, opening=True, literate=False, players=None):
        """Export an individual game

        :param str game_id: ID of game to export
        :param Optional[bool] moves: Whether to include the PGN moves
        :param Optional[bool] pgn_in_json: Whether to include the full PGN within the JSON response
        :param Optional[bool] tags: Whether to include the PGN tags
        :param Optional[bool] clocks: Whether to include clock comments, whenever available, in the PGN moves
        :param Optional[bool] evals: Whether to include analysis evaluation comments, whenever available, in the PGN
        :param Optional[bool] opening: Whether to include the opening name
        :param Optional[bool] literate: Whether to include textual annotations in the PGN about the opening, analysis variations, mistakes, and game termination
        :param Optional[str] players: A URL of a text file containing real names and ratings to replace Lichess usernames and ratings in the PGN
        :return: A string with PGN data of an individual game
        :rtype: str
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
        return self.request(path=path, payload=payload, parse=True, game_id=game_id)

    def export_ongoing_by_user(self, user, moves=True, pgn_in_json=False, tags=True, clocks=True, evals=True, opening=True, literate=False, players=None):
        """Export the ongoing game of a user

        :param str user: User whose ongoing game you want to export
        :param Optional[bool] moves: Whether to include the PGN moves
        :param Optional[bool] pgn_in_json: Whether to include the full PGN within the JSON response
        :param Optional[bool] tags: Whether to include the PGN tags
        :param Optional[bool] clocks: Whether to include clock comments, whenever available, in the PGN moves
        :param Optional[bool] evals: Whether to include analysis evaluation comments, whenever available, in the PGN
        :param Optional[bool] opening: Whether to include the opening name
        :param Optional[bool] literate: Whether to include textual annotations in the PGN about the opening, analysis variations, mistakes, and game termination
        :param Optional[str] players: A URL of a text file containing real names and ratings to replace Lichess usernames and ratings in the PGN
        :return: A string with PGN data of the user's ongoing game
        :rtype: str
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
        return self.request(path=path, payload=payload, parse=True)

    def export_by_user(self, user, since=None, until=None, max_games=None, vs=None, rated=None, perf_type=None, color=None, analyzed=None, moves=True, pgn_in_json=False, tags=True, clocks=True, evals=True, opening=True, ongoing=False, finished=True, players=None, sort="dateDesc"):
        """Export all the games of a user

        :param str user: User whose games you want to export
        :param Optional[int] since: Filters for games played since this timestamp (default is account creation date)
        :param Optional[int] until: Filters for games played until this timestamp (default is now)
        :param Optional[int] max_games: How many games to download (default downloads all games)
        :param Optional[str] vs: Filter for games that are only played against this specific opponent 
        :param Optional[bool] rated: Filter for games that are only rated (True) or only casual (False)
        :param Optional[str] perf_type: Filter for games that have a specific speed or variant
        :param Optional[str] color: Filters for games only played as a specific color ("white" or "black")
        :param Optional[bool] analyzed: Whether to filter for games that have a computer analysis available
        :param Optional[bool] moves: Whether to include the PGN moves
        :param Optional[bool] pgn_in_json: Whether to include the full PGN within the JSON response
        :param Optional[bool] tags: Whether to include the PGN tags
        :param Optional[bool] clocks: Whether to include clock comments, whenever available, in the PGN moves
        :param Optional[bool] evals: Whether to include analysis evaluation comments, whenever available, in the PGN
        :param Optional[bool] opening: Whether to include the opening name
        :param Optional[bool] ongoing: Whether to include ongoing games (last 3 moves will be omitted)
        :param Optional[bool] finished: Whether to only include finished games (False to only get ongoing games)
        :param Optional[str] players: A URL of a text file containing real names and ratings to replace Lichess usernames and ratings in the PGN
        :param Optional[str] sort: Sort order of the games ("dateAsc" or "dateDesc")
        :return: A string with PGN data of all the user's games
        :rtype: str
        """
        endpoint = "api/games/user/{username}"
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
        return self.request(path=path, payload=payload, parse=True)

    """
    ndjson
    POST
    """
    # def export_by_ids(self):
    #     """

    #     :return:
    #     :rtype:
    #     """
    #     endpoint = "api/games/export/_ids"
    #     pass

    """
    ndjson
    POST
    """
    # def stream_among_users(self):
    #     """Stream the games played between users

    #     :return:
    #     :rtype:
    #     """
    #     endpoint = "api/stream/games-by-users"
    #     pass

    def get_ongoing(self, max_games=9):
        """Get your ongoing games (realtime and correspondence)

        :param int max_games: Max number of games to fetch
        :return: A dictionary with your ongoing games
        :rtype: dict
        """
        endpoint = "api/account/playing"
        return self.request(path=endpoint, oauth=True)

    """
    ndjson
    """
    def stream_moves(self, game_id):
        """Stream the moves/positions of any ongoing game

        :param str game_id: ID of game to stream
        :return:
        :rtype:
        """
        endpoint = "api/stream/game/{id}"
        path = endpoint.format(id=game_id)
        return self.request(path=path, ndjson=True)

    """
    POST
    """
    def import_by_pgn(self, pgn):
        """Upload a PGN game

        :param pgn:
        :return:
        :rtype:
        """
        endpoint = "api/import"
        pass

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
    # def stream_tv_game(self):
    #     """Stream positions and moves of the current TV game

    #     :return:
    #     :rtype:
    #     """
    #     endpoint = "api/tv/feed"
    #     return self.request(path=endpoint, ndjson=True)

    def get_games_channel(self, channel, num_games=10, moves=True, pgn_in_json=False, tags=True, clocks=True, opening=True):
        """Get the best games currently being played for a specific speed/variant, including computer games and bot games

        :param str channel: Name of the channel in camelCase
        :param Optional[bool] num_games: Number of games to fetch
        :param Optional[bool] moves: Whether to include the PGN moves
        :param Optional[bool] pgn_in_json: Whether to include the full PGN within the JSON response
        :param Optional[bool] tags: Whether to include the PGN tags
        :param Optional[bool] clocks: Whether to include clock comments, whenever available, in the PGN moves
        :param Optional[bool] opening: Whether to include the opening name
        :return: A string with the PGN data of the best games being played for a specific speed/variant
        :rtype: str
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
        return self.request(path=path, payload=payload, parse=True)

    # -- Puzzles --------------------------------------------------------------

    def get_daily_puzzle(self):
        """Get the daily puzzle as JSON

        :return: A dictionary with the daily puzzle
        :rtype: dict
        """
        endpoint = "api/puzzle/daily"
        return self.request(path=endpoint)

    def get_puzzle_activity(self, max_entries=None):
        """Get your puzzle activity as NDJSON

        :param Optional[int] max_entries: Number of entries to download (leave empty to download all activity)
        :return: A list with dictionaries containing all your puzzle activity
        :rtype: list
        """
        endpoint = "api/puzzle/activity"
        payload = {"max": max_entries,}
        return self.request(path=endpoint, payload=payload, oauth=True, ndjson=True)

    def get_puzzle_dashboard(self, days):
        """Get your puzzle dashboard as JSON

        :param int days: Number of days to look back when aggregating puzzle results
        :return: A dictionary with your puzzle dashboard data
        :rtype: dict
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
        return self.request(path=path, payload=payload)

    # -- Teams ----------------------------------------------------------------

    def get_team_swiss(self, team_id, max_tournaments=100):
        """Get all swiss tournaments of a team

        :param str team_id: ID of team whose info to query
        :param Optional[int] max_tournaments: Maximum tournaments to query
        :return: A list with dictionaries containing all the swiss tournaments of a team
        :rtype: list
        """
        endpoint = "api/team/{teamId}/swiss"
        path = endpoint.format(teamId=team_id)
        payload = {"max": max_tournaments, }
        return self.request(path=path, payload=payload, ndjson=True)

    def get_team_info(self, team_id):
        """Get info about a team

        :param str team_id: ID of team whose info to query
        :return: A dictionary with the team's info
        :rtype: dict
        """
        endpoint = "api/team/{teamId}"
        path = endpoint.format(teamId=team_id)
        return self.request(path=path)

    def get_popular_teams(self, page=1):
        """Get popular teams

        :param Optional[int] page: Page of most popular teams to query
        :return: A dictionary with the popular teams
        :rtype: dict
        """
        endpoint = "api/team/all"
        payload = {"page": page, }
        return self.request(path=endpoint, payload=payload)

    def get_teams_player(self, user):
        """Get all the teams a player is a member of

        :param str user: User to query their team memberships
        :return: A list with dictionaries containing the teams a player is a member of
        :rtype: list
        """
        endpoint = "api/team/of/{username}"
        path = endpoint.format(username=user)
        return self.request(path=path)

    def search_teams(self, text, page=1):
        """Get search results for keyword in team search

        :param str text: Keyword to use in team search
        :param Optional[int] page: Page of team search to query
        :return: A dictionary with the team search results
        :rtype: dict
        """
        endpoint = "api/team/search"
        payload = {
            "text": text,
            "page": page,
        }
        return self.request(path=endpoint, payload=payload)

    def get_team_members(self, team_id):
        """Get members of a team

        :param str team_id: ID of team whose members to query
        :return: A list with dictionaries containing the members of a team
        :rtype: list
        """
        endpoint = "api/team/{teamId}/users"
        path = endpoint.format(teamId=team_id)
        return self.request(path=path, ndjson=True)

    """
    400 Bad Request
    """
    def get_join_requests(self, team_id):
        """Get pending join requests of your team

        :param str team_id:
        :return:
        :rtype:
        """
        endpoint = "api/team/{teamId}/requests"
        path = endpoint.format(teamId=team_id)
        return self.request(path=path, oauth=True)

    # -- Board ----------------------------------------------------------------
    # -- Bot ------------------------------------------------------------------
    # -- Challenges -----------------------------------------------------------
    # -- Bulk pairings --------------------------------------------------------
    # -- Arena tournaments ----------------------------------------------------

    def get_arena_all(self):
        """Get recently finished, ongoing, and upcoming tournaments

        :return: A dictionary with the recently finished, ongoing, and upcoming tournaments
        :rtype: dict
        """
        endpoint = "api/tournament"
        return self.request(path=endpoint)

    def get_arena_info(self, tournament_id, page=1):
        """Get info about an Arena tournament

        :param str tournament_id: ID of Arena tournament to query
        :param Optional[int] page:
        :return: A dictionary with the info about the queried Arena tournament
        :rtype: dict
        """
        endpoint = "api/tournament/{id}"
        path = endpoint.format(id=tournament_id)
        payload = {"page": page, }
        return self.request(path=path, payload=payload)

    def export_arena_games(self, tournament_id):
        """Export games of an Arena tournament
        
        :param str tournament_id: ID of Arena tournament to query
        :return: A string with PGN data of the Arena tournament's games
        :rtype: str
        """
        endpoint = "api/tournament/{id}/games"
        path = endpoint.format(id=tournament_id)
        return self.request(path=path, parse=True)

    def get_arena_results(self, tournament_id, max_players=None):
        """Get results of an Arena tournament
        
        :param str tournament_id: ID of Arena tournament to query
        :param Optional[int] max_players: Maximum number of players to fetch
        :return: A list with dictionaries of Arena tournament players, with their score and performance, sorted by rank (best first)
        :rtype: list
        """
        endpoint = "api/tournament/{id}/results"
        path = endpoint.format(id=tournament_id)
        if max_players:
            payload = {"nb": max_players, }
            return self.request(path=path, payload=payload, ndjson=True)
        else:
            return self.request(path=path, ndjson=True)

    def get_teambattle_info(self, tournament_id):
        """Get team standing of a team battle
        
        :param str tournament_id: ID of arena tournament to query
        :return: A dictionary with the info about the queried team battle
        :rtype: dict
        """
        endpoint = "api/tournament/{id}/teams"
        path = endpoint.format(id=tournament_id)
        return self.request(path=path)
    
    def get_arena_createdby(self, user):
        """Get tournaments created by a user
        
        :param str user: User to query their created tournaments
        :return: A list with dictionaries of all the tournaments created by the user 
        :rtype: list
        """
        endpoint = "api/user/{username}/tournament/created"
        path = endpoint.format(username=user)
        return self.request(path=path, ndjson=True)

    # -- Swiss Tournaments ----------------------------------------------------

    def get_swiss_info(self, tournament_id):
        """Get info about a Swiss tournament

        :param str tournament_id: ID of Swiss tournament to query
        :return: A dictionary with the info about the queried Swiss tournament
        :rtype: dict
        """
        endpoint = "api/swiss/{id}"
        path = endpoint.format(id=tournament_id)
        return self.request(path=path)

    def export_swiss_info(self, tournament_id):
        """Export the TRF of a Swiss tournament
        
        :param str tournament_id: ID of Swiss tournament to query
        :return: A string with TRF data of the Swiss tournament
        :rtype: str
        """
        endpoint = "swiss/{id}.trf"
        path = endpoint.format(id=tournament_id)
        return self.request(path=path, parse=True)

    def export_swiss_games(self, tournament_id):
        """Export games of a Swiss tournament
        
        :param str tournament_id: ID of Swiss tournament to query
        :return: A string with PGN data of the Swiss tournament's games
        :rtype: str
        """
        endpoint = "api/swiss/{id}/games"
        path = endpoint.format(id=tournament_id)
        return self.request(path=path, parse=True)
    
    def get_swiss_results(self, tournament_id, max_players=None):
        """Get results of a Swiss tournament
        
        :param str tournament_id: ID of Swiss tournament to query
        :param Optional[int] max_players: Maximum number of players to fetch
        :return: A list with dictionaries of Swiss tournament players, with their score and performance, sorted by rank (best first)
        :rtype: list
        """
        endpoint = "api/swiss/{id}/results"
        path = endpoint.format(id=tournament_id)
        if max_players:
            payload = {"nb": max_players, }
            return self.request(path=path, payload=payload, ndjson=True)
        else:
            return self.request(path=path, ndjson=True)

    # -- Simuls ---------------------------------------------------------------

    def get_simuls(self):
        """Get recently finished, ongoing, and upcoming simuls

        :return: A dictionary with the recently finished, ongoing, and upcoming simuls
        :rtype: dict
        """
        endpoint = "api/simul"
        return self.request(path=endpoint)

    # -- Studies --------------------------------------------------------------

    def export_chapter(self, study_id, chapter_id, clocks=True, comments=True, variations=True):
        """Export one study chapter
        
        :param str study_id: The study ID (8 characters)
        :param str chapter_id: The chapter ID (8 characters)
        :param Optional[bool] clocks: When available, include clock comments in the PGN moves
        :param Optional[bool] comments: When available, include analysis and annotator comments in the PGN moves
        :param Optional[bool] variations: When available, include non-mainline moves
        :return: A string with PGN data of one study chapter
        :rtype: str
        """
        endpoint = "study/{studyId}/{chapterId}.pgn"
        path = endpoint.format(studyId=study_id, chapterId=chapter_id)

        payload = {
        "clocks": clocks,
        "comments": comments,
        "variations": variations,
        }
        return self.request(path=path, payload=payload, parse=True)
    
    def export_chapters(self, study_id, clocks=True, comments=True, variations=True):
        """Export all the chapters of a study
        
        :param str study_id: The study ID (8 characters)
        :param Optional[bool] clocks: When available, include clock comments in the PGN moves
        :param Optional[bool] comments: When available, include analysis and annotator comments in the PGN moves
        :param Optional[bool] variations: When available, include non-mainline moves
        :return: A string with PGN data of all the chapters of a study
        :rtype: str
        """
        endpoint = "api/study/{studyId}.pgn"
        path = endpoint.format(studyId=study_id)

        payload = {
        "clocks": clocks,
        "comments": comments,
        "variations": variations,
        }
        return self.request(path=path, payload=payload, parse=True)

    def export_studies(self, user, clocks=True, comments=True, variations=True):
        """Export all the studies of a user
        
        :param str user: The user whose studies to export
        :param Optional[bool] clocks: When available, include clock comments in the PGN moves
        :param Optional[bool] comments: When available, include analysis and annotator comments in the PGN moves
        :param Optional[bool] variations: When available, include non-mainline moves
        :return: A string with PGN data of all the studies of a user
        :rtype: str
        """

        endpoint = "study/by/{username}/export.pgn"
        path = endpoint.format(username=user)
        payload = {
        "clocks": clocks,
        "comments": comments,
        "variations": variations,
        }
        return self.request(path=path, payload=payload, oauth=True, parse=True)

    # -- Messaging ------------------------------------------------------------
    # -- Broadcasts -----------------------------------------------------------
    # -- Analysis -------------------------------------------------------------
    # -- Opening Explorer -----------------------------------------------------
    # -- Tablebase ------------------------------------------------------------
    # -- OAuth ----------------------------------------------------------------

