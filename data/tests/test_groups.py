import data.groups as grps
import pytest
from unittest.mock import patch


ADD_NAME = 'TEST NEW GROUP'
TEST_PASSWORD = 'test password'


@pytest.fixture(scope='function')
def temp_group():
    name = grps._get_test_name()
    member = grps._get_test_members()
    password = "test password"
    ret = grps.add_group(name, member, password, [])
    yield name
    if grps.exists(name):
        grps.del_group(name)


@pytest.mark.skip("skip till we connect to mogno")
def test_get_group_details():
    test_group_name = "Foodies"
    expected_details = grps.groups["Foodies"]
    actual_details = grps.get_group_details(test_group_name)
    assert actual_details == expected_details


def test_get_test_name():
    name = grps._get_test_name()
    assert isinstance(name, str)
    assert len(name) > 0


@pytest.mark.skip("skip till we connect to mogno")
def test_get_test_members():
    members = grps._get_test_members()
    assert isinstance(members, str)
    assert len(members) > 0


@pytest.mark.skip("skip till we connect to mogno")
def test_get_test_restaurants():
    restaurant = grps._get_test_resturants()
    assert isinstance(restaurant, str)
    assert len(restaurant) > 0


@pytest.mark.skip("skip till we connect to mogno")
def test_group_size():
    expected_size = grps.get_group_size("Foodies")
    assert expected_size == 2


def test_gen_id():
    _id = grps._gen_id()
    assert isinstance(_id, str)
    assert len(_id) == grps.ID_LEN


def test_get_test_group():
    assert isinstance(grps.get_test_group(), dict)


def test_get_groups(temp_group):
     groups = grps.get_groups()
     assert isinstance(groups, dict)
     assert len(groups) > 0
     for key in groups:
         group = groups[key]
         assert isinstance(key, str)
         assert isinstance(group, dict)
         assert isinstance(group[grps.MEMBERS], list)
         #assert isinstance(group[grps.RESTAURANTS], list)
     assert grps.exists(temp_group)


@pytest.mark.skip("skip till we connect to mogno")
def test_get_restaurants(temp_group):
    name = temp_group
    restaurants = grps.get_restaurants(name)
    assert isinstance(restaurants, list)
    if len(restaurants) > 0:
        for restaurant in restaurants:
            assert isinstance(restaurant, str)


def test_add_group_dup_name(temp_group):
    """
    Make sure a duplicate group name raises a ValueError.
    `temp_game` is the name of the game that our fixture added.
    """
    with pytest.raises(ValueError):
        grps.add_group(temp_group, 'test_member', TEST_PASSWORD, [])


def test_add_group_blank_name():
    """
    Make sure a blank group name raises a ValueError.
    """
    with pytest.raises(ValueError):
        grps.add_group('', 'test_member', TEST_PASSWORD, [])


def test_del_group(temp_group):
    name = temp_group
    grps.del_group(name)
    assert not grps.exists(name)

def test_del_group_not_there():
    name = grps._get_test_name()
    with pytest.raises(ValueError):
        grps.del_group(name)


def test_add_group():
    new_name = grps._get_test_name()
    new_member = grps._get_test_members()
    ret = grps.add_group(new_name, new_member, TEST_PASSWORD, [])
    assert grps.exists(new_name)
    assert isinstance(ret, bool)
    grps.del_group(new_name)


@pytest.mark.skip("skip till we connect to mogno")
def test_add_restaurant(temp_group):
    name = temp_group
    grps.add_restaurant(name, grps.TEST_RESTAURANT)
    assert grps.TEST_RESTAURANT in grps.get_restaurants(name)


@patch('data.users.exists', return_value=True)
def test_add_member(mock_exists, temp_group):
    name = temp_group
    grps.add_member(name, grps.TEST_MEMBER, TEST_PASSWORD)
    assert grps.TEST_MEMBER in grps.get_members(name)


def test_get_group(temp_group):
    ret = grps.get_group(temp_group)
    print(f'{ret=}')
    assert ret[grps.GROUP_NAME] == temp_group


def test_get_members(temp_group):
    group = grps.get_group(temp_group)
    assert group
    members = grps.get_members(temp_group)
    assert isinstance(members, list)
    for member in members:
        if member.startswith(grps.TEST_MEMBER):
            assert True
            return
    assert False


def test_get_members_group_not_there():
    with pytest.raises(ValueError):
        grps.get_members("This is not a group name!")

# if there are no members write a test that will check for an empty list