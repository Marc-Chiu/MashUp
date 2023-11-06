import data.users as usrs
import pytest


def test_get_users():
    users = usrs.get_users()
    assert isinstance(users, dict)
    assert len(users) > 0 # at least one user!
    for key in users:
        assert isinstance(key,str)
        assert len(key) >= usrs.MIN_USER_NAME_LEN
        user = users[key]
        assert isinstance(user, dict)
        assert usrs.LEVEL in user
        assert isinstance(user[usrs.LEVEL], int)

# Test function for register_user
def test_register_user():
    new_username = "NewUser"
    new_password = "securepassword123"

    users_before_registration = usrs.get_users()
    assert new_username not in users_before_registration
    usrs.register_user(new_username, new_password)
    users_after_registration = usrs.get_users()
    assert new_username in users_after_registration
    hashed_password = users_after_registration[new_username]
    assert isinstance(hashed_password, str)
    assert len(hashed_password) > 0