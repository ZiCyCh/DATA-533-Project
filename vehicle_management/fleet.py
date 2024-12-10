
# car_sharing_system/vehicle_management/fleet.py

from vehicle_management.vehicle import Vehicle

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Only instances of Vehicle can be added.")
        if any(v.license_plate == vehicle.license_plate for v in self.vehicles):
            raise ValueError(f"Vehicle with license plate {vehicle.license_plate} already exists in the fleet.")
        self.vehicles.append(vehicle)

    def remove_vehicle_by_plate(self, license_plate):
        self.vehicles = [vehicle for vehicle in self.vehicles if vehicle.license_plate != license_plate]

    def list_available_vehicles(self):
        return [str(vehicle) for vehicle in self.vehicles if vehicle.is_available]

    def find_vehicle_by_plate(self, license_plate):
        for vehicle in self.vehicles:
            if vehicle.license_plate == license_plate:
                return vehicle
        return None

    def __str__(self):
        return f"Fleet has {len(self.vehicles)} vehicles."
