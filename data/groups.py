"""
This module interfaces to our groups data
"""
import random
from data import users as usrs
# import data.db_connect as dbc

ID_LEN = 24
BIG_NUM = 100_000_000_000_000_000_000
MIN_Group_NAME_LEN = 2
MOCK_ID = '0' * ID_LEN
NAME = "Name"
MEMBERS = "Members"
RESTAURANTS = "Restaurants"
TEST_GROUP_NAME = 'Coffee Lover'
TEST_OWNER_NAME = 'Callahan'
GROUP_COLLECT = 'groups'
TEST_RESTAURANT = "Domino's"
TEST_MEMEBER = "John Doe"

"""
 Our Contract:
     - Returns a dictionary of groups keyed on group name (a str).
     - Each user name must be the key for a dictionary.
     - Each group must have a list of memembers
     - Each group must have a list of liked restaurants
"""

groups = {
    "Foodies": {
        MEMBERS: ["Marc"],
        RESTAURANTS: ["Shack Shake"],
     },
    TEST_GROUP_NAME: {
        MEMBERS: ["Red"],
        RESTAURANTS: ["Caine's"],
    },
}


def del_group(name: str):
    if exists(name):
        # dbc.del_one(GAMES_COLLECT, {NAME: name})
        del groups[name]
    else:
        raise ValueError(f'Delete failure: {name} not in database.')


def get_groups() -> dict:
    # dbc.connecet_db()
    # return dbc.fetch_all_as_dict(NAME, GROUPS_COLLECT)
    return groups


def add_group(group_name: str, owner: str):
    if exists(group_name):
        raise ValueError(f'Sorry {group_name} is already taken')
    if not group_name:
        raise ValueError('Group name cannot be empty')
    groups[group_name] = {
            MEMBERS: [owner],
            RESTAURANTS: []}
    # group = {}
    # group[group_name] = {
    #   MEMBERS: [owner],
    #   RESTAURANTS: []}
    # _id = dbc.insert_one(GROUP_COLLECT, group)
    # return _id is not None
    return _gen_id()


def add_restaurant(group_name: str, restaurant: str):
    if restaurant in groups[group_name][RESTAURANTS]:
        raise ValueError(f'{restaurant} has already been added')
    groups[group_name][RESTAURANTS].append(restaurant)
    return groups


def remove_restaurant(group_name: str, restaurant: str):
    if restaurant not in groups[group_name]:
        raise ValueError(f'{restaurant} is not in your list')
    groups[group_name][RESTAURANTS].remove(restaurant)
    return groups


def add_member(group_name: str, user: str):
    if group_name in groups:
        if user in usrs.get_users():
            groups[group_name][MEMBERS].append(user)
        else:
            raise ValueError(f'{user} does not exist')
    else:
        raise ValueError(f'{group_name} does not exist')


def remove_memember(group_name: str, user: str):
    if group_name in groups:
        if user in groups[group_name]:
            groups[group_name][MEMBERS].remove(user)
        else:
            raise ValueError(f'{user} is not in {group_name}')
    else:
        raise ValueError(f'{group_name} does not exist')


def _gen_id() -> str:
    _id = random.randint(0, BIG_NUM)
    _id = str(_id)
    _id = _id.rjust(ID_LEN, '0')
    return _id


def get_group(group):
    return group.get(MEMBERS, '')


def get_members(group_name):
    return groups[group_name][MEMBERS]


def get_restaurants(group: str) -> list:
    if group in get_groups():
        return groups[group][RESTAURANTS]
    else:
        raise ValueError(f'{group} does not exist')


def restaurant_exists(group: str, restaurant: str) -> bool:
    if group in get_groups():
        if restaurant in groups:
            return restaurant in get_groups()
    else:
        raise ValueError(f'{group} does not exist')


def exists(name: str) -> bool:
    return name in get_groups()


# all tests
def _get_test_name():
    name = 'test'
    rand_part = random.randint(0, BIG_NUM)
    return name + str(rand_part)


def _get_test_members():
    name = 'John'
    rand_part = random.randint(0, BIG_NUM)
    return name + str(rand_part)


def _get_test_resturants():
    name = 'Starbucks'
    rand_part = random.randint(0, BIG_NUM)
    return name + str(rand_part)


def get_test_group():
    test_group = {}
    test_group[NAME] = _get_test_name()
    test_group[MEMBERS] = _get_test_members()
    test_group[RESTAURANTS] = _get_test_resturants()
    return test_group

def get_group_size(group_name: str) -> dict:
    if group_name in groups:
        return len(groups[group_name])
    else:
        return 0
def get_group_details(group_name: str) -> dict:
    if exists(group_name):
        group_details = {
            MEMBERS: groups[group_name][MEMBERS],
            RESTAURANTS: groups[group_name][RESTAURANTS],
        }
        return group_details
    else:
        raise ValueError(f'{group_name} does not exist')
