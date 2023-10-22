"""
This module interfaces to our restaraunts data
"""
RATING = "Rating"
MIN_Group_NAME_LEN = 2

def get_restaraunts():
    """
    Our Contract:
        - No arguments.
        - Returns a dictionary of restaraunts keyed on name (a str).
        - Each user name must be the key for a dictionary.
        - Each restaraunt must have a rating (int)
    """
    restaraunts = {
        "Shake Shack": {
            RATING: 4,
        },
        "Caine's": {
            RATING: 5,
        },
    }
    return restaraunts
