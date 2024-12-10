import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from test_vehicle import TestVehicle
from test_fleet import TestFleet
from test_user import TestUser
from test_booking import TestBooking

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestVehicle))
    suite.addTest(unittest.makeSuite(TestFleet))
    suite.addTest(unittest.makeSuite(TestUser))
    suite.addTest(unittest.makeSuite(TestBooking))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
