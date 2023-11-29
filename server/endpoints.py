"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus

from flask import Flask, request
from flask_restx import Resource, Api, fields

import werkzeug.exceptions as wz

import data.users as users
import data.groups as grps
import data.restaurants as restrnts

app = Flask(__name__)
api = Api(app)

DELETE = 'delete'
ADD = 'add'
DEFAULT = 'Default'

TYPE = 'Type'
DATA = 'Data'
TITLE = 'Title'
RETURN = 'Return'

MENU = 'menu'
MAIN_MENU_EP = '/MainMenu'
MAIN_MENU_NM = "Welcome to MashUp!"

USERS_EP = '/users'
ADD_USER_EP = f'{USERS_EP}/{ADD}'
DEL_USER_EP = f'{USERS_EP}/{DELETE}'
USER_MENU_EP = '/user_menu'
USER_MENU_NM = 'User Menu'
USER_ID = 'User ID'

GROUPS_EP = '/groups'
DEL_GROUP_EP = f'{GROUPS_EP}/{DELETE}'
ADD_MEMBER_EP = f'{GROUPS_EP}/{ADD}'
GROUP_MENU_EP = '/groups_menu'
GROUP_MENU_NM = 'Group Menu'
GROUP_ID = 'Group ID'

RESTAURANTS_EP = '/restaurants'
RESTAURANTS_MENU_EP = '/restaurants_menu'
RESTAURANTS_MENU_NM = 'Restaurant Menu'
RESTAURANT_ID = 'Restaurant ID'


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


user_fields = api.model('NewUser', {
    users.USERNAME: fields.String,
    users.PASSWORD: fields.String,
})


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


    @api.expect(user_fields)
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'Not Acceptable')
    def post(self):
        """
        Add a user.
        """
        username = request.json[users.USERNAME]
        password = request.json[users.PASSWORD]
        try:
            new_id = users.register_user(username, password)
            if new_id is None:
                raise wz.ServiceUnavailable('We have a technical problem.')
            return {USER_ID: new_id}
        except ValueError as e:
            raise wz.NotAcceptable(f'{str(e)}')


@api.route(f'{DEL_USER_EP}/<username>')
class DelUser(Resource):
    """
    Deletes a user by name.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def delete(self, username):
        """
        Deletes a user by name.
        """
        try:
            users.del_user(username)
            return {username: 'Deleted'}
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')



"""
This section is for Groups

"""
@api.route(f'{DEL_GROUP_EP}/<name>')
class DelGroup(Resource):
    """
    Deletes a group by name.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def delete(self, name):
        """
        Deletes a group by name.
        """
        try:
            grps.del_group(name)
            return {name: 'Deleted'}
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')


@api.route(f'{ADD_MEMBER_EP}/<group>/<name>')
class AddMember(Resource):
    """
    Add a member by name
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self, name, group):
        """
        add a member to a group by name.
        """
        try:
            grps.add_member(group, name)
            return {name: 'added'}
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')


group_fields = api.model('NewGroup', {
    grps.NAME: fields.String,
    grps.MEMBERS: fields.String,
    grps.RESTAURANTS: fields.String,
})


@api.route(f'{GROUPS_EP}')
class Groups(Resource):
    """
    This class supports fetching a list of all groups.
    """
    def get(self):
        """
        This method returns all groups.
        """
        return {
            TYPE: DATA,
            TITLE: 'Current Groups',
            DATA: grps.get_groups(),
            MENU: GROUP_MENU_EP,
            RETURN: MAIN_MENU_EP
            }

    @api.expect(group_fields)
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'Not Acceptable')
    def post(self):
        """
        Add a group.
        """
        print(f'{request.json=}')
        name = request.json[grps.NAME]
        members = request.json[grps.MEMBERS]
        resturants = request.json[grps.RESTAURANTS]
        try:
            new_id = grps.add_group(name, members)
            if new_id is None:
                raise wz.ServiceUnavailable('We have a technical problem.')
            return {GROUP_ID: new_id}
        except ValueError as e:
            raise wz.NotAcceptable(f'{str(e)}')


"""
This section is for Restaurants
"""
restaurants_field = api.model('NewRestaurant', {
    restrnts.NAME: fields.String,
    restrnts.RATING: fields.Integer,
    restrnts.PRICE: fields.String,
    restrnts.CUISINE: fields.String,
    restrnts.ADDRESS: fields.String,
})



@api.route(f'{RESTAURANTS_EP}')
class Restaurants(Resource):
    """
    This class supports fetching a list of all groups.
    """
    def get(self):
        """
        This method returns all groups.
        """
        return {
            TYPE: DATA,
            TITLE: 'Current RESTAURANTS',
            DATA: restrnts.get_restaurants(),
            MENU: RESTAURANTS_MENU_EP,
            RETURN: MAIN_MENU_EP
            }

    @api.expect(restaurants_field)
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'Not Acceptable')
    def post(self):
        """
        Add a game.
        """
        print(f'{request.json=}')
        name = request.json[restrnts.NAME]
        rating = request.json[restrnts.RATING]
        price = request.json[restrnts.PRICE]
        cuisine = request.json[restrnts.CUISINE]
        address = request.json[restrnts.ADDRESS]
        try:
            new_id = restrnts.add_restaurant(name, rating, price, cuisine, address)
            if new_id is None:
                raise wz.ServiceUnavailable('We have a technical problem.')
            return {RESTAURANT_ID: new_id}
        except ValueError as e:
            raise wz.NotAcceptable(f'{str(e)}')