from booking_management.user import User
from booking_management.booking import Booking
from vehicle_management.vehicle import Vehicle
from vehicle_management.fleet import Fleet

def run_car_sharing_system():
    fleet = Fleet()

    while True:
        print("\nWelcome to the Car Sharing System")
        print("1. Add a User")
        print("2. Add a Vehicle to Fleet")
        print("3. List Available Vehicles")
        print("4. Add a Booking")
        print("5. Cancel a Booking")
        print("6. View Bookings for a User")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            try:
                user = User(name, email)
                print(f"User added: {user}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 2:
            vehicle_type = input("Enter vehicle type (e.g., Sedan, SUV): ")
            license_plate = input("Enter vehicle license plate: ")
            make = input("Enter vehicle make: ")
            model = input("Enter vehicle model: ")
            try:
                vehicle = Vehicle(vehicle_type, license_plate, make, model)
                fleet.add_vehicle(vehicle)
                print(f"Vehicle added to fleet: {vehicle}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 3:
            print("\nAvailable Vehicles:")
            for v in fleet.list_available_vehicles():
                print(v)

        elif choice == 4:
            user_email = input("Enter user email: ")
            user = User.find_user_by_email(user_email)
            if not user:
                print("User not found.")
                continue

            resource_type = input("Do you want to book a 'Vehicle' or 'Fleet'? ").strip().lower()

            if resource_type == 'vehicle':
                license_plate = input("Enter vehicle license plate: ")
                vehicle = fleet.find_vehicle_by_plate(license_plate)
                if not vehicle:
                    print("Vehicle not found.")
                    continue
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                try:
                    booking = Booking(user, vehicle, start_date, end_date)
                    print(f"Booking added: {booking}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif resource_type == 'fleet':
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                try:
                    booking = Booking(user, fleet, start_date, end_date)
                    print(f"Booking added: {booking}")
                except ValueError as e:
                    print(f"Error: {e}")

            else:
                print("Invalid resource type. Please choose 'Vehicle' or 'Fleet'.")

        elif choice == 5:
            user_email = input("Enter user email: ")
            user = User.find_user_by_email(user_email)
            if not user:
                print("User not found.")
                continue

            user_bookings = Booking.get_bookings_by_user(user)
            if not user_bookings:
                print("No bookings found for this user.")
                continue

            print("\nUser Bookings:")
            for idx, booking in enumerate(user_bookings, start=1):
                print(f"{idx}. {booking}")

            try:
                cancel_idx = int(input("Enter the number of the booking to cancel: "))
                if 1 <= cancel_idx <= len(user_bookings):
                    user_bookings[cancel_idx - 1].cancel_booking()
                    print("Booking cancelled.")
                else:
                    print("Invalid booking number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == 6:
            user_email = input("Enter user email: ")
            user = User.find_user_by_email(user_email)
            if not user:
                print("User not found.")
                continue

            user_bookings = Booking.get_bookings_by_user(user)
            if not user_bookings:
                print("No bookings found for this user.")
            else:
                print("\nUser Bookings:")
                for booking in user_bookings:
                    print(booking)

        elif choice == 7:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 7.")
