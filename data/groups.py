"""
This module interfaces to our groups data
"""

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
            'Memeber1': "Marc",
        },
        "Reddy": {
            'Member2': "Red",
        },
    }
    return groups
