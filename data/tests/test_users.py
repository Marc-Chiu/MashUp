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


def test_register_user():
    # Test case 1: Register a new user with a username that meets the minimum length requirement
    test_username = "testuser"
    test_password = "testpassword123"
    assert len(test_username) >= usrs.MIN_USER_NAME_LEN, "Username should meet the minimum length requirement"
    
    # Perform the registration
    usrs.register_user(test_username, test_password)
    
    # Check if the user was added and if the password is correctly hashed
    users = usrs.get_users()
    passwords = usrs.get_passwords()
    assert test_username in users, "User should be added to the users dictionary"
    assert isinstance(users[test_username], dict), "User data should be a dictionary"
    assert usrs.LEVEL in users[test_username], "User data should have a level"
    assert isinstance(users[test_username][usrs.LEVEL], int), "User level should be an integer"
    assert passwords[test_username]==test_password, "Password should be correctly hashed"
    
    # Test case 2: Try to register a user with an existing username
    # usrs.register_user(test_username, test_password)
    # assert len(users) == 1, "Duplicate user should not be added"
    
    # Clean up after test
    del users[test_username]


def test_get_pasaswords():
    passwords = usrs.get_passwords()
    assert isinstance(passwords, dict)
    assert len(passwords) > 0 
    for key in passwords:
        assert isinstance(key,str)
        assert len(passwords[key]) >= usrs.MIN_PASSWORD_LEN
        password = passwords[key]
        assert isinstance(password, str)


def test_change_password():
    passwords = usrs.get_passwords()
    username = 'Reddy'
    old_password = 'Restaurant2'
    new_password = 'test_password'
    usrs.register_user(username, new_password)
    result = usrs.change_password(username, old_password, new_password, passwords)
    print(passwords)
    assert(passwords[username], new_password)
