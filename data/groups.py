"""
This module interfaces to our groups data
"""

MEMBERS = []
MIN_Group_NAME_LEN = 2


def get_groups():
    """
    Our Contract:
        - No arguments.
        - Returns a dictionary of groups keyed on group name (a str).
        - Each user name must be the key for a dictionary.
        - Each group must have a list of memembers
    """
    groups = {
        "Foodies": {
            MEMBERS: ["Marc"] ,
        },
        "Reddy": {
            MEMBERS: ["Red"],
        },
    }
    return users
