

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

    **This project is still in Pre-Alpha. As a result, it is still unstable and not all features have been implemented.**

Click `here <https://lichess.readthedocs.io>`_ for the full documentation for this package.

|

=======
Install
=======
You can install lichess_ on the Terminal (macOS/UNIX) or the Command Prompt (Windows) with::

    pip install lichess

Alternatively, you can use Git to clone the repository from GitHub with::

    git clone https://github.com/qe/lichess.git
    cd lichess
    pip install .

Or, if you already have it, upgrade to the latest version with::

    pip install lichess --upgrade

|

=======
Example
=======
For the full documentation, please check the `Lichess Python API Documentation <https://lichess.readthedocs.io>`_.

Some methods, such as ``Client.get_email()``, require authorization while others, such as ``Client.get_leaderboard()``,
do not require it. As a result, if you want to use a method/endpoint that does require authorization, you will need to
`generate a personal access token on Lichess <https://lichess.org/account/oauth/token>`_. If you do so, this will be your API Key.

To determine whether or nor you need to generate a personal access token, check if the endpoint you are interested in
using has a OAuth2 badge in the `Lichess API Documentation <https://lichess.org/api>`_.

Here is an example of using lichess_ **with** a personal access token:
::

    import lichess

    API_KEY = "<YOUR API KEY GOES HERE>"
    myclient = lichess.Client(token=API_KEY)

    print(myclient.get_email())

::

    {'email': 'youremailwillshowuphere@gmail.com'}


Here is an example of using lichess_ **without** a personal access token:
::

    import lichess

    myclient = lichess.Client()

    print(myclient.get_data("ismodes"))

::

    {
    "id": "ismodes",
    "username": "ismodes",
    "perfs": {
        "blitz": {"games": 90, "rating": 1599, "rd": 109, "prog": 21},
        "puzzle": {"games": 984, "rating": 2355, "rd": 132, "prog": 0, "prov": True},
        "bullet": {"games": 0, "rating": 1500, "rd": 500, "prog": 0, "prov": True},
        "correspondence": {
            "games": 0,
            "rating": 1500,
            "rd": 500,
            "prog": 0,
            "prov": True,
        },
        "classical": {"games": 0, "rating": 1500, "rd": 500, "prog": 0, "prov": True},
        "rapid": {"games": 239, "rating": 1909, "rd": 102, "prog": -79},
        "storm": {"runs": 15, "score": 24},
        "racer": {"runs": 2, "score": 32},
    },
    "createdAt": 1620502920988,
    "online": True,
    "profile": {
        "country": "AR",
        "location": "🇦🇷",
        "bio": "🇦🇷",
        "firstName": "Velez",
        "links": "🇦🇷",
    },
    "seenAt": 1647342929853,
    "playTime": {"total": 208321, "tv": 0},
    "url": "https://lichess.org/@/ismodes",
    "completionRate": 73,
    "count": {
        "all": 338,
        "rated": 329,
        "ai": 0,
        "draw": 13,
        "drawH": 13,
        "loss": 148,
        "lossH": 148,
        "win": 177,
        "winH": 177,
        "bookmark": 2,
        "playing": 0,
        "import": 0,
        "me": 0,
    },
    }



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
        Get members of a team
        ✗   get_team_members()
        Get the current live streamers
        ✓   get_live_streamers()
        Get the crosstable of two users
        ✓   get_crosstable()

    -- Relations ------------------------------------------------------------
        Get users who you are following
        ✗   following()
        Follow a player
        ✗   follow()
        Unfollow a player
        ✗   unfollow()

    -- Games ----------------------------------------------------------------
        Download a game by ID as PGN or JSON
        ~   export_by_id()
        Download the ongoing game of a user in either JSON or PGN format
        ~   export_ongoing_by_user()
        Download all games of a user as PGN or NDJSON
        ~   export_by_user()
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
        ~   get_games_channel()

    -- Puzzles --------------------------------------------------------------
        Get the daily puzzle as JSON
        ✓   get_daily_puzzle()
        Get your puzzle activity as NDJSON
        ✗   get_puzzle_activity()
        Get your puzzle dashboard as JSON
        ✓   get_puzzle_dashboard()
        Get the storm dashboard of any player as JSON
        ✓   get_storm_dashboard()

    -- Teams ----------------------------------------------------------------
        Get all swiss tournaments of a team
        ~   get_team_swiss()
        Get info about a team
        ✓   get_team_info()
        Get popular teams
        ✓   get_popular_teams()
        Get all the teams a player is a member of
        ✓   get_teams_player()
        Get search results for keyword in team search
        ✓   search_teams()
        Get members of a team
        ~   get_team_members()
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

    -- Swiss Tournaments ----------------------------------------------------
        .
        .
        .
        Get info about a Swiss tournament
        ✓   get_swiss_info()
        .
        .
        .

    -- Simuls ---------------------------------------------------------------
        Get recently finished, ongoing, and upcoming simuls
        ✓   get_simuls()

    -- Studies --------------------------------------------------------------
    -- Messaging ------------------------------------------------------------
    -- Broadcasts -----------------------------------------------------------
    -- Analysis -------------------------------------------------------------
    -- Opening Explorer -----------------------------------------------------
    -- Tablebase ------------------------------------------------------------
    -- OAuth ----------------------------------------------------------------

``~ json.decoder.JSONDecodeError: Expecting value: line 1 column 2 (char 1)``
happens when browser prompts actual file download

High likelihood this error relates with NDJSONs

|

========
Warnings
========

    **Make sure your inputs are valid.**

There is basic error handling for some invalid inputs, but there are exceptions.


Firstly, there are many types of invalid inputs. Here is an example:

- Usernames that don't exist
    - Valid username, but no user has taken it
    - Invalid username

lichess_ does basic error handling with invalid inputs (using Regex), but it does not
account for valid inputs that do not exist. Here is a more explicit example:

``"jzq0wUnCYR"`` is a valid username (i.e. it can be registered), but at the time of writing this,
there is no user by this name. As a result, the following code does not return everything:
::

    import lichess

    myclient = lichess.Client()

    print(myclient.get_status("jzq0wUnCYR", "penguingim1"))

::

    [{'name': 'penguingim1', 'title': 'GM', 'patron': True, 'id': 'penguingim1'}]


Conversely, ``"jzq0 wUnCYR"`` is an invalid username, since it has invalid characters (note the whitespace!)
However, lichess_ does catch this error, as seen below:
::

    import lichess

    myclient = lichess.Client()

    print(myclient.get_status("jzq0 wUnCYR", "penguingim1"))

::

    Traceback (most recent call last):
      File "main.py", line 109, in <module>
        main()
      File "main.py", line 76, in main
        print(myclient.get_status("jzq0 wUnCYR", "penguingim1"))
      raise ArgumentValueError("One or more usernames are invalid.")
    lichess.exceptions.ArgumentValueError: One or more usernames are invalid.

It is your responsibility to make sure your inputs are valid, but lichess_ tries its best to catch errors <3

|

=====
Links
=====
- `Lichess Python API Documentation <https://lichess.readthedocs.io>`_
- `Lichess API Documentation <https://lichess.org/api>`_
- `Lichess Website <https://lichess.org>`_

|

=======
Contact
=======
Email me at

    **helloemailmerighthere [at] gmail [dot] com**


.. _lichess: https://pypi.org/project/lichess/

