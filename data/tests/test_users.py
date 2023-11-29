import data.users as usrs
import pytest

@pytest.mark.skip("skip till we connect to mogno")
def test_get_users():
    users = usrs.get_users()
    assert isinstance(users, dict)
    print(users)
    print(len(users))
    assert len(users) > 0 # at least one user!
    for key in users:
        assert isinstance(key,str)
        assert len(key) >= usrs.MIN_USER_NAME_LEN
        user = users[key]
        assert isinstance(user, dict)
        assert usrs.PASSWORD in user
        assert isinstance(user[usrs.PASSWORD], str)
        assert len(user[usrs.PASSWORD]) >= usrs.MIN_PASSWORD_LEN

@pytest.mark.skip("skip till we connect to mogno")
def test_register_user():
    # Test case 1: Register a new user with a username that meets the minimum length requirement
    test_username = "testuser"
    test_password = "testpassword123"
    assert len(test_username) >= usrs.MIN_USER_NAME_LEN, "Username should meet the minimum length requirement"

    # Perform the registration
    usrs.register_user(test_username, test_password)

    # Check if the user was added and if the password is correctly hashed
    users = usrs.get_users()
    assert test_username in users, "User should be added to the users dictionary"
    assert isinstance(users[test_username], dict), "User data should be a dictionary"
    assert users[test_username][usrs.PASSWORD]==test_password, "Password should be correctly hashed"

    # Test case 2: Try to register a user with an existing username
    # usrs.register_user(test_username, test_password)
    # assert len(users) == 1, "Duplicate user should not be added"

    # Clean up after test
    usrs.del_user(test_username)

# @pytest.mark.skip("skip till we connect to mogno")
# def test_get_pasaswords():
#     passwords = usrs.get_passwords()
#     assert isinstance(passwords, dict)
#     assert len(passwords) > 0
#     for key in passwords:
#         assert isinstance(key,str)
#         assert len(passwords[key]) >= usrs.MIN_PASSWORD_LEN
#         password = passwords[key]
#         assert isinstance(password, str)

@pytest.mark.skip("skip till we connect to mogno")
def test_change_password():
    passwords = usrs.get_passwords()
    username = 'Reddy'
    old_password = 'Restaurant2'
    new_password = 'test_password'
    usrs.register_user(username, new_password)
    result = usrs.change_password(username, old_password, new_password, passwords)
    print(passwords)
    assert(passwords[username], new_password)


@pytest.mark.skip("skip till we connect to mogno")
def test_remove_user():
    test_username = "testuser_for_removal"
    test_password = "testpassword"
    usrs.register_user(test_username, test_password)

    assert test_username in usrs.get_users()
    assert usrs.remove_user(test_username) == True, "User removal should return True"
    assert test_username not in usrs.get_users()
    assert usrs.remove_user("nonexistent_user") == False, "Removing a non-existent user should return False"

@pytest.mark.skip("skip till we connect to mogno")
def test_get_user_info_valid_user():
    test_username = "Reddy"
    result = usrs.get_user_info(test_username)
    assert result == {"level": 1}


@pytest.mark.skip("skip till we connect to mogno")
def test_get_user_info_invalid_user():
    # Assuming 'testuser' is already registered
    test_username = 'testuser'
    result = usrs.get_user_info(test_username)
    assert result == "User not found."
    # user_info = usrs.get_user_info('testuser')
    # assert isinstance(user_info, dict), "User info should be returned as a dictionary."
    # assert usrs.get_user_info('nonexistentuser') == "User not found.", "Querying a non-existent user should return 'User not found.'"
    # del users[test_username]

