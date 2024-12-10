from booking_management.user import User
from booking_management.booking import Booking
from vehicle_management.vehicle import Vehicle
from vehicle_management.fleet import Fleet

def main():
    # Create some users
    user1 = User("Alice", "alice@example.com")
    user2 = User("Bob", "bob@example.com")
    user3 = User("Charlie", "charlie@example.com")
    print("Users created:")
    for user in User.get_all_users():
        print(user)

    # Test updating user details
    user1.update_details(name="Alice Updated", email="alice.updated@example.com")
    print(f"Updated user1: {user1}")

    # Test finding a user by email
    found_user = User.find_user_by_email("bob@example.com")
    print(f"Found user by email: {found_user}")

    # Create a vehicle fleet and add some vehicles
    fleet = Fleet()
    vehicle1 = Vehicle("Sedan", "ABC-1234", "Toyota", "Camry")
    vehicle2 = Vehicle("SUV", "XYZ-5678", "Ford", "Explorer")
    vehicle3 = Vehicle("Truck", "LMN-9101", "Chevrolet", "Silverado")
    fleet.add_vehicle(vehicle1)
    fleet.add_vehicle(vehicle2)
    try:
        # Attempt to add a vehicle with duplicate plate
        fleet.add_vehicle(Vehicle("SUV", "ABC-1234", "Honda", "CRV"))
    except ValueError as e:
        print(e)

    # List available vehicles
    print("Available vehicles:")
    print(fleet.list_available_vehicles())

    # Test finding a vehicle by license plate
    found_vehicle = fleet.find_vehicle_by_plate("XYZ-5678")
    print(f"Found vehicle by plate: {found_vehicle}")

    # Make bookings
    booking1 = Booking(user1, vehicle1, "2024-12-01", "2024-12-05")
    try:
        # Attempt to add a vehicle with duplicate plate
        booking2 = Booking(user2, fleet, "2024-12-10", "2024-12-15")
    except ValueError as e:
        print(e)
    print("\nBookings made:")
    print(booking1)

    # Cancel a booking
    booking1.cancel_booking()
    print(f"After cancelling booking1: {booking1}")
    booking2 = Booking(user2, fleet, "2024-12-10", "2024-12-15")  # Book entire fleet
    print(booking2)
    # List bookings for a user
    user1_bookings = Booking.get_bookings_by_user(user1)
    print("\nBookings for user1:")
    for booking in user1_bookings:
        print(booking)

if __name__ == "__main__":
    main()
