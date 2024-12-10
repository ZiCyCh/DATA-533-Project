import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from booking_management.booking import Booking
from booking_management.user import User
from vehicle_management.vehicle import Vehicle



# Add the root directory to sys.path




class TestBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up TestBooking class resources...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestBooking class resources...")

    def setUp(self):
        self.user = User("Bob", "bob@example.com")
        self.vehicle = Vehicle("Sedan", "GHI-1234", "Honda", "Civic")
        self.booking = Booking(self.user, self.vehicle, "2024-12-01", "2024-12-05")

    def tearDown(self):
        self.booking = None

    def test_booking_initialization(self):
        self.assertEqual(self.booking.user.name, "Bob")
        self.assertEqual(self.booking.resource.make, "Honda")
        self.assertEqual(self.booking.start_date, "2024-12-01")
        self.assertEqual(self.booking.end_date, "2024-12-05")

    def test_booking_cancellation(self):
        self.assertEqual(self.booking.status, "Active")
        self.booking.cancel_booking()
        self.assertEqual(self.booking.status, "Cancelled")
        self.assertTrue(self.vehicle.is_available)
