import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from vehicle_management.fleet import Fleet
from vehicle_management.vehicle import Vehicle


class TestFleet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up TestFleet class resources...")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down TestFleet class resources...")

    def setUp(self):
        self.fleet = Fleet()
        self.vehicle1 = Vehicle("SUV", "XYZ-5678", "Ford", "Explorer")
        self.vehicle2 = Vehicle("Sedan", "ABC-1234", "Toyota", "Camry")
        self.fleet.add_vehicle(self.vehicle1)
        self.fleet.add_vehicle(self.vehicle2)

    def tearDown(self):
        self.fleet = None

    def test_add_vehicle(self):
        self.assertEqual(len(self.fleet.vehicles), 2)
        vehicle3 = Vehicle("Truck", "DEF-8901", "Chevrolet", "Silverado")
        self.fleet.add_vehicle(vehicle3)
        self.assertEqual(len(self.fleet.vehicles), 3)

    def test_list_available_vehicles(self):
        available = self.fleet.list_available_vehicles()
        self.assertEqual(len(available), 2)
        self.vehicle1.mark_as_rented()
        available = self.fleet.list_available_vehicles()
        self.assertEqual(len(available), 1)
