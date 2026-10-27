'''
package org.nailyourinterview.lld.parking_lot;

import org.nailyourinterview.lld.parking_lot.enums.*;
import org.nailyourinterview.lld.parking_lot.factory.VehicleFactory;
import org.nailyourinterview.lld.parking_lot.model.*;
import org.nailyourinterview.lld.parking_lot.service.*;

public class Main {
    public static void main(String[] args) {
        // 1. Build the parking lot
        ParkingLot lot = ParkingLot.getInstance();

        ParkingFloor floor1 = new ParkingFloor("F1");
        floor1.addSpot(new ParkingSpot("S1", VehicleType.CAR));
        floor1.addSpot(new ParkingSpot("S2", VehicleType.BIKE));
        floor1.addSpot(new ParkingSpot("S3", VehicleType.TRUCK));

        ParkingFloor floor2 = new ParkingFloor("F2");
        floor2.addSpot(new ParkingSpot("S4", VehicleType.CAR));
        floor2.addSpot(new ParkingSpot("S5", VehicleType.BIKE));

        lot.addFloor(floor1);
        lot.addFloor(floor2);

        lot.addEntryGate(new EntryGate("E1"));
        lot.addExitGate(new ExitGate("X1"));

        // 2. Create the processor
        ParkingProcessor processor = new ParkingProcessor(lot);

        // 3. Park vehicles
        Vehicle car = VehicleFactory.create("KA-01-1234", VehicleType.CAR);
        Vehicle bike = VehicleFactory.create("KA-02-5678", VehicleType.BIKE);
        Vehicle truck = VehicleFactory.create("KA-03-9999", VehicleType.TRUCK);

        Ticket t1 = processor.processEntry(car);
        Ticket t2 = processor.processEntry(bike);
        Ticket t3 = processor.processEntry(truck);

        // 4. Exit vehicles
        processor.processExit(t1.getTicketId(), PricingStrategyType.TIME_BASED, PaymentMode.CASH);
        processor.processExit(t2.getTicketId(), PricingStrategyType.EVENT_BASED, PaymentMode.UPI);
        processor.processExit(t3.getTicketId(), PricingStrategyType.TIME_BASED, PaymentMode.CARD);
    }
}
'''

import sys
import os
import importlib

# Configure console encoding for Unicode support (e.g. ₹ symbol on Windows)
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
if hasattr(sys.stderr, 'reconfigure'):
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Dynamically locate the project root directory
_curr = os.path.dirname(os.path.abspath(__file__))
while _curr and not (os.path.exists(os.path.join(_curr, 'model')) and os.path.exists(os.path.join(_curr, 'service'))):
    _parent = os.path.dirname(_curr)
    if _parent == _curr:
        break
    _curr = _parent

_project_root = _curr
_parent_dir = os.path.dirname(_project_root)
_pkg_name = os.path.basename(_project_root)

for _d in [_parent_dir, _project_root]:
    if _d not in sys.path:
        sys.path.insert(0, _d)

# Robust imports: support both package-relative and package-absolute modes
try:
    from ..enums.VehicleType import VehicleType
    from ..enums.PricingStrategyType import PriceStrategyType
    from ..enums.PaymentMode import PaymentMode
    from ..model.Parkingfloor import ParkingFloor
    from ..model.Parkingspot import ParkingSpot
    from ..model.EntryGate import EntryGate
    from ..model.ExitGate import ExitGate
    from ..factory.VehicleFactory import VehicleFactory
    from ..service.ParkingLot import ParkingLot
    from ..service.ParkingProcessor import ParkingProcessor
    from .DateTimeParser import DateTimeParser
except (ImportError, ValueError):
    VehicleType = importlib.import_module(f"{_pkg_name}.enums.VehicleType").VehicleType
    PriceStrategyType = importlib.import_module(f"{_pkg_name}.enums.PricingStrategyType").PriceStrategyType
    PaymentMode = importlib.import_module(f"{_pkg_name}.enums.PaymentMode").PaymentMode
    ParkingFloor = importlib.import_module(f"{_pkg_name}.model.Parkingfloor").ParkingFloor
    ParkingSpot = importlib.import_module(f"{_pkg_name}.model.Parkingspot").ParkingSpot
    EntryGate = importlib.import_module(f"{_pkg_name}.model.EntryGate").EntryGate
    ExitGate = importlib.import_module(f"{_pkg_name}.model.ExitGate").ExitGate
    VehicleFactory = importlib.import_module(f"{_pkg_name}.factory.VehicleFactory").VehicleFactory
    ParkingLot = importlib.import_module(f"{_pkg_name}.service.ParkingLot").ParkingLot
    ParkingProcessor = importlib.import_module(f"{_pkg_name}.service.ParkingProcessor").ParkingProcessor
    DateTimeParser = importlib.import_module(f"{_pkg_name}.utils.DateTimeParser").DateTimeParser


def main():
    # ── 1. Build the parking lot ──────────────────────────────────
    lot = ParkingLot.get_instance()

    floor1 = ParkingFloor("F1")
    floor1.add_spot(ParkingSpot("S1", VehicleType.CAR))
    floor1.add_spot(ParkingSpot("S2", VehicleType.BIKE))
    floor1.add_spot(ParkingSpot("S3", VehicleType.TRUCK))

    floor2 = ParkingFloor("F2")
    floor2.add_spot(ParkingSpot("S4", VehicleType.CAR))
    floor2.add_spot(ParkingSpot("S5", VehicleType.BIKE))

    lot.add_floor(floor1)
    lot.add_floor(floor2)

    lot.add_entry_gate(EntryGate("E1"))
    lot.add_exit_gate(ExitGate("X1"))

    # ── 2. Create the processor ───────────────────────────────────
    processor = ParkingProcessor(lot)

    # ── 3. Park vehicles ──────────────────────────────────────────
    car = VehicleFactory.create("KA-01-1234", VehicleType.CAR)
    bike = VehicleFactory.create("KA-02-5678", VehicleType.BIKE)
    truck = VehicleFactory.create("KA-03-9999", VehicleType.TRUCK)

    t1 = processor.process_entry(car)
    t2 = processor.process_entry(bike)
    t3 = processor.process_entry(truck)

    # ── 4. Exit vehicles ──────────────────────────────────────────
    processor.process_exit(t1.ticket_id, PriceStrategyType.TIME_BASED, PaymentMode.CASH)
    processor.process_exit(t2.ticket_id, PriceStrategyType.EVENT_BASED, PaymentMode.UPI)
    processor.process_exit(t3.ticket_id, PriceStrategyType.TIME_BASED, PaymentMode.CARD)


if __name__ == "__main__":
    main()

