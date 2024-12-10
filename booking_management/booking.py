
# car_sharing_system/booking_management/booking.py

from vehicle_management.vehicle import Vehicle
from vehicle_management.fleet import Fleet
from booking_management.user import User

class Booking:
    _bookings = []

    def __init__(self, user, resource, start_date, end_date):
        if not isinstance(user, User):
            raise TypeError("Invalid user. Must be an instance of User.")
        if not isinstance(resource, (Vehicle, Fleet)):
            raise TypeError("Invalid resource. Must be a Vehicle or a Fleet.")
        
        self.user = user
        self.resource = resource
        self.start_date = start_date
        self.end_date = end_date
        self.status = "Active"
        
        if isinstance(resource, Vehicle):
            if not resource.is_available:
                raise ValueError("Vehicle is not available for booking.")
            resource.mark_as_rented()
        elif isinstance(resource, Fleet):
            unavailable_vehicles = [v for v in resource.vehicles if not v.is_available]
            if unavailable_vehicles:
                raise ValueError("Some vehicles in the fleet are not available for booking.")
            for vehicle in resource.vehicles:
                vehicle.mark_as_rented()
        
        Booking._bookings.append(self)

    def cancel_booking(self):
        self.status = "Cancelled"
        if isinstance(self.resource, Vehicle):
            self.resource.mark_as_available()
        elif isinstance(self.resource, Fleet):
            for vehicle in self.resource.vehicles:
                vehicle.mark_as_available()

    @classmethod
    def get_bookings_by_user(cls, user):
        return [booking for booking in cls._bookings if booking.user == user]

    def __str__(self):
        if isinstance(self.resource, Vehicle):
            resource_details = f"Vehicle ({self.resource.make} {self.resource.model})"
        else:
            resource_details = f"Fleet ({len(self.resource.vehicles)} vehicles)"
        return (f"Booking for {self.user.name} - {resource_details} "
                f"from {self.start_date} to {self.end_date} - Status: {self.status}")
