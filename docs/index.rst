
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

Introduction
------------

lichess_ is a Python library for interacting with the `Lichess API <https://lichess.org/api>`_ and can be used to get profile data, game data, and much more.

The package is open source, and its code is available on `GitHub <https://github.com/qe/lichess>`_ under the MIT license.


Installation
------------
The lichess_ Python package can be easily installed using ``pip``.

Open the ``Terminal`` (macOS/UNIX) or the ``Command Prompt`` (Windows), and do:

.. code-block:: bash

    pip install lichess


Alternatively, you can use Git to clone the repository from GitHub with:

.. code-block:: bash

    git clone https://github.com/qe/lichess.git
    cd lichess
    pip install .

Or, if you already have it, upgrade to the latest version with:

.. code-block:: bash

    pip install lichess -U


Usage
-----

Some methods, such as ``Client.get_email()``, require authorization while others, such as ``Client.get_leaderboard()``,
do not require it. As a result, if you want to use a method/endpoint that does require authorization, you will need to
`generate a personal access token on Lichess <https://lichess.org/account/oauth/token>`_.
If you do so, this will be your API Key.

To determine whether or nor you need to generate a personal access token, check if the endpoint you are interested
in using has a OAuth2 badge in the `Lichess API <https://lichess.org/api>`_.

Here is an example of using lichess_ **without** a personal access token:

.. code-block:: python

    import lichess

    myclient = lichess.Client()

Here is an example of using lichess_ **with** a personal access token:

.. code-block:: python

    import lichess

    API_KEY = "<YOUR API KEY GOES HERE>"
    myclient = lichess.Client(token=API_KEY)

Usage
-----

.. toctree::
   :caption: Lichess Python API
   :maxdepth: 2

   source/account.rst
   source/users.rst
   source/relations.rst
   source/games.rst
   source/tv.rst
   source/puzzles.rst
   source/teams.rst
   source/arena.rst
   source/swiss.rst
   source/simuls.rst
   source/studies.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _lichess: https://pypi.org/project/lichess/
