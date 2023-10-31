"""
This module interfaces to our user data
"""

import smtplib
import re
import string
import hashlib


LEVEL = 'level'
MIN_USER_NAME_LEN = 2


# Sample restaurant app user database
users = {}
session = {}  # session was used earlier and not defined in authenticate_user not sure what you wanted


# Function to register a new user
def register_user(username, password):
    if username in users:
        print("Username already exists. Please choose a different one.")
    else:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        users[username] = hashed_password
        print("Registration successful for", username)


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


# Function to authenticate a user
def authenticate_user(username, password):
    if username in users:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if users[username] == hashed_password:
            session['username'] = username
            return "Authentication successful. Welcome, " + username
        else:
            return "Authentication failed. Incorrect password."
    else:
        return "Authentication failed. User not found."


def is_valid_email(email):
    # A simple regex pattern for email validation
    email_pattern = r'^[\w\.-]+@[\w\.-]+$'

    if not re.match(email_pattern, email):
        print("Invalid email format")
        return False

    try:
        # Split the email address to extract the domain
        username, domain = email.split('@')

        # DNS lookup to get the MX (Mail Exchange) records for the domain
        records = smtplib.getmxrr(domain)

        if records:
            # Try to connect to the mail server of the domain
            server = smtplib.SMTP(records[0][1])
            server.quit()
            return True
        else:
            print("No MX records found for the domain")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def create_password():
    """
    Prompt the user to create a password with the following requirements:
    - Minimum length of 6 characters
    - At least one capital letter
    - At least one special character (e.g., !@#$%^&*())

    Returns:
    - A valid password as a string.
    """
    while True:
        password = input("Create a password: ")

        if len(password) < 6:
            print("Password is too short. It must be at least 6 characters.")
            continue

        if not any(char.isupper() for char in password):
            print("Password must contain at least one capital letter.")
            continue

        if not any(char in string.punctuation for char in password):
            print("Password must contain at least one special character.")
            continue

        # If all requirements are met, return the password
        return password


def leave_review(restaurant_name, review_text, reviews):
    """
    Allow a user to leave a review for a restaurant.

    Parameters:
    - restaurant_name (str): The name of the restaurant for which the review is being left.
    - review_text (str): The text of the review.
    - reviews (dict): A dictionary that stores restaurant reviews.

    Returns:
    - None
    """
    if restaurant_name in reviews:
        # If the restaurant already has reviews, append the new review to the list of reviews
        reviews[restaurant_name].append(review_text)
    else:
        # If the restaurant has no reviews yet, create a new list with the first review
        reviews[restaurant_name] = [review_text]
