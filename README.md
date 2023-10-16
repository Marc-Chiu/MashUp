# flask-api
An example flask rest API server.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

MASHUP

User Features

User Authentication: Users should be able to download the app, register, and sign in using their phone number, email address, or social network account.

Filters & Search: The location, cuisine type, pricing range, and ratings are just a few of the factors that users can use to look for restaurants.

Listings of restaurants: A list of restaurants should be displayed that meet the user's search criteria. Include important details like name, cuisine, location, and ratings.

Detailed Restaurant Profiles: Users have access to each restaurant's complete profile, which includes the menu, hours of operation, reviews, and images. 

Integration of Maps: Map out the locations of the restaurants. Give users the option to acquire directions to the preferred eatery.

Ratings and reviews: Publish reviews and ratings for restaurants that users may read and leave. Set up a rating system (such as 1–5 stars).

Bookmarks & Favorites: Users can easily reach their favorite eateries by marking them. Create a bookmark feature to save potential restaurants for later.

Reserving Method: Include a function that allows users to reserve tables at eateries. 

User Profile: Users' profiles, which can include personal data and dietary preferences, can be created and edited.

Notifications: Send push notifications for updates, new restaurant recommendations, and reservation confirmations.



Implementing the Database for this App:

The database will efficiently store and manage various types of data, including user profiles, restaurant information, reviews, reservations, and more. Prior to creating the database, we will design the database schema for our restaurant finder app, MASHUP. We will also create an API layer that serves as an intermediary between the database and the application. It will handle data retrieval, manipulation, and validation, ensuring that the database is protected. We will also implement strict data validation and sanitization to prevent any security vulnerabilities such as SQL injection and other attacks.


