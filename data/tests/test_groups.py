import data.groups as grps

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

ADD_NAME = 'New Game'


def test_add_game():
    ret = grps.add_group(ADD_NAME, "owner")
    assert grps.exists(ADD_NAME)
    assert isinstance(ret, str)
