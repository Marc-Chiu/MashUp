import data.users as usrs


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

def test_get_pasaswords():
    passwords = usrs.get_passwords()
    assert isinstance(passwords, dict)
    assert len(users) > 0 
    for key in passwords:
        assert isinstance(key,str)
        assert len(key) >= usrs.MIN_PASSWORD_LEN
        password = passwords[key]
        assert isinstance(password, dict)
