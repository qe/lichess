

.. image:: https://raw.githubusercontent.com/qe/lichess/main/docs/lichess.png
   :target: https://lichess.org
   :width: 160
   :alt: Logo

=============================================
lichess: a Python wrapper for the Lichess API
=============================================

.. image:: https://img.shields.io/pypi/l/lichess?label=license
   :alt: License

.. image:: https://img.shields.io/pypi/v/lichess
   :target: https://pypi.org/project/lichess
   :alt: PyPI

.. image:: https://img.shields.io/github/repo-size/qe/lichess?label=repo-size
   :target: https://github.com/qe/lichess
   :alt: GitHub Repo Size

.. image:: https://img.shields.io/github/languages/code-size/qe/lichess?label=code-size
   :target: https://github.com/qe/lichess
   :alt: GitHub Code Size (bytes)

.. image:: https://img.shields.io/tokei/lines/github/qe/lichess?label=lines-of-code
   :target: https://github.com/qe/lichess
   :alt: Total Lines of Code

lichess_ is a Python library for interacting with the `Lichess API <https://lichess.org/api>`_ and can be used to get profile data, game data, and much more.

    **This project is still in Pre-Alpha. As a result, it is still unstable, and not all features have been implemented.**


|

============
Installation
============
You can install lichess_ on the Terminal (macOS/UNIX) or the Command Prompt (Windows) with::

    pip install lichess

Alternatively, you can use Git to clone the repository from GitHub with::

    git clone https://github.com/qe/lichess.git
    cd lichess
    pip install .

Or, if you already have it, upgrade to the latest version with::

    pip install lichess -U

|

=====
Usage
=====

For the full documentation, please check the `Lichess Python API Documentation <https://lichess-api.readthedocs.io>`_.

Some methods, such as ``Client.get_email()``, require authorization while others, such as ``Client.get_leaderboard()``,
do not require it. As a result, if you want to use a method/endpoint that does require authorization, you will need to
`generate a personal access token on Lichess <https://lichess.org/account/oauth/token>`_. If you do so, this will be your API Key.

To determine whether or nor you need to generate a personal access token, check if the endpoint you are interested in
using has a OAuth2 badge in the `Lichess API Documentation <https://lichess.org/api>`_.

Here is an example of using lichess_ **without** a personal access token:
::

    import lichess

    myclient = lichess.Client()


Here is an example of using lichess_ **with** a personal access token:
::

    import lichess

    API_KEY = "<YOUR API KEY GOES HERE>"
    myclient = lichess.Client(token=API_KEY)


|

==============
Quick Examples
==============

The following are some examples of popular uses of this package:

|

Get the profile data of a user

::

    myclient = lichess.Client()

    user = myclient.get_data("bmartin")


Get the rating history of a user

::
    myclient = lichess.Client()

    history = myclient.get_rating_history("agadmator")


Get the list of users that are offline, online, and playing

::

    myclient = lichess.Client()

    users = ["Oliver_Penrose", "bmartin", "ismodes", "penguingim1", "Zhigalko_Sergei"]
    data = myclient.get_status(users)

    offline = [i['name'] for i in data if 'online' not in i.keys()]
    online = [i['name'] for i in data if 'online' in i.keys()]
    playing = [i['name'] for i in data if 'playing' in i.keys()]


Download all the games of a user

::

    myclient = lichess.Client()

    games = myclient.export_by_user(<USERNAME GOES HERE>)

    with open("games.pgn", "w") as f:
        f.write(games)
    f.close()


Get the list of all the members of a team

::

    API_KEY = "<YOUR API KEY GOES HERE>"
    myclient = lichess.Client(token=API_KEY)

    members = myclient.get_team_members(<TEAMNAME GOES HERE>)


Get the list of all the IDs of the puzzles you have failed

::

    API_KEY = "<YOUR API KEY GOES HERE>"
    myclient = lichess.Client(token=API_KEY)

    activity = myclient.get_puzzle_activity()
    failed = [i['id'] for i in activity if not i['win']]

|

For more examples, check the examples directory in the source code.

|

=========
Endpoints
=========
At the moment, here are the available methods for some of the Lichess API endpoints.
Below, the methods with the ``✓`` symbol are working.

::

    -- Account --------------------------------------------------------------
        Get your public profile information
        ✓   get_profile()
        Get your email address
        ✓   get_email()
        Get your preferences
        ✓   get_preferences()
        Get your kid mode status
        ✓   get_kid_mode()
        Set your kid mode status
        ✗   set_kid_mode()

    -- Users ----------------------------------------------------------------
        Get real-time status of one or more users
        ✓   get_status()
        Get the top 10 players for each speed and variant
        ✗   get_top_ten()
        Get leaderboard of an individual speed or variant
        ✗   get_leaderboard()
        Get public data of an individual user
        ✓   get_data()
        Get rating history of an individual user
        ✓   get_rating_history()
        Get performance statistics of an individual user
        ✓   get_stats()
        Get the activity feed of an individual user
        ✓   get_activity()
        Get users by ID
        ✗   get_by_id()
        Get the current live streamers
        ✓   get_live_streamers()
        Get the crosstable of two users
        ✓   get_crosstable()

    -- Relations ------------------------------------------------------------
        Get users who you are following
        ✓   following()
        Follow a player
        ✗   follow()
        Unfollow a player
        ✗   unfollow()

    -- Games ----------------------------------------------------------------
        Download a game by ID as PGN or JSON
        ✓   export_by_id()
        Download the ongoing game of a user in either JSON or PGN format
        ✓   export_ongoing_by_user()
        Download all games of a user as PGN or NDJSON
        ✓   export_by_user()
        Download games by IDs as PGN or NDJSON
        ✗   export_by_ids()
        Stream the games played between users
        ✗   stream_among_users()
        Get your ongoing games
        ✓   get_ongoing()
        Stream the moves/positions of any ongoing game
        ✗   stream_moves()
        Upload a PGN game
        ✗   import_by_pgn()

    -- TV -------------------------------------------------------------------
        Get the best games currently being played for each speed/variant
        ✓   get_games_channels()
        Stream positions and moves of the current TV game
        ✗   stream_tv_game()
        Get the best games currently being played for a specific speed/variant
        ✓   get_games_channel()

    -- Puzzles --------------------------------------------------------------
        Get the daily puzzle as JSON
        ✓   get_daily_puzzle()
        Get your puzzle activity as NDJSON
        ✓   get_puzzle_activity()
        Get your puzzle dashboard as JSON
        ✓   get_puzzle_dashboard()
        Get the storm dashboard of any player as JSON
        ✓   get_storm_dashboard()

    -- Teams ----------------------------------------------------------------
        Get all swiss tournaments of a team
        ✓   get_team_swiss()
        Get info about a team
        ✓   get_team_info()
        Get popular teams
        ✓   get_popular_teams()
        Get all the teams a player is a member of
        ✓   get_teams_player()
        Get search results for keyword in team search
        ✓   search_teams()
        Get members of a team
        ✓   get_team_members()
        .
        .
        .
        Get join requests
        ✗   get_join_requests()
        .
        .
        .

    -- Board ----------------------------------------------------------------
    -- Bot ------------------------------------------------------------------
    -- Challenges -----------------------------------------------------------
    -- Bulk pairings --------------------------------------------------------
    -- Arena tournaments ----------------------------------------------------
        Get recently finished, ongoing, and upcoming tournaments
        ✓   get_arena_all()
        .
        .
        .
        Get info about an Arena tournament
        ✓   get_arena_info()
        .
        .
        .
        Export games of an Arena tournament
        ✓   export_arena_games()
        Get results of an Arena tournament
        ✓   get_arena_results()
        Get team standing of a team battle
        ✓   get_teambattle_info()
        Get tournaments created by a user
        ✓   get_arena_createdby()

    -- Swiss Tournaments ----------------------------------------------------
        .
        .
        .
        Get info about a Swiss tournament
        ✓   get_swiss_info()
        .
        .
        .
        Export the TRF of a Swiss tournament
        ✓   export_swiss_info()
        Export games of a Swiss tournament
        ✓   export_swiss_games()
        Get results of a Swiss tournament
        ✓   get_swiss_results()

    -- Simuls ---------------------------------------------------------------
        Get recently finished, ongoing, and upcoming simuls
        ✓   get_simuls()

    -- Studies --------------------------------------------------------------
        Export one study chapter
        ✓   export_chapter()
        Export all the chapters of a study
        ✓   export_chapters()
        Export all studies of a user
        ✓   export_studies()

    -- Messaging ------------------------------------------------------------
    -- Broadcasts -----------------------------------------------------------
    -- Analysis -------------------------------------------------------------
    -- Opening Explorer -----------------------------------------------------
    -- Tablebase ------------------------------------------------------------
    -- OAuth ----------------------------------------------------------------

|

=====
Links
=====
- `Lichess Python API Documentation <https://lichess-api.readthedocs.io>`_
- `Lichess API Documentation <https://lichess.org/api>`_
- `Lichess Website <https://lichess.org>`_


.. _lichess: https://pypi.org/project/lichess/

