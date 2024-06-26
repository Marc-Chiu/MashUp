"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus

from flask import Flask, request
from flask_restx import Resource, Api, fields
from flask_cors import CORS

import werkzeug.exceptions as wz

import data.users as users
import data.groups as grps
import data.restaurants as restrnts
import data.categories as cats

app = Flask(__name__)
CORS(app)
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
USERS_BYNAME_EP = f'{USERS_EP}/byname'
ADD_USER_EP = f'{USERS_EP}/{ADD}'
DEL_USER_EP = f'{USERS_EP}/{DELETE}'
USER_MENU_EP = '/user_menu'
USER_MENU_NM = 'User Menu'
USER_ID = 'User ID'

GROUPS_EP = '/groups'
GROUPS_BYNAME_EP = f'{GROUPS_EP}/byname'
DEL_USER_GROUP_EP = f'{GROUPS_EP}/{DELETE}/user'
DEL_REST_GROUP_EP = f'{GROUPS_EP}/{DELETE}/restaurant'
DEL_GROUP_EP = f'{GROUPS_EP}/{DELETE}'
ADD_MEMBER_EP = f'{GROUPS_EP}/add_member'
ADD_RESTAURANT_EP = f'{GROUPS_EP}/add_restaurant'
GROUP_MENU_EP = '/groups_menu'
GROUP_MENU_NM = 'Group Menu'
GROUP_ID = 'Group ID'

RESTAURANTS_EP = '/restaurants'
RESTAURANTS_MENU_EP = '/restaurants_menu'
RESTAURANTS_MENU_NM = 'Restaurant Menu'
RESTAURANT_ID = 'Restaurant ID'
RESTAURANTS_BYNAME_EP = f'{RESTAURANTS_EP}/byname'
DEL_RESTAURANT_EP = f'{RESTAURANTS_EP}/{DELETE}'

CATEGORIES_EP = '/categories'
CATEGORIES_MENU_EP = '/categories_menu'
CATEGORY_ID = 'Category ID'


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
                    '1': {'url': '/endpoints', 'method': 'get',
                          'text': 'List of All Endpoints'},
                    '2': {'url': f'{GROUPS_EP}',
                          'method': 'get', 'text': 'List Groups'},
                    '3': {'url': f'{USERS_EP}',
                          'method': 'get', 'text': 'List Users'},
                    '4': {'url': f'{RESTAURANTS_EP}',
                          'method': 'get', 'text': 'List Restaurants'},
                    '5': {'url': f'{DEL_GROUP_EP}',
                          'method': 'del', 'text': 'Delete Group'},
                    '6': {'url': f'{DEL_USER_EP}',
                          'method': 'del', 'text': 'Delete User'},
                    '7': {'url': f'{DEL_RESTAURANT_EP}',
                          'method': 'del', 'text': 'Delete Restaurant'},
                    '8': {'url': f'{ADD_MEMBER_EP}',
                          'method': 'post', 'text': 'Add memeber'},
                    '9': {'url': f'{ADD_USER_EP}',
                          'method': 'post', 'text': 'Add User'},
                    '10': {'url': f'{RESTAURANTS_EP}',
                          'method': 'post', 'text': 'Add Restaurant'},
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
    users.OLD_PASSWORD: fields.String,
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


    @api.expect(user_fields)
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Acceptable')
    def put(self):
        """
        Update a user's information.
        """
        username = request.json[users.USERNAME]
        old_password = request.json[users.OLD_PASSWORD]
        new_password = request.json[users.PASSWORD]
        try:
            new_id = users.change_password(username, old_password, new_password)
            print(new_id)
            if not new_id:
                raise wz.NotFound('User not found.')
            return {"message": "User updated successfully"}
        except Exception as e:
            # Handle other exceptions as necessary
            raise wz.ServiceUnavailable(f'Error: {str(e)}')


@api.route(f'{USERS_BYNAME_EP}/<username>')
class GetUserByName(Resource):
    """
    Gets a user by name.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, username):
        """
        Gets a user by name.
        """
        try:
            user = users.get_user(username)
            return user #{username: 'Found'}
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')


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

group_fields = api.model('NewGroup', {
    grps.GROUP_NAME: fields.String,
    grps.PASSWORD: fields.String,
    grps.NAME: fields.String,
    #grps.RESTAURANTS: fields.List(cls_or_instance=fields.ClassName('Restaurant')),
})

add_restaurant_fields = api.model('NewAddRestaurant', {
    grps.GROUP_NAME: fields.String,
    grps.RESTAURANTS: fields.String,
})

@api.route(f'{DEL_REST_GROUP_EP}/<name>/<group>')
class DelRestGroup(Resource):
    """
    Deletes restaurant from the group.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def delete(self, name, group):
        """
        Deletes a restaurant from group.
        """
        try:
            grps.remove_restaurant(group, name)
            return {name: 'Deleted'}
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')


@api.route(f'{DEL_USER_GROUP_EP}/<username>/<group>')
class DelUserGroup(Resource):
    """
    Deletes a user from the group.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def delete(self, username, group):
        """
        Deletes a user from group.
        """
        try:
            grps.remove_member(group, username)
            return {username: 'Deleted'}
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')


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


@api.route(f'{ADD_MEMBER_EP}')
class AddMember(Resource):
    """
    Add a member by name
    """
    @api.expect(group_fields)
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self):
        """
        add a member to a group by name.
        """
        group = request.json[grps.GROUP_NAME]
        name = request.json[grps.NAME]
        password = request.json[grps.PASSWORD]
        try:
            if grps.add_member(group, name, password) is not None:
                return {name: 'added'}
            else:
                return {name: 'not added'}
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')


@api.route(f'{ADD_RESTAURANT_EP}')
class AddRestaurant(Resource):
    """
    Add a Restaurant by name
    """
    @api.expect(add_restaurant_fields)
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self):
        """
        add a restaurant to a group by name.
        """
        group = request.json[grps.GROUP_NAME]
        restaurant = request.json[grps.RESTAURANTS]
        try:
            if grps.add_restaurant(group, restaurant) is not None:
                return {restaurant: 'added'}
            else:
                return {restaurant: 'not added'}
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')


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
        Make a group.
        """
        print(f'{request.json=}')
        group_name = request.json[grps.GROUP_NAME]
        name = request.json[grps.NAME]
        password = request.json[grps.PASSWORD]
        #restaurants = request.json[grps.RESTAURANTS]
        try:
            new_id = grps.add_group(group_name, name, password, [])
            if new_id is None:
                raise wz.ServiceUnavailable('We have a technical problem.')
            return {GROUP_ID: new_id}
        except ValueError as e:
            raise wz.NotAcceptable(f'{str(e)}')

@api.route(f'{GROUPS_BYNAME_EP}/<groupname>')
class GetGroupByName(Resource):
    """
    Gets a Group by name.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, groupname):
        """
        Gets a Group by name.
        """
        try:
            group = grps.get_group(groupname)
            return group
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')


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
    This class supports fetching a list of all restaurants.
    """

    @api.doc(params={'cuisine': "Cuisine type"})
    def get(self):
        """
        This method returns all restaurants.
        """
        args = request.args.to_dict()
        cuisine = args.get('cuisine', None)
        return {
            TYPE: DATA,
            TITLE: 'Current RESTAURANTS',
            DATA: restrnts.get_restaurants(cuisine),
            MENU: RESTAURANTS_MENU_EP,
            RETURN: MAIN_MENU_EP
            }

    @api.expect(restaurants_field)
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'Not Acceptable')
    def post(self):
        """
        Add a restauarant.
        """

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


@api.route(f'{DEL_RESTAURANT_EP}/<name>')
class DelRestaurant(Resource):
    """
    Deletes a restaurant by name.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def delete(self, name):
        """
        Deletes a restaurant by name.
        """
        try:
            restrnts.del_restaurant(name)
            return {name: 'Deleted'}
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')

@api.route(f'{RESTAURANTS_BYNAME_EP}/<name>')
class GetRestaurantByName(Resource):
    """
    Gets a restaurant by name.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, name):
        """
        Gets a user by name.
        """
        try:
            restaurant = restrnts.get_restaurants_by_name(name)
            return restaurant #{username: 'Found'}
        except ValueError as e:
            raise wz.NotFound(f'{str(e)}')


"""
This section is for Categories
"""
categories_field = api.model('NewCategory', {
    cats.CATEGORY: fields.String,
})


@api.route(f'{CATEGORIES_EP}')
class Categories(Resource):
    """
    This class supports fetching a list of all restaurants.
    """
    def get(self):
        """
        This method returns all categories.
        """
        return {
            TYPE: DATA,
            TITLE: 'Current categories',
            DATA: cats.get_categories(),
            MENU: CATEGORIES_MENU_EP,
            RETURN: MAIN_MENU_EP
            }

    @api.expect(categories_field)
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'Not Acceptable')
    def post(self):
        """
        Add a category.
        """
        category = request.json[cats.CATEGORY]
        try:
            new_id = cats.add_category(category)
            if new_id is None:
                raise wz.ServiceUnavailable('We have a technical problem.')
            return {CATEGORY_ID: new_id}
        except ValueError as e:
            raise wz.NotAcceptable(f'{str(e)}')