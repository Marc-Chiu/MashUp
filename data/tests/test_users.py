import data.users as usrs
import pytest


# @pytest.mark.skip("working, but github actions not yet connected to mongo")
def test_get_users():
    users = usrs.get_users()
    assert isinstance(users, dict)
    print(users)
    print(len(users))
    assert len(users) > 0 # at least one user!
    for key in users:
        assert isinstance(key,str)
        # assert len(key) >= usrs.MIN_USER_NAME_LEN
        user = users[key]
        assert isinstance(user, dict)
        assert usrs.PASSWORD in user
        assert isinstance(user[usrs.PASSWORD], str)
        # assert len(user[usrs.PASSWORD]) >= usrs.MIN_PASSWORD_LEN

# @pytest.mark.skip("skip till we connect to mogno")
def test_register_user():
    test_username = "testuser"
    test_password = "testpassword123"
    assert len(test_username) >= usrs.MIN_USER_NAME_LEN
    usrs.register_user(test_username, test_password)

    users = usrs.get_users()
    assert test_username in users
    assert isinstance(users[test_username], dict)
    assert users[test_username][usrs.PASSWORD]==test_password

    usrs.del_user(test_username)


@pytest.mark.skip("skip till we can update mogno")
def test_change_password():
    passwords = usrs.get_passwords()
    username = 'Reddy'
    old_password = 'Restaurant2'
    new_password = 'test_password'
    usrs.register_user(username, new_password)
    result = usrs.change_password(username, old_password, new_password, passwords)
    print(passwords)
    assert(passwords[username], new_password)


# @pytest.mark.skip("skip till we connect to mogno")
def test_del_user():
    test_username = "testuser_for_removal"
    test_password = "testpassword"
    usrs.register_user(test_username, test_password)

    assert test_username in usrs.get_users()
    assert usrs.del_user(test_username)
    assert test_username not in usrs.get_users()


@pytest.mark.skip("don't understand this test")
def test_get_user_info_invalid_user():
    # Assuming 'testuser' is already registered
    test_username = 'testuser'
    result = usrs.get_user_info(test_username)
    assert result == "User not found."
    # user_info = usrs.get_user_info('testuser')
    # assert isinstance(user_info, dict), "User info should be returned as a dictionary."
    # assert usrs.get_user_info('nonexistentuser') == "User not found.", "Querying a non-existent user should return 'User not found.'"
    # del users[test_username]