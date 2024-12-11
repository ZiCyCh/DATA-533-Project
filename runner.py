import csv
import os
from booking_management.user import User
from booking_management.booking import Booking
from vehicle_management.vehicle import Vehicle
from vehicle_management.fleet import Fleet

def export_data(fleet):
    """Export all current data to CSV files, overwriting the files to avoid duplicates."""
    user_file = "users.csv"
    vehicle_file = "vehicles.csv"
    booking_file = "bookings.csv"

    # Export Users
    with open(user_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email"])
        for user in User.get_all_users():
            writer.writerow([user.name, user.email])

    # Export Vehicles
    with open(vehicle_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "License Plate", "Make", "Model", "Availability"])
        for vehicle in fleet.vehicles:
            writer.writerow([vehicle.vehicle_type, vehicle.license_plate, vehicle.make, vehicle.model, vehicle.is_available])

    # Export Bookings
    with open(booking_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["User Name", "User Email", "Resource", "Start Date", "End Date", "Status"])
        for booking in Booking._bookings:
            resource = booking.resource
            resource_details = (resource.license_plate if isinstance(resource, Vehicle) else "Fleet")
            writer.writerow([booking.user.name, booking.user.email, resource_details, booking.start_date, booking.end_date, booking.status])

def read_data(fleet):
    """Read all saved data from CSV files on startup."""
    user_file = "users.csv"
    vehicle_file = "vehicles.csv"
    booking_file = "bookings.csv"

    # Read Users
    if os.path.exists(user_file):
        with open(user_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            for row in reader:
                if len(row) == 2:
                    User(row[0], row[1])

    # Read Vehicles
    if os.path.exists(vehicle_file):
        with open(vehicle_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            for row in reader:
                if len(row) == 5:
                    vehicle = Vehicle(row[0], row[1], row[2], row[3])
                    vehicle.is_available = row[4] == 'True'
                    fleet.add_vehicle(vehicle)

    # Read Bookings
    if os.path.exists(booking_file):
        with open(booking_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            for row in reader:
                if len(row) == 6:
                    user = User.find_user_by_email(row[1])
                    if not user:
                        user = User(row[0], row[1])
                    resource = fleet.find_vehicle_by_plate(row[2]) if row[2] != "Fleet" else fleet

                    # Temporarily mark the vehicle as available
                    if isinstance(resource, Vehicle) and not resource.is_available:
                        resource.is_available = True

                    booking = Booking(user, resource, row[3], row[4])
                    booking.status = row[5]

                    # Restore original availability
                    if isinstance(resource, Vehicle) and booking.status == "Active":
                        resource.is_available = False


def run_car_sharing_system():
    fleet = Fleet()
    read_data(fleet)

    while True:
        print("\nWelcome to the Car Sharing System")
        print("1. Add a User")
        print("2. Create and Add a Vehicle to Fleet")
        print("3. List All Users")
        print("4. List All Vehicles")
        print("5. List All Bookings")
        print("6. Create a Booking")
        print("7. Cancel a Booking")
        print("8. Update User")
        print("9. Find User by Email")
        print("10. Remove Vehicle by License Plate")
        print("11. Find Vehicle by License Plate")
        print("12. Get All Bookings for a Given User")
        print("13. Update Vehicle Details")
        print("14. Export Data")
        print("15. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 15.")
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
                print(f"Vehicle created and added to fleet: {vehicle}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 3:
            print("\nAll Users:")
            for user in User.get_all_users():
                print(user)

        elif choice == 4:
            print("\nAll Vehicles:")
            for vehicle in fleet.vehicles:
                print(vehicle)

        elif choice == 5:
            print("\nAll Bookings:")
            for booking in Booking._bookings:
                print(booking)

        elif choice == 6:
            email = input("Enter user email for booking: ")
            user = User.find_user_by_email(email)
            if not user:
                print("User not found. Please create the user first.")
                continue

            resource_type = input("Do you want to book a 'Vehicle' or 'Fleet'? ").strip().lower()

            if resource_type == 'vehicle':
                license_plate = input("Enter vehicle license plate: ")
                resource = fleet.find_vehicle_by_plate(license_plate)
                if not resource:
                    print("Vehicle not found. Please add it to the fleet first.")
                    continue
            elif resource_type == 'fleet':
                resource = fleet
            else:
                print("Invalid resource type. Please choose 'Vehicle' or 'Fleet'.")
                continue

            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            try:
                booking = Booking(user, resource, start_date, end_date)
                print(f"Booking created: {booking}")
            except ValueError as e:
                print(f"Error: {e}")


        elif choice == 7:
            email = input("Enter user email to find bookings: ")
            user = User.find_user_by_email(email)
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
                    booking_to_cancel = user_bookings[cancel_idx - 1]
                    booking_to_cancel.cancel_booking()
                    print("Booking cancelled.")
                else:
                    print("Invalid booking number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 8:
            email = input("Enter user email to update: ")
            user = User.find_user_by_email(email)
            if user:
                name = input("Enter new name (leave blank to keep current): ")
                new_email = input("Enter new email (leave blank to keep current): ")
                try:
                    user.update_user_details(name=name or user.name, email=new_email or user.email)
                    print(f"User updated: {user}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("User not found.")

        elif choice == 9:
            email = input("Enter user email to find: ")
            user = User.find_user_by_email(email)
            if user:
                print(f"User found: {user}")
            else:
                print("User not found.")

        elif choice == 10:
            license_plate = input("Enter vehicle license plate to remove: ")
            found_vehicle = fleet.find_vehicle_by_plate(license_plate)
            if found_vehicle:
                try:
                    fleet.remove_vehicle_by_plate(license_plate)
                    print(f"Vehicle with license plate {license_plate} removed.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print(f"Error: Vehicle with license plate {license_plate} is not in the fleet.")



        elif choice == 11:
            license_plate = input("Enter vehicle license plate to find: ")
            vehicle = fleet.find_vehicle_by_plate(license_plate)
            if vehicle:
                print(f"Vehicle found: {vehicle}")
            else:
                print("Vehicle not found.")

        elif choice == 12:
            email = input("Enter user email to find bookings: ")
            user = User.find_user_by_email(email)
            if user:
                user_bookings = Booking.get_bookings_by_user(user)
                if user_bookings:
                    print("\nBookings for the user:")
                    for booking in user_bookings:
                        print(booking)
                else:
                    print("No bookings found for the user.")
            else:
                print("User not found.")

        elif choice == 13:
            license_plate = input("Enter vehicle license plate to update: ")
            vehicle = fleet.find_vehicle_by_plate(license_plate)
            if vehicle:
                vehicle_type = input("Enter new vehicle type (leave blank to keep current): ")
                make = input("Enter new make (leave blank to keep current): ")
                model = input("Enter new model (leave blank to keep current): ")
                vehicle.update_details(vehicle_type=vehicle_type or vehicle.vehicle_type, make=make or vehicle.make, model=model or vehicle.model)
                print(f"Vehicle updated: {vehicle}")
            else:
                print("Vehicle not found.")

        elif choice == 14:
            export_data(fleet)
            print("Data exported successfully.")

        elif choice == 15:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 15.")
