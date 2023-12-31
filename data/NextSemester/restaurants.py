# def get_restaurant_by_name(restaurant_name: str):
#     if restaurant_name in restaurants:
#         return restaurants[restaurant_name]
#     raise ValueError(f'{restaurant_name} does not exist')


# def get_highly_rated_restaurants(min_rating=4):
#     highly_rated_restaurants = [restaurant for restaurant, data in restaurants.items() if data[RATING] >= min_rating]
#     return [{restaurant: restaurants[restaurant]} for restaurant in highly_rated_restaurants]


# def get_restaurants_with_min_name_length(min_length=MIN_RESTAURANT_NAME_LEN):
#     """
#     Get a list of restaurants with names of at least a specified minimum length.

#     Parameters:
#     - min_length (int): The minimum length of restaurant names to include.

#     Returns:
#     - A list of dictionaries, each containing information about restaurants meeting the criteria.
#     """
#     valid_restaurants = {restaurant: data for restaurant, data in restaurants.items() if len(restaurant) >= min_length}
#     return [{restaurant: valid_restaurants[restaurant]} for restaurant in valid_restaurants]


# def search_restaurants(search_criteria, restaurants):
#     """
#     Search and filter restaurants based on user-defined criteria.

#     Parameters:
#     - search_criteria (dict): A dictionary containing user-defined search criteria.
#         Example:
#         {
#             "cuisine": "Italian",
#             "location": "New York",
#             "min_rating": 4
#         }
#     - restaurants (dict): A dictionary of restaurants with their details.

#     Returns:
#     - A list of dictionaries, each containing information about restaurants that match the criteria.
#     """
#     matching_restaurants = []

#     for restaurant, data in restaurants.items():
#         cuisine = data.get("cuisine", "")
#         location = data.get("location", "")
#         rating = data.get("rating", 0)

#         # Check if the restaurant meets the search criteria
#         if (
#             (not search_criteria.get("cuisine") or search_criteria["cuisine"].lower() == cuisine.lower()) and
#             (not search_criteria.get("location") or search_criteria["location"].lower() == location.lower()) and
#             rating >= search_criteria.get("min_rating", 0)
#         ):
#             matching_restaurants.append({
#                 "name": restaurant,
#                 "cuisine": cuisine,
#                 "location": location,
#                 "rating": rating
#             })

#     return matching_restaurants

# def find_restaurants_by_price(restaurants, price_range="$$"):
#     """
#     Find restaurants that match a specified price range.

#     Parameters:
#     - restaurants (list of dictionaries): A list of restaurant dictionaries, each containing price information.
#     - price_range (str): The price range to filter by, e.g., "$", "$$", "$$$", "$$$$".

#     Returns:
#     - A list of restaurants that match the specified price range.
#     """
#     matching_restaurants = []

#     for restaurant in restaurants:
#         if restaurant.get("price") == price_range:
#             matching_restaurants.append(restaurant)

#     return matching_restaurants

# Function to find the nearest restaurant to the user's location
# def find_nearest_restaurant(user_lat, user_lon, restaurant_data):
#     if not restaurant_data:
#         return "No restaurants available."

#     nearest_distance = float('inf')
#     nearest_restaurant = None

#     for restaurant in restaurant_data:
#         restaurant_lat = restaurant['latitude']
#         restaurant_lon = restaurant['longitude']
#         distance = haversine(user_lat, user_lon, restaurant_lat, restaurant_lon)

#         if distance < nearest_distance:
#             nearest_distance = distance
#             nearest_restaurant = restaurant

#    return nearest_restaurant


# def leave_review(restaurant_name, review_text, review_stars, reviews):
#     if restaurant_name in reviews:
#         # If the restaurant already has reviews, append the new review to the list of reviews
#         reviews[restaurant_name].append([review_stars, review_text])

#     else:
#         # If the restaurant has no reviews yet, create a new list with the first review
#         reviews[restaurant_name] = [review_stars, review_text]


# def delete_review(restaurant_name, target_review_text, reviews):
#     if restaurant_name in reviews:
#         for review_stars, review_text in reviews:
#             if review_text == target_review_text:
#                 reviews[restaurant_name].remove([review_stars, review_text])
#     else:
#         return f"{restaurant_name} not found in reviews."



# def _gen_id() -> str:
#     _id = random.randint(0, BIG_NUM)
#     _id = str(_id)
#     _id = _id.rjust(ID_LEN, '0')
#     return _id