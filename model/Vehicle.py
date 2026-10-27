from abc import ABC
from ..enums.VehicleType import VehicleType


class Vehicle(ABC):
    def __init__(self, number: str, type: VehicleType):
        self.number = number
        self.type = type

    def getNumber(self) -> str:
        return self.number

    def getType(self) -> VehicleType:
        return self.type