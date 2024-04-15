"""
This module interfaces to our groups data
"""
import random
from data import users as usrs
from data import restaurants as rstrnts
import data.db_connect as dbc

ID_LEN = 24
BIG_NUM = 100_000_000_000_000_000_000
MIN_Group_NAME_LEN = 2

MOCK_ID = '0' * ID_LEN

NAME = "Name"
MEMBERS = "Members"
RESTAURANTS = "Restaurants"
PASSWORD = "Password"

GROUPS_COLLECT = 'groups'
GROUP_NAME = 'group_name'
TEST_RESTAURANT = "Domino's"
TEST_MEMBER = usrs.TEST_USER


"""
 Our Contract:
     - Returns a dictionary of groups keyed on group name (a str).
     - Each user name must be the key for a dictionary.
     - Each group must have a list of memembers
     - Each group must have a list of liked restaurants
"""

# get groups gets all the groups information and is connected to the endpoint


def get_groups() -> dict:
    dbc.connect_db()
    return dbc.fetch_all_as_dict(GROUP_NAME, GROUPS_COLLECT)


def exists(name: str) -> bool:
    dbc.connect_db()
    return dbc.fetch_one(GROUPS_COLLECT, {GROUP_NAME: name})


def add_group(group_name: str, owner: str, password: str, restaurant: list):
    if exists(group_name):
        raise ValueError(f'Sorry {group_name} is already taken')
    if not group_name:
        raise ValueError('Group name cannot be empty')

    group = {}
    group[GROUP_NAME] = group_name
    group[MEMBERS] = [owner]
    group[PASSWORD] = password
    group[RESTAURANTS] = restaurant
    # group[RESTAURANTS] = []
    dbc.connect_db()
    _id = dbc.insert_one(GROUPS_COLLECT, group)
    return _id is not None


def del_group(group_name: str):
    if exists(group_name):
        return dbc.del_one(GROUPS_COLLECT, {GROUP_NAME: group_name})
    else:
        raise ValueError(f'Delete failure: {group_name} not in database.')


def add_member(group_name: str, user: str, password: str):
    groups = get_groups()
    print(f'{groups=}')
    if group_name in groups:
        if usrs.exists(user):
            if password ==groups[group_name][PASSWORD]:
                groups[group_name][MEMBERS].append(user)
                dbc.connect_db()
                return dbc.update_doc(GROUPS_COLLECT, {GROUP_NAME: group_name},
                                  {MEMBERS: groups[group_name][MEMBERS]})
            else:
                raise ValueError(f'Password is incorrect')
        else:
            raise ValueError(f'User {user} does not exist')
    else:
        raise ValueError(f'Group {group_name} does not exist')


def add_restaurant(group_name: str, restaurant: str):
    group = get_group(group_name)
    if restaurant in group[RESTAURANTS]:
        raise ValueError(f'{restaurant} has already been added')
    if rstrnts.exists(restaurant):
        group[RESTAURANTS].append(restaurant)
        dbc.connect_db()
        return dbc.update_doc(GROUPS_COLLECT, {GROUP_NAME: group_name},
                                  {RESTAURANTS: group[RESTAURANTS]})
    else:
        raise ValueError(f'{restaurant} does not exist')


def remove_restaurant(group_name: str, restaurant: str):
    groups = get_groups()
    print("deleting restaurant")
    if group_name in groups:
        if restaurant in groups[group_name][RESTAURANTS]:
            groups[group_name][RESTAURANTS].remove(restaurant)
            dbc.connect_db()
            dbc.update_doc(GROUPS_COLLECT, {GROUP_NAME: group_name},
                           {RESTAURANTS: groups[group_name][RESTAURANTS]})
        else:
            raise ValueError(f'{restaurant} is not in {group_name}')
    else:
        raise ValueError(f'{group_name} does not exist')


def remove_member(group_name: str, user: str):
    groups = get_groups()
    if group_name in groups:
        if user in groups[group_name][MEMBERS]:
            groups[group_name][MEMBERS].remove(user)
            dbc.connect_db()
            dbc.update_doc(GROUPS_COLLECT, {GROUP_NAME: group_name},
                           {MEMBERS: groups[group_name][MEMBERS]})
        else:
            raise ValueError(f'{user} is not in {group_name}')
    else:
        raise ValueError(f'{group_name} does not exist')

# one group's information


def get_group(group):
    dbc.connect_db()
    ret = dbc.fetch_one(GROUPS_COLLECT, {GROUP_NAME: group})
    return ret


def get_members(group_name: str):
    group = get_group(group_name)
    if group is None:
        raise ValueError(f'{group_name} does not exist')
    return group.get(MEMBERS, [])


# def get_restaurants(group: str) -> list:
#     if group in get_groups():
#         return groups[group][RESTAURANTS]
#     else:
#         raise ValueError(f'{group} does not exist')


# def restaurant_exists(group: str, restaurant: str) -> bool:
#     if group in get_groups():
#         if restaurant in groups:
#             return restaurant in get_groups()
#     else:
#         raise ValueError(f'{group} does not exist')


# all tests
def _get_test_name():
    name = 'Test Name'
    rand_part = random.randint(0, BIG_NUM)
    return name + str(rand_part)


def _get_test_members():
    name = TEST_MEMBER
    rand_part = random.randint(0, BIG_NUM)
    return name + str(rand_part)


def _get_test_resturants():
    name = 'Test Resturant'
    rand_part = random.randint(0, BIG_NUM)
    return name + str(rand_part)


def get_test_group():
    test_group = {}
    test_group[NAME] = _get_test_name()
    test_group[MEMBERS] = _get_test_members()
    # test_group[RESTAURANTS] = _get_test_resturants()
    return test_group



def _gen_id() -> str:
    _id = random.randint(0, BIG_NUM)
    _id = str(_id)
    _id = _id.rjust(ID_LEN, '0')
    return _id


# def get_group_size(group_name: str) -> tuple:
#     if group_name in groups:
#         return len(groups[group_name])
#     else:
#         return 0


# def get_group_details(group_name: str) -> dict:
#     if exists(group_name):
#         group_details = {
#             MEMBERS: groups[group_name][MEMBERS],
#             RESTAURANTS: groups[group_name][RESTAURANTS],
#         }
#         return group_details
#     else:
#         raise ValueError(f'{group_name} does not exist')
