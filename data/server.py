class SimpleServer:
    def __init__(self):
        self.users = []  # In-memory user storage

    def add_user(self, email, password):
        # Check if the email is already registered
        for user in self.users:
            if user['email'] == email:
                print("User with this email already exists.")
                return False
        
        # If the email is not already registered, add the user
        self.users.append({'email': email, 'password': password})
        print("User added successfully.")
        return True