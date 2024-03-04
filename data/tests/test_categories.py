import data.categories as cats
import pytest

TEST_CATEGORY = "Italian"


@pytest.fixture(scope='function')
def temp_category():
    ret = cats.add_category(TEST_CATEGORY)
    yield TEST_CATEGORY
    if cats.exists(TEST_CATEGORY):
        cats.del_category(TEST_CATEGORY)


def test_get_categories(temp_category):
    categories = cats.get_categories()
    assert isinstance(categories, dict)
    print(categories)
    print(len(categories))
    assert len(categories) > 0 # at least one category!
    for key in categories:
        assert isinstance(key,str)
        cat = categories[key]
        assert isinstance(cat, dict)
    assert cats.exists(temp_category)

