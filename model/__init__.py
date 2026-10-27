# Model package initialization and non-invasive patches for existing classes
from .Ticket import Ticket
from .Parkingfloor import ParkingFloor
from .Gate import Gate
from .EntryGate import EntryGate
from .ExitGate import ExitGate
from .Vehicle import Vehicle
from .Car import Car
from .Bike import Bike
from .Truck import Truck

# 1. Provide ParkingSpot and attach it to model.Parkingspot module
class ParkingSpot:
    """Represents an individual parking spot on a parking floor."""
    def __init__(self, id: str, allowed_type: str):
        self.id = id
        self.allowed_type = allowed_type
        self.occupied = False

    def try_occupy(self) -> bool:
        if not self.occupied:
            self.occupied = True
            return True
        return False

    def tryOccupy(self) -> bool:
        return self.try_occupy()

    def free(self) -> None:
        self.occupied = False

    def is_occupied(self) -> bool:
        return self.occupied

    def isOccupied(self) -> bool:
        return self.occupied

    def get_id(self) -> str:
        return self.id

    def getId(self) -> str:
        return self.id

    def get_allowed_type(self) -> str:
        return self.allowed_type

    def getAllowedType(self) -> str:
        return self.allowed_type

from . import Parkingspot as _pspot_mod
_pspot_mod.ParkingSpot = ParkingSpot

# 2. Add full functionality to ParkingFloor
def _add_spot(self, spot):
    spot_id = spot.id if hasattr(spot, 'id') else getattr(spot, 'getId', lambda: str(id(spot)))()
    self.spots[spot_id] = spot

def _find_available_spot(self, vehicle_type):
    for spot in self.spots.values():
        allowed = getattr(spot, 'allowed_type', None)
        if allowed is None and hasattr(spot, 'getAllowedType'):
            allowed = spot.getAllowedType()
        can_occupy = False
        if hasattr(spot, 'tryOccupy'):
            can_occupy = spot.tryOccupy()
        elif hasattr(spot, 'try_occupy'):
            can_occupy = spot.try_occupy()
        if allowed == vehicle_type and can_occupy:
            return spot
    return None

ParkingFloor.add_spot = _add_spot
ParkingFloor.addSpot = _add_spot
ParkingFloor.find_available_spot = _find_available_spot
ParkingFloor.findAvailableSpot = _find_available_spot
ParkingFloor.get_spots = lambda self: self.spots
ParkingFloor.getSpots = lambda self: self.spots
ParkingFloor.get_id = lambda self: self.id
ParkingFloor.getId = lambda self: self.id

# 3. Add Java-style and Pythonic accessors to Ticket
Ticket.getTicketId = lambda self: self.ticket_id
Ticket.get_ticket_id = lambda self: self.ticket_id
Ticket.getVehicle = lambda self: self.vehicle
Ticket.get_vehicle = lambda self: self.vehicle
Ticket.getEntryTime = lambda self: self.entry_time
Ticket.get_entry_time = lambda self: self.entry_time
Ticket.getFloorId = lambda self: self.floor_id
Ticket.get_floor_id = lambda self: self.floor_id
Ticket.getSpotId = lambda self: self.spot_id
Ticket.get_spot_id = lambda self: self.spot_id
Ticket.getPaymentStatus = lambda self: self.payment_status
Ticket.get_payment_status = lambda self: self.payment_status
Ticket.setPaymentStatus = lambda self, status: setattr(self, 'payment_status', status)
Ticket.set_payment_status = lambda self, status: setattr(self, 'payment_status', status)

