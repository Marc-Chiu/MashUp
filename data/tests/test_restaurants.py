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

def test_delete_restaurant():
    # Add a restaurant to ensure it exists
    restrnts.restaurants['Temp Restaurant'] = {
        restrnts.RATING: 5,
        restrnts.PRICE: "$$$",
        restrnts.CUISINE: "Test Cuisine",
        restrnts.ADDRESS: "Test Address"
    }

    # Delete the restaurant and test for success message
    result = restrnts.delete_restaurant('Temp Restaurant')
    assert result == "Temp Restaurant has been deleted."
    assert 'Temp Restaurant' not in restrnts.restaurants

    # Try to delete a non-existing restaurant and test for failure message
    result = restrnts.delete_restaurant('Fake Restaurant')
    assert result == "Fake Restaurant not found in the list."

def test_leave_review():
    # Setup: an empty reviews dictionary
    reviews = {}

    # Test adding a review to a restaurant with no previous reviews
    leave_review("Pizzeria Roma", "Great pizza!", reviews)
    assert "Pizzeria Roma" in reviews
    assert reviews["Pizzeria Roma"] == ["Great pizza!"]

    # Test adding another review to the same restaurant
    leave_review("Pizzeria Roma", "Excellent crust.", reviews)
    assert reviews["Pizzeria Roma"] == ["Great pizza!", "Excellent crust."]

    # Test adding a review to a different restaurant
    leave_review("Sushi Place", "Fresh sushi.", reviews)
    assert "Sushi Place" in reviews
    assert reviews["Sushi Place"] == ["Fresh sushi."]
