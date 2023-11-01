"""
This module interfaces to our groups data
"""
import random

ID_LEN = 24
BIG_NUM = 100000000000000000000
MIN_Group_NAME_LEN = 2
MEMBERS = "Members"
RESTAURANTS = "Restaurants"


"""
 Our Contract:
     - No arguments.
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
    "Reddy": {
        MEMBERS: ["Red"],
        RESTAURANTS: ["Caine's"],
    },
}

def _get_test_members():
    name = 'Hah-Young'
    rand_part = random.randint(0, BIG_NUM)
    return name + str(rand_part)


def _get_test_resturants():
    name = 'Starbucks'
    rand_part = random.randint(0, BIG_NUM)
    return name + str(rand_part)


def get_test_group():
    test_group = {}
    test_group[MEMBERS] = _get_test_members()
    test_group[RESTAURANTS] = _get_test_resturants()
    return test_group


def get_groups():
    return groups


def add_group(group_name: str, owner: str):
    if group_name in groups:
        raise ValueError(f'Sorry {group_name} is already taken')
    if not group_name:
        raise ValueError('Group name cannot be empty')
    groups[group_name] = {
            MEMBERS: [owner],
            RESTAURANTS: []}
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


def _gen_id() -> str:
    _id = random.randint(0, BIG_NUM)
    _id = str(_id)
    _id = _id.rjust(ID_LEN, '0')
    return _id


def exists(name: str) -> bool:
    return name in get_groups()
