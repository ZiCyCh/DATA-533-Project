import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from booking_management.user import User

class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up TestUser class resources...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestUser class resources...")

    def setUp(self):
        self.user = User("Alice", "alice@example.com")

    def tearDown(self):
        self.user = None

    def test_user_initialization(self):
        self.assertEqual(self.user.name, "Alice")
        self.assertEqual(self.user.email, "alice@example.com")

    def test_user_string_representation(self):
        self.assertEqual(str(self.user), "User: Alice (Email: alice@example.com)")
