"""
This module interfaces to our restaraunts data
"""
import random
# from haversine import haversine
import data.db_connect as dbc


RESTAURANTS_COLLECT = 'restaurant'
NAME = 'name'
RATING = "Rating"
CUISINE = "Cuisine"
ADDRESS = "Address"
PRICE = "Price"


MIN_RESTAURANT_NAME_LEN = 2
ID_LEN = 24
BIG_NUM = 100000000000000000000
MOCK_ID = '0' * ID_LEN
MEMBERS = 'members'
MENU = 'MENU'


"""
Our Contract:
 - No arguments.
 - Returns a dictionary of restaraunts keyed on name (a str).
 - Each user name must be the key for a dictionary.
 - Each restaraunt must have a rating (int)
 """


def exists(name: str) -> bool:
    dbc.connect_db()
    return dbc.fetch_one(RESTAURANTS_COLLECT, {NAME: name})


def add_restaurant(name: str, rating: int, price: str, cuisine: str, address: str):
    if exists(name):
        raise ValueError(f'Duplicate Restaurant name: {name}')
    if not name:
        raise ValueError('Restaurant name may not be blank')
    restaurant ={}
    restaurant[NAME] = name
    restaurant[RATING] = rating
    restaurant[PRICE] = price
    restaurant[ADDRESS] = address
    restaurant[CUISINE] = cuisine
    dbc.connect_db()
    _id = dbc.insert_one(RESTAURANTS_COLLECT, restaurant)
    return _id is not None


def get_restaurants(cuisine=None):
    dbc.connect_db()
    restaurants = dbc.fetch_all_as_dict(NAME, RESTAURANTS_COLLECT)
    if cuisine is not None:
        deletes = []
        for name, restaurant in restaurants.items():
            print(f'{name}, {restaurant}')
            if restaurant[CUISINE] != cuisine:
                deletes.append(restaurant[NAME])
        for restaurant in deletes:
            del restaurants[restaurant]
    return restaurants


def get_restaurants_by_name(restaurant: str):
    if exists(restaurant):
        dbc.connect_db()
        return dbc.fetch_one(RESTAURANTS_COLLECT, {NAME: restaurant})
    else:
        raise ValueError(f'{restaurant} not found')



def get_restaurant(name):
    if exists(name):
        dbc.connect_db()
        return dbc.fetch_one(RESTAURANTS_COLLECT, name)
    else:
        raise ValueError(f'{name} not found')


def del_restaurant(name):
    if exists(name):
        dbc.connect_db()
        return dbc.del_one(RESTAURANTS_COLLECT, {NAME: name})
    else:
        raise ValueError(f'Delete failure: {name} not in database.')


# tests for endpoints
def get_test_restaurant():
    test_restaurant = {}
    test_restaurant[NAME] = _get_test_name()
    test_restaurant[RATING] = 2
    test_restaurant[PRICE] = "$$$"
    test_restaurant[CUISINE] = "Tacos"
    test_restaurant[ADDRESS] = "abc ave"
    return test_restaurant

def _get_test_name():
    name = 'test'
    rand_part = random.randint(0, BIG_NUM)
    return name + str(rand_part)
