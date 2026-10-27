'''
package org.nailyourinterview.lld.parking_lot.service;

import lombok.Getter;
import org.nailyourinterview.lld.parking_lot.enums.VehicleType;
import org.nailyourinterview.lld.parking_lot.model.*;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class ParkingLot {
    private static volatile ParkingLot instance;

    @Getter
    private final List<ParkingFloor> floors = new ArrayList<>();
    private final Map<String, EntryGate> entryGates = new ConcurrentHashMap<>();
    private final Map<String, ExitGate> exitGates = new ConcurrentHashMap<>();

    private ParkingLot() {}

    public static ParkingLot getInstance() {
        if (instance == null) {
            synchronized (ParkingLot.class) {
                if (instance == null) {
                    instance = new ParkingLot();
                }
            }
        }
        return instance;
    }

    public void addFloor(ParkingFloor floor) { floors.add(floor); }
    public void addEntryGate(EntryGate gate) { entryGates.put(gate.getGateNumber(), gate); }
    public void addExitGate(ExitGate gate) { exitGates.put(gate.getGateNumber(), gate); }

    public ParkingSpot findSpot(VehicleType type) {
        for (ParkingFloor floor : floors) {
            ParkingSpot spot = floor.findAvailableSpot(type);
            if (spot != null) return spot;
        }
        return null;
    }
}
'''

import threading
from typing import List, Dict, Optional

from ..model.Parkingfloor import ParkingFloor
from ..model.EntryGate import EntryGate
from ..model.ExitGate import ExitGate
from ..enums.VehicleType import VehicleType


class ParkingLot:
    """Singleton Parking Lot managing multiple floors and gates."""

    _instance: Optional['ParkingLot'] = None
    _lock = threading.Lock()

    def __new__(cls) -> 'ParkingLot':
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.floors: List[ParkingFloor] = []
        self.entry_gates: Dict[str, EntryGate] = {}
        self.exit_gates: Dict[str, ExitGate] = {}

    @classmethod
    def get_instance(cls) -> 'ParkingLot':
        return cls()

    getInstance = get_instance

    def add_floor(self, floor: ParkingFloor) -> None:
        self.floors.append(floor)

    addFloor = add_floor

    def add_entry_gate(self, gate: EntryGate) -> None:
        gate_num = gate.getGateNumber() if hasattr(gate, 'getGateNumber') else gate.gate_number
        self.entry_gates[gate_num] = gate

    addEntryGate = add_entry_gate

    def add_exit_gate(self, gate: ExitGate) -> None:
        gate_num = gate.getGateNumber() if hasattr(gate, 'getGateNumber') else gate.gate_number
        self.exit_gates[gate_num] = gate

    addExitGate = add_exit_gate

    def find_spot(self, vehicle_type: str) -> Optional[object]:
        """Find an available parking spot for the given vehicle type across all floors."""
        for floor in self.floors:
            if hasattr(floor, 'find_available_spot'):
                spot = floor.find_available_spot(vehicle_type)
            elif hasattr(floor, 'findAvailableSpot'):
                spot = floor.findAvailableSpot(vehicle_type)
            else:
                spot = None
            if spot is not None:
                return spot
        return None

    findSpot = find_spot

    def get_floors(self) -> List[ParkingFloor]:
        return self.floors

    getFloors = get_floors
