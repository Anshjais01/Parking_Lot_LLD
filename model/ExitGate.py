from ..enums.GateType import GateType
from .Ticket import Ticket
from .Vehicle import Vehicle
from .Gate import Gate

class ExitGate(Gate):
    def __init__(self, gate_number: str):
        super().__init__(gate_number, GateType.EXIT)