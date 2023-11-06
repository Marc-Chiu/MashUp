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
    # Start with a clean users dictionary
    users.clear()

    username = "testuser"
    password = "password123"

    # Test successful registration
    result = register_user(username, password)
    assert result == "Registration successful for " + username
    assert username in users
    assert users[username] == hashlib.sha256(password.encode()).hexdigest()

    # Test registration with existing username
    result = register_user(username, password)
    assert result == "Username already exists. Please choose a different one."
    assert users[username] == hashlib.sha256(password.encode()).hexdigest()  # Ensure no duplicate entry was created