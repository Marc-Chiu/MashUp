import data.restaurants as restrnts


def test_get_restaurants():
    restaurants = restrnts.get_restaurants()
    assert isinstance(restaurants, dict)
    assert len(restaurants) > 0 # at least one user!
    for key in restaurants:
        assert isinstance(key,str)
        assert len(key) >= restrnts.MIN_RESTAURANT_NAME_LEN
        restaurant = restaurants[key]
        assert isinstance(restaurant, dict)
        assert restrnts.RATING in restaurant
        assert isinstance(restaurant[restrnts.RATING], int)
