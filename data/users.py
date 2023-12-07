"""
This module interfaces to our user data
"""

# import smtplib
# import re
# import string
# import hashlib
import data.db_connect as dbc


MIN_USER_NAME_LEN = 2
MIN_PASSWORD_LEN = 8
TEST_USER = 'test'
USERNAME = 'username'
PASSWORD = 'password'
OLD_PASSWORD = 'old password'
USERS_COLLECT = "users"


# Basic CRUD Operations

def exists(name: str) -> bool:
    dbc.connect_db()
    return dbc.fetch_one(USERS_COLLECT, {USERNAME: name})


def register_user(username, password):
    if exists(username):
        raise ValueError("Username already exists. Please choose a different one.")
    else:
        # hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = {}
        user[USERNAME] = username
        user[PASSWORD] = password
        dbc.connect_db()
        _id = dbc.insert_one(USERS_COLLECT, user)
        return _id is not None


def get_user(username):
    if exists(username):
        dbc.connect_db()
        return dbc.fetch_one(USERS_COLLECT, username)
    else:
        raise ValueError(f'{username} not found')


def get_users():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(USERNAME, USERS_COLLECT)


def del_user(username):
    if exists(username):
        dbc.connect_db()
        return dbc.del_one(USERS_COLLECT, {USERNAME: username})
    else:
        raise ValueError(f'Delete failure: {username} not in database.')


# no way to update as of now that I know of.
def change_password(username, old_password, new_password):
    if exists(username):
        dbc.connect_db()
        users = dbc.fetch_all_as_dict(USERNAME, USERS_COLLECT)
        user = users[username]
        if user[PASSWORD] == old_password:
            user[PASSWORD] = new_password
            return True
        else:
            raise ValueError(f'{old_password} does not match password')
    else:
        raise ValueError(f'{username} does not exists')


