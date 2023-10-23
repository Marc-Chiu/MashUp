"""
This module interfaces to our user data
"""
LEVEL = 'level'
MIN_USER_NAME_LEN = 2


def get_users():
    """
    Our Contract:
        - No arguments.
        - Returns a dictionary of users keyed on user name (a str).
        - Each user name must be the key for a dictionary.
        - That dictionary must at least include a LEVEL member that has an
        int value.
    """
    users = {
        "Callahan": {
            LEVEL: 0,
        },
        "Reddy": {
            LEVEL: 1,
        },
    }
    return users

def get_users_with_min_name_length(min_length, users):
    """
    Get a list of users with names of at least a specified minimum length.

    Parameters:
    - min_length (int): The minimum length of user names to include.
    - users (dict): A dictionary of users with their details.

    Returns:
    - A list of dictionaries, each containing information about users meeting the name length criteria.
    """
    valid_users = {user_name: data for user_name, data in users.items() if len(user_name) >= min_length}
    return [{user_name: valid_users[user_name]} for user_name in valid_users]
