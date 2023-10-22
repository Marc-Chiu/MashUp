import data.groups as grps

def test_get_groups():
     groups = grps.get_groups()
     assert isinstance(groups, dict)
     assert len(groups) > 0
     for group in groups:
         assert isinstance(group, str)
         assert isinstance(groups[group], dict)
                    
