"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from flask_restx import Resource, Api

import data.games as gms
import data.users as users
import data.groups as grps

app = Flask(__name__)
api = Api(app)

DEFAULT = 'Default'
MENU = 'menu'
MAIN_MENU_EP = '/MainMenu'
MAIN_MENU_NM = "Welcome to Text Game!"
HELLO_EP = '/hello'
HELLO_RESP = '/hello'
GAMES_EP = '/games'
GAME_MENU_EP = '/game_menu'
GAME_MENU_NM = 'Game Menu'
# USERS = 'users'
USERS_EP = '/users'
USER_MENU_EP = '/user_menu'
USER_MENU_NM = 'User Menu'
GROUPS_EP = '/groups'
GROUP_MENU_EP = '/groups_menu'
GROUP_MENU_NM = 'Group Menu'
TYPE = 'Type'
DATA = 'Data'
TITLE = 'Title'
RETURN = 'Return'


@api.route(HELLO_EP)
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {HELLO_RESP: 'world'}


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


@api.route(f'{MAIN_MENU_EP}')
# @api.route('/')
class MainMenu(Resource):
    """
    This will deliver our main menu.
    """
    def get(self):
        """
        Gets the main game menu.
        """
        return {TITLE: MAIN_MENU_NM,
                DEFAULT: 2,
                'Choices': {
                    '1': {'url': '/', 'method': 'get',
                          'text': 'List Available Characters'},
                    '2': {'url': '/',
                          'method': 'get', 'text': 'List Active Games'},
                    '3': {'url': f'{USERS_EP}',
                          'method': 'get', 'text': 'List Users'},
                    '4': {'url': f'{USERS_EP}',
                          'method': 'get', 'text': 'Illustrating a Point!'},
                    'X': {'text': 'Exit'},
                }}


@api.route(f'{USER_MENU_EP}')
# @api.route('/')
class UserMenu(Resource):
    """
    This will deliver our user menu.
    """
    def get(self):
        """
        Gets the user menu.
        """
        return {
                    TITLE: USER_MENU_NM,
                    DEFAULT: '0',
                    'Choices': {
                        '1': {
                                'url': '/',
                                'method': 'get',
                                'text': 'Get User Details',
                        },
                        '0': {
                            'text': 'Return',
                            'url': MAIN_MENU_EP,
                        },
                    },
                }


@api.route(f'{USERS_EP}')
class Users(Resource):
    """
    This class supports fetching a list of all pets.
    """
    def get(self):
        """
        This method returns all users.
        """
        return {
            TYPE: DATA,
            TITLE: 'Current Users',
            DATA: users.get_users(),
            MENU: USER_MENU_EP,
            RETURN: MAIN_MENU_EP
        }


@api.route(f'{GAMES_EP}')
class Games(Resource):
    """
    This class supports fetching a list of all games.
    """
    def get(self):
        """
        This method returns all games.
        """
        return {
            TYPE: DATA,
            TITLE: 'Current Games',
            DATA: gms.get_users(),
            MENU: GAME_MENU_EP,
            RETURN: MAIN_MENU_EP
        }

@api.route(f'{GROUPS_EP}')
class Groups(Resource):
    """
    This class supports fetching a list of all games.
    """
    def get(self):
        """
        This method returns all games.
        """
        return {
            TYPE: DATA,
            TITLE: 'Current Groups',
            DATA: gms.get_users(),
            MENU: GAME_MENU_EP,
            RETURN: MAIN_MENU_EP
            }
