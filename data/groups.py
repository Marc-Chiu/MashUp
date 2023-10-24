"""
This module interfaces to our groups data
"""

MIN_Group_NAME_LEN = 2
MEMBERS = "Members"
RESTAURANTS = "Restaurants"


def get_groups():
    """
    Our Contract:
        - No arguments.
        - Returns a dictionary of groups keyed on group name (a str).
        - Each user name must be the key for a dictionary.
        - Each group must have a list of memembers
        - Each group must have a list of liked restaurants
    """
    groups = {
        "Foodies": {
            MEMBERS: ["Marc"],
            RESTAURANTS: ["Shack Shake"],
        },
        "Reddy": {
            MEMBERS: ["Red"],
            RESTAURANTS: ["Caine's"],
        },
    }
    return groups
