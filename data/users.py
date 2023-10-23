"""
This module interfaces to our user data
"""
LEVEL = 'level'
MIN_USER_NAME_LEN = 2
import smtplib
import re


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
