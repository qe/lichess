

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

To determine whether or nor you need to generate a personal access token, check
the `Lichess API Documentation <https://lichess.org/api>`_ if the endpoint your interested in using has a OAuth2 badge.

Here is an example of using lichess_ **with** an personal access token:
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

