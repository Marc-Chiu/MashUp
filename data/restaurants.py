"""
This module interfaces to our restaraunts data
"""
RATING = "Rating"
MIN_Group_NAME_LEN = 2
MIN_RESTAURANT_NAME_LEN = 2
CUISINE = "Cuisine"
ADDRESS = "Address"
PRICE = "Price"


def get_restaurants():
    """
    Our Contract:
        - No arguments.
        - Returns a dictionary of restaraunts keyed on name (a str).
        - Each user name must be the key for a dictionary.
        - Each restaraunt must have a rating (int)
    """
    restaurants = {
        "Shake Shack": {
            RATING: 4,
            PRICE: "$$",
            CUISINE: "American",
            ADDRESS: "123 E 6th Street"
        },
        "Caine's": {
            RATING: 5,
            PRICE: "$$",
            CUISINE: "American",
            ADDRESS: "223 E 4th Street"
        },
    }
    return restaurants


def get_restaurant_by_name(restaurant_name):
    """
    Get restaurant details by name.

    Parameters:
    - restaurant_name (str): The name of the restaurant to retrieve.

    Returns:
    - A dictionary containing the restaurant's information, e.g rating
    - Returns None if the restaurant is not found.
    """
    restaurants = get_restaurants()
    return restaurants[restaurant_name]


def get_highly_rated_restaurants(min_rating=4):
    """
    Get a list of highly rated restaurants.

    Parameters:
    - min_rating (int): The minimum rating for a restaurant to be considered
    highly rated.

    Returns:
    - A list of dictionaries, each containing information about highly rated
    restaurants.
    """
    restaurants = get_restaurants()
    highly_rated_restaurants = [restaurant for restaurant, data in restaurants.items() if data[RATING] >= min_rating]
    return [{restaurant: restaurants[restaurant]} for restaurant in highly_rated_restaurants]


def get_restaurants_with_min_name_length(min_length=MIN_RESTAURANT_NAME_LEN):
    """
    Get a list of restaurants with names of at least a specified minimum length.

    Parameters:
    - min_length (int): The minimum length of restaurant names to include.

    Returns:
    - A list of dictionaries, each containing information about restaurants meeting the criteria.
    """
    restaurants = get_restaurants()
    valid_restaurants = {restaurant: data for restaurant, data in restaurants.items() if len(restaurant) >= min_length}
    return [{restaurant: valid_restaurants[restaurant]} for restaurant in valid_restaurants]


def search_restaurants(search_criteria, restaurants):
    """
    Search and filter restaurants based on user-defined criteria.

    Parameters:
    - search_criteria (dict): A dictionary containing user-defined search criteria.
        Example:
        {
            "cuisine": "Italian",
            "location": "New York",
            "min_rating": 4
        }
    - restaurants (dict): A dictionary of restaurants with their details.

    Returns:
    - A list of dictionaries, each containing information about restaurants that match the criteria.
    """
    matching_restaurants = []

    for restaurant, data in restaurants.items():
        cuisine = data.get("cuisine", "")
        location = data.get("location", "")
        rating = data.get("rating", 0)

        # Check if the restaurant meets the search criteria
        if (
            (not search_criteria.get("cuisine") or search_criteria["cuisine"].lower() == cuisine.lower()) and
            (not search_criteria.get("location") or search_criteria["location"].lower() == location.lower()) and
            rating >= search_criteria.get("min_rating", 0)
        ):
            matching_restaurants.append({
                "name": restaurant,
                "cuisine": cuisine,
                "location": location,
                "rating": rating
            })

    return matching_restaurants

def find_restaurants_by_price(restaurants, price_range):
    """
    Find restaurants that match a specified price range.

    Parameters:
    - restaurants (list of dictionaries): A list of restaurant dictionaries, each containing price information.
    - price_range (str): The price range to filter by, e.g., "$", "$$", "$$$", "$$$$".

    Returns:
    - A list of restaurants that match the specified price range.
    """
    matching_restaurants = []
    for restaurant in restaurants:
        if restaurant.get("price") == price_range:
            matching_restaurants.append(restaurant)

    return matching_restaurants