

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

lichess_ is a Python library for interacting with the Lichess API and can be used to get profile data, game data, and much more.

    **This project is still in Pre-Alpha. As a result, it is still unstable and not all features have been implemented.**

|

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

Example
=======
For the full documentation, please check the `Lichess Python API Documentation <https://lichess.readthedocs.io>`_.

Here's a quick example of what using two of the ____ could look like::

    from lichess import get_data, get_status

    # Get public data of Eric Hansen
    response1 = get_data("chessbrahs")

    # Get real-time users status of them, and if they are playing any games, return their game IDs
    response2 = get_status("DrNykterstein", "gmwesleyso1993", "penguingim1", with_game_ids=True)


    print("RESPONSE 1")
    print(response1)
    print()
    print("RESPONSE 2")
    print(response2)
    print()
    print("Currently online:", len([usr for usr in response2 if usr.get('online')]))

::

    RESPONSE 1
    {
    "id": "chessbrahs",
    "username": "chessbrahs",
    "perfs": {
    "chess960": {"games": 19, "rating": 2425, "rd": 258, "prog": 112, "prov": True},
    "antichess": {"games": 4, "rating": 1631, "rd": 296, "prog": 0, "prov": True},
    "atomic": {"games": 3, "rating": 1601, "rd": 307, "prog": 0, "prov": True},
    "ultraBullet": {"games": 979, "rating": 2472, "rd": 103, "prog": -102},
    "blitz": {"games": 786, "rating": 2768, "rd": 89, "prog": 20},
    "kingOfTheHill": {
    "games": 4,
    "rating": 1995,
    "rd": 300,
    "prog": 0,
    "prov": True,
    },
    "crazyhouse": {
    "games": 466,
    "rating": 2244,
    "rd": 193,
    "prog": 6,
    "prov": True,
    },
    "threeCheck": {"games": 1, "rating": 1425, "rd": 370, "prog": 0, "prov": True},
    "bullet": {"games": 11652, "rating": 3030, "rd": 45, "prog": -2},
    "correspondence": {
    "games": 0,
    "rating": 1500,
    "rd": 500,
    "prog": 0,
    "prov": True,
    },
    "horde": {"games": 62, "rating": 2239, "rd": 240, "prog": 80, "prov": True},
    "puzzle": {"games": 281, "rating": 2426, "rd": 269, "prog": -13, "prov": True},
    "classical": {"games": 0, "rating": 1500, "rd": 500, "prog": 0, "prov": True},
    "rapid": {"games": 3, "rating": 2015, "rd": 286, "prog": 0, "prov": True},
    "storm": {"runs": 4, "score": 78},
    },
    "title": "GM",
    "createdAt": 1429821366542,
    "online": False,
    "profile": {
    "country": "CA",
    "bio": "Professional chess player, commentator, and streamer. Founder of ChessbrahTV and member of the Canadian Olympic team.\r\n\r\n\r\n\r\n ",
    "firstName": "Eric",
    "lastName": "Hansen",
    "fideRating": 2629,
    "uscfRating": 2670,
    "links": "https://linktr.ee/erichansen\r\n",
    },
    "seenAt": 1647084092185,
    "playTime": {"total": 1758311, "tv": 527202},
    "url": "https://lichess.org/@/chessbrahs",
    "completionRate": 100,
    "count": {
    "all": 14377,
    "rated": 13988,
    "ai": 36,
    "draw": 302,
    "drawH": 299,
    "loss": 2465,
    "lossH": 2445,
    "win": 11610,
    "winH": 11597,
    "bookmark": 1,
    "playing": 0,
    "import": 1,
    "me": 0,
    },
    }

    RESPONSE 2
    [
    {"name": "DrNykterstein", "title": "GM", "patron": True, "id": "drnykterstein"},
    {
    "name": "gmwesleyso1993",
    "title": "GM",
    "id": "gmwesleyso1993",
    "online": True,
    "playing": True,
    "playingId": "850Rfzf8",
    },
    {"name": "penguingim1", "title": "GM", "patron": True, "id": "penguingim1"},
    ]

    Currently online: 1

For more examples, check the examples directory in the source code.

|

Warnings
========
**Make sure your inputs are valid.**

For example, if you input an invalid username like::

    "chessbrahs "

It will ignore this input as shown below:

::

    from lichess import get_status

    response4 = get_status("chessbrahs ", "gmwesleyso1993")

    print(response4)



::

    [
        {
            "name": "gmwesleyso1993",
            "title": "GM",
            "id": "gmwesleyso1993",
            "online": True,
            "playing": True,
        }
    ]

As seen above, the ``"chessbrahs "`` input was ignored in lichess_' response because it is invalid (in this case, because of the invalid whitespace).
This is not limited to invalid characters since inputs that don't exist (such as, a username that does not exist) will also be ignored.

|

Links
=====
- `Lichess Python API Documentation <https://lichess.readthedocs.io>`_
- `Lichess General API Documentation <https://lichess.org/api>`_
- `Lichess Website <https://lichess.org>`_

|

Contact
=======
Email me at

    **helloemailmerighthere [at] gmail [dot] com**


.. _lichess: https://pypi.org/project/lichess/

