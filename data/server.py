import Flask
import render_template


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


app = Flask(__name__)


# A list to store restaurant data (in practice, you'd use a database)
restaurants = [
    {'name': 'Restaurant A', 'description': 'Great food and ambiance'},
    {'name': 'Restaurant B', 'description': 'Family-friendly dining'},
]


"""
Was getting lint error "undefined name cursor
def check_credentials(email, password):
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    return user is not None
"""


@app.route('/')
def index():
    return render_template('index.html', restaurants=restaurants)


@app.route('/customer')
def customer_page():
    return render_template('customer.html', restaurants=restaurants)


@app.route('/restaurant')
def restaurant_page():
    return render_template('restaurant.html', restaurants=restaurants)


if __name__ == '__main__':
    app.run(debug=True)
