
# car_sharing_system/booking_management/user.py

class User:
    _users = []

    def __init__(self, name, email):
        if any(user.name == name and user.email == email for user in User._users):
            raise ValueError("User already exists.")
        self.name = name
        self.email = email
        User._users.append(self)
    @classmethod
    def get_all_users(cls):
        return cls._users

    def update_user_details(self, name=None, email=None):
        """Update the user details for this booking."""
        if name:
            self.name = name
        if email:
            if '@' not in email:
                raise ValueError("Invalid email address.")
            self.email = email
        print(f"User details updated for booking: {self}")



    @classmethod
    def find_user_by_email(cls, email):
        """
        Find and return a user by their email address.
        """
        for user in cls._users:
            if user.email == email:
                return user
        return None

    def __str__(self):
        return f"User: {self.name} (Email: {self.email})"
