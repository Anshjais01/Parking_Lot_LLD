from ..enums.GateType import GateType
from .Ticket import Ticket
from .Gate import Gate
from .Vehicle import Vehicle

class EntryGate(Gate):
    def __init__(self, gate_number: str):
        super().__init__(gate_number, GateType.ENTRY)
    
