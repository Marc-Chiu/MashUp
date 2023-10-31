import data.restaurants as restrnts
import pytest


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
        assert restrnts.PRICE in restaurant
        assert isinstance(restaurant[restrnts.PRICE], str)
        assert restrnts.CUISINE in restaurant
        assert isinstance(restaurant[restrnts.CUISINE], str)
        assert restrnts.ADDRESS in restaurant
        assert isinstance(restaurant[restrnts.ADDRESS], str)


ADD_NAME = 'New Restaurant'


def test_add_restaurants():
    rating = 4
    address = "123 blv"
    price = "$"
    cuisine = "Indian"
    ret = restrnts.add_restaurant(ADD_NAME, rating, price, cuisine, address)
    assert restrnts.exists(ADD_NAME)
    assert isinstance(ret, str)
