import data.groups as grps
import pytest


@pytest.fixture(scope='function')
def temp_group():
    name = grps._get_test_name()
    ret = grps.add_group(name, 0)
    yield name
    if grps.exists(name):
        grps.del_group(name)


def test_get_test_name():
    name = grps._get_test_name()
    assert isinstance(name, str)
    assert len(name) > 0


def test_get_test_members():
    members = grps._get_test_members()
    assert isinstance(members, str)
    assert len(members) > 0


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
         assert isinstance(group[grps.RESTAURANTS], list)
     assert grps.exists(temp_group)


def test_add_group_dup_name(temp_group):
    """
    Make sure a duplicate group name raises a ValueError.
    `temp_game` is the name of the game that our fixture added.
    """
    dup_group_name = temp_group
    with pytest.raises(ValueError):
        grps.add_group(temp_group, 'owner')


def test_add_group_blank_name():
    """
    Make sure a blank group name raises a ValueError.
    """
    with pytest.raises(ValueError):
        grps.add_group('', 'owner')


def test_del_group(temp_group):
    name = temp_group
    grps.del_group(name)
    assert not grps.exists(name)


def test_del_group_not_there():
    name = grps._get_test_name()
    with pytest.raises(ValueError):
        grps.del_group(name)


ADD_NAME = 'New Group'


def test_add_group():
    new_name = grps._get_test_name()
    ret = grps.add_group(new_name, 4)
    assert grps.exists(new_name)
    assert isinstance(ret, bool)
    grps.del_group(new_name)
