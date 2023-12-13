import data.users as usrs
import pytest

TEST_USER = "Test User"
TEST_PASSWORD = "Test Password"


@pytest.fixture(scope='function')
def temp_user():
    ret = usrs.register_user(TEST_USER, TEST_PASSWORD)
    yield TEST_USER
    if usrs.exists(TEST_USER):
        usrs.del_user(TEST_USER)


# @pytest.mark.skip("working, but github actions not yet connected to mongo")
def test_get_users(temp_user):
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
    assert usrs.exists(temp_user)

# @pytest.mark.skip("working, github actions not connected")
def test_register_user():
    test_username = "testuser"
    test_password = "testpassword123"
    assert len(test_username) >= usrs.MIN_USER_NAME_LEN
    usrs.register_user(test_username, test_password)

    users = usrs.get_users()
    assert usrs.exists(test_username)
    assert isinstance(users[test_username], dict)
    assert users[test_username][usrs.PASSWORD]==test_password

    usrs.del_user(test_username)


#@pytest.mark.skip("skip till we can update mogno")
def test_change_password(temp_user):
    name = temp_user
    new_password = 'new_test_password'
    result = usrs.change_password(TEST_USER, TEST_PASSWORD, new_password)
    user = usrs.get_users()[TEST_USER]
    password = user[usrs.PASSWORD]
    assert(password == new_password)
    #assert(result)
    usrs.del_user(name)


# @pytest.mark.skip("working, github actions not yet connected")
def test_del_user(temp_user):
    # test_username = "testuser_for_removal"
    # test_password = "testpassword"
    # usrs.register_user(test_username, test_password)

    name = temp_user
    # assert test_username in usrs.get_users()
    usrs.del_user(name)
    assert not usrs.exists(name)


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