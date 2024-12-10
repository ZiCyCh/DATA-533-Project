
# car_sharing_system/booking_management/user.py

class User:
    _users = []

    def __init__(self, name, email):
        if any(user.name == name and user.email == email for user in User._users):
            print("user's information has been updated")
        self.name = name
        self.email = email
        User._users.append(self)
    @classmethod
    def get_all_users(cls):
        return cls._users

    def update_details(self, name=None, email=None):
        """
        Update the user's name and/or email.
        Ensures no duplicates are created during the update process.
        """
        if name:
            if any(user.name == name and user.email == (email or self.email) for user in User._users if user != self):
                raise ValueError("Updating to this name and email would create a duplicate user.")
            self.name = name
        if email:
            if any(user.email == email and user.name == (name or self.name) for user in User._users if user != self):
                raise ValueError("Updating to this name and email would create a duplicate user.")
            self.email = email

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
