from .Vehicle import Vehicle
from ..enums import VehicleType

class Bike(Vehicle):
    def __init__(self, number: str):
        super().__init__(number, VehicleType.BIKE)