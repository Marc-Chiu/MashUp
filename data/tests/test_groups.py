import data.groups as grps
import pytest

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


def test_get_groups():
     groups = grps.get_groups()
     assert isinstance(groups, dict)
     assert len(groups) > 0
     for key in groups:
         group = groups[key]
         assert isinstance(key, str)
         assert isinstance(group, dict)
         assert isinstance(group[grps.MEMBERS], list)
         assert isinstance(group[grps.RESTAURANTS], list)


def test_add_group_dup_name():
    with pytest.raises(ValueError):
        grps.add_group(grps.TEST_GROUP_NAME, grps.TEST_OWNER_NAME)


def test_add_group_blank_name():
    with pytest.raises(ValueError):
        grps.add_group('', 'owner')

ADD_NAME = 'New Group'


def test_add_group():
    ret = grps.add_group(ADD_NAME, "owner")
    assert grps.exists(ADD_NAME)
    assert isinstance(ret, str)
