# `car_sharing_system` Package
### Author: Tianmu Wang, Zifei Chen

The `car_sharing_system` Package is a modular framework for managing a car-sharing platform. It is divided into two sub-packages: **booking_management** and **vehicle_management**.

---

### `booking_management` Sub-package
#### `user` Module
This module manages user accounts and ensures data integrity by avoiding duplicates.

**Methods**
1. `__init__(name, email)`:
   - Create a new user while ensuring no duplicate entries based on name and email.

2. `get_all_users()`:
   - Retrieve a list of all registered users.

3. `update_details(name=None, email=None)`:
   - Update user details (name or email) with duplication checks.

4. `find_user_by_email(email)`:
   - Retrieve a user by their email address.

---

#### `booking` Module
This module manages bookings for vehicles or fleets, including creation, cancellation, and tracking.

**Methods**
1. `__init__(user, resource, start_date, end_date)`:
   - Create a booking for a user. The resource can be a `Vehicle` or a `Fleet`.

2. `cancel_booking()`:
   - Cancel a booking and restore the availability of the resource.

3. `get_bookings_by_user(user)`:
   - Retrieve all bookings made by a specific user.

4. `__str__()`:
   - Return a human-readable representation of the booking details.

---

### `vehicle_management` Sub-package
#### `vehicle` Module
This module represents individual vehicles, including their status and details.

**Methods**
1. `__init__(vehicle_type, license_plate, make, model)`:
   - Initialize a new vehicle with its details.

2. `mark_as_rented()`:
   - Mark the vehicle as rented.

3. `mark_as_available()`:
   - Mark the vehicle as available.

4. `update_details(vehicle_type=None, make=None, model=None)`:
   - Update the details of a vehicle.

5. `__str__()`:
   - Provide a string representation of the vehicle's details and availability.

---

#### `fleet` Module
This module manages collections of vehicles and provides fleet-related operations.

**Methods**
1. `__init__()`:
   - Initialize a fleet.

2. `add_vehicle(vehicle)`:
   - Add a vehicle to the fleet while avoiding duplicates by license plate.

3. `remove_vehicle_by_plate(license_plate)`:
   - Remove a vehicle from the fleet using its license plate.

4. `list_available_vehicles()`:
   - List all available vehicles in the fleet.

5. `find_vehicle_by_plate(license_plate)`:
   - Find a vehicle in the fleet by its license plate.

6. `__str__()`:
   - Provide a summary of the fleet, including the total number of vehicles.

---

### Usage
To use this package, create instances of `User`, `Vehicle`, and `Fleet` to manage users, vehicles, and fleets. Utilize the `Booking` module to create and manage reservations. See the provided test scripts for implementation examples.

---
=======
# `car_sharing_system` Package
### Author: Tianmu Wang, Zifei Chen

The `car_sharing_system` Package is a modular framework for managing a car-sharing platform. It is divided into two sub-packages: **booking_management** and **vehicle_management**.

---

### `booking_management` Sub-package
#### `user` Module
This module manages user accounts and ensures data integrity by avoiding duplicates.

**Methods**
1. `__init__(name, email)`:
   - Create a new user while ensuring no duplicate entries based on name and email.

2. `get_all_users()`:
   - Retrieve a list of all registered users.

3. `update_details(name=None, email=None)`:
   - Update user details (name or email) with duplication checks.

4. `find_user_by_email(email)`:
   - Retrieve a user by their email address.
