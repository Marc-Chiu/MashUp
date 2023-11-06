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

# Test function for authenticate_user
def test_authenticate_user():
    # Prepare a username and password
    username = "ExistingUser"
    correct_password = "correctpassword"
    incorrect_password = "incorrectpassword"

    # Register a new user
    usrs.register_user(username, correct_password)

    # Attempt to authenticate with correct password
    auth_result_correct = usrs.authenticate_user(username, correct_password)
    assert auth_result_correct == f"Authentication successful. Welcome, {username}"
    assert usrs.session[username] is not None  # Session should be updated

    # Attempt to authenticate with incorrect password
    auth_result_incorrect = usrs.authenticate_user(username, incorrect_password)
    assert auth_result_incorrect == "Authentication failed. Incorrect password."
    assert username not in usrs.session  # Session should not be updated for failed authentication

    # Attempt to authenticate a non-existing user
    auth_result_non_existing = usrs.authenticate_user("NonExistingUser", correct_password)
    assert auth_result_non_existing == "Authentication failed. User not found."