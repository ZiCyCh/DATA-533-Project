# tests/test_car_sharing.py
import sys
import os
sys.path.append(os.path.abspath('../'))

from booking_management.user import User
from booking_management.booking import Booking
from vehicle_management.vehicle import Vehicle
from vehicle_management.fleet import Fleet

def test_vehicle_creation():
    vehicle = Vehicle("Sedan", "ABC-1234", "Toyota", "Camry")
    assert vehicle.license_plate == "ABC-1234"
    assert vehicle.is_available

def test_user_creation():
    user = User("Alice", "alice@example.com")
    assert user.email == "alice@example.com"

def test_user_update_and_find():
    user = User("Bob", "bob@example.com")
    user.update_details(name="Bob Updated", email="bob.updated@example.com")
    assert user.name == "Bob Updated"
    assert user.email == "bob.updated@example.com"

    found_user = User.find_user_by_email("bob.updated@example.com")
    assert found_user == user

def test_booking_creation_and_cancellation():
    user = User("Charlie", "charlie@example.com")
    vehicle = Vehicle("SUV", "XYZ-5678", "Ford", "Explorer")
    booking = Booking(user, vehicle, "2024-12-01", "2024-12-05")
    assert booking.start_date == "2024-12-01"
    assert vehicle.is_available == False

    booking.cancel_booking()
    assert booking.status == "Cancelled"
    assert vehicle.is_available == True

def test_fleet_management():
    fleet = Fleet()
    vehicle1 = Vehicle("Truck", "LMN-9101", "Chevrolet", "Silverado")
    vehicle2 = Vehicle("Sedan", "ABC-1234", "Toyota", "Camry")
    fleet.add_vehicle(vehicle1)
    fleet.add_vehicle(vehicle2)

    # Ensure no duplicate vehicles
    try:
        fleet.add_vehicle(Vehicle("Truck", "LMN-9101", "Chevrolet", "Silverado"))
    except ValueError as e:
        assert str(e) == "Vehicle with license plate LMN-9101 already exists in the fleet."

    assert len(fleet.list_available_vehicles()) == 2

def test_fleet_booking():
    user = User("Diana", "diana@example.com")
    fleet = Fleet()
    vehicle1 = Vehicle("Sedan", "GHI-2345", "Honda", "Civic")
    vehicle2 = Vehicle("SUV", "JKL-6789", "Nissan", "Rogue")
    fleet.add_vehicle(vehicle1)
    fleet.add_vehicle(vehicle2)

    booking = Booking(user, fleet, "2024-12-10", "2024-12-15")
    assert booking.start_date == "2024-12-10"
    assert vehicle1.is_available == False
    assert vehicle2.is_available == False

    booking.cancel_booking()
    assert vehicle1.is_available == True
    assert vehicle2.is_available == True

if __name__ == "__main__":
    test_vehicle_creation()
    test_user_creation()
    test_user_update_and_find()
    test_booking_creation_and_cancellation()
    test_fleet_management()
    test_fleet_booking()
    print("All tests passed.")
