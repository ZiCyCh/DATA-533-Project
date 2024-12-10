
# car_sharing_system/vehicle_management/vehicle.py

class Vehicle:
    def __init__(self, vehicle_type, license_plate, make, model):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.make = make
        self.model = model
        self.is_available = True

    def mark_as_rented(self):
        self.is_available = False

    def mark_as_available(self):
        self.is_available = True

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
