import data.restaurants as restrnts

ADD_NAME = 'New Restaurant'
TEST_NAME = 'test name'
TEST_RATING = 3
TEST_CUISINE = "Thai"
TEST_PRICE = '$$'
TEST_ADDRESS = "123 Ave"


def test_get_restaurants():
    restaurants = restrnts.get_restaurants()
    assert isinstance(restaurants, dict)
    assert len(restaurants) > 0 # at least one user!
    for key in restaurants:
        assert isinstance(key, str)
        assert len(key) >= restrnts.MIN_RESTAURANT_NAME_LEN
        restaurant = restaurants[key]
        assert isinstance(restaurant, dict)
        assert restrnts.RATING in restaurant
        assert isinstance(restaurant[restrnts.RATING], int)
        assert restrnts.PRICE in restaurant
        assert isinstance(restaurant[restrnts.PRICE], str)
        assert restrnts.CUISINE in restaurant
        assert isinstance(restaurant[restrnts.CUISINE], str)
        assert restrnts.ADDRESS in restaurant
        assert isinstance(restaurant[restrnts.ADDRESS], str)


def test_add_restaurants():
    ret = restrnts.add_restaurant(TEST_NAME, TEST_RATING, TEST_PRICE, TEST_CUISINE, TEST_ADDRESS)
    assert restrnts.exists(TEST_NAME)
    assert ret
    restrnts.del_restaurant(TEST_NAME)
    assert not restrnts.exists(TEST_NAME)

