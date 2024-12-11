
# car_sharing_system/vehicle_management/vehicle.py
class BookingError(Exception):
    """Custom exception for booking-related errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Vehicle:
    def __init__(self, vehicle_type, license_plate, make, model):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.make = make
        self.model = model
        self.is_available = True

    def mark_as_rented(self):
        try:
            if not self.is_available:
                raise BookingError(f"Vehicle {self.license_plate} is already rented.")
            self.is_available = False
        except BookingError as e:
            print(f"Error: {e}")

    def mark_as_available(self):
        try:
            if self.is_available:
                raise BookingError(f"Vehicle {self.license_plate} is already available.")
            self.is_available = True
        except BookingError as e:
            print(f"Error: {e}")

    def update_details(self, vehicle_type=None, make=None, model=None):
        if vehicle_type:
            self.vehicle_type = vehicle_type
        if make:
            self.make = make
        if model:
            self.model = model

    def __str__(self):
        availability = "Available" if self.is_available else "Rented"
        return (f"{self.vehicle_type} - {self.make} {self.model} "
                f"(Plate: {self.license_plate}) - {availability}")
