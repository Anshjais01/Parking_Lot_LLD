from abc import ABC
from ..enums.GateType import GateType

class Gate(ABC):
    def __init__(self, gate_number: str, type: GateType):
        self.gate_number = gate_number
        self.type = type

    def getGateNumber(self) -> str:
        return self.gate_number

    def getType(self) -> GateType:
        return self.type