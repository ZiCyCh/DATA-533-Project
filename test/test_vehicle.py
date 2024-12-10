import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from vehicle_management.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up TestVehicle class resources...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestVehicle class resources...")

    def setUp(self):
        self.vehicle = Vehicle("Sedan", "ABC-1234", "Toyota", "Camry")

    def tearDown(self):
        self.vehicle = None

    def test_vehicle_initialization(self):
        self.assertEqual(self.vehicle.vehicle_type, "Sedan")
        self.assertEqual(self.vehicle.license_plate, "ABC-1234")
        self.assertEqual(self.vehicle.make, "Toyota")
        self.assertEqual(self.vehicle.model, "Camry")

    def test_vehicle_availability(self):
        self.assertTrue(self.vehicle.is_available)
        self.vehicle.mark_as_rented()
        self.assertFalse(self.vehicle.is_available)
        self.vehicle.mark_as_available()
        self.assertTrue(self.vehicle.is_available)
