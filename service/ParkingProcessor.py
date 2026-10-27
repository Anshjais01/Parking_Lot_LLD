'''
package org.nailyourinterview.lld.parking_lot.service;

import org.nailyourinterview.lld.parking_lot.enums.*;
import org.nailyourinterview.lld.parking_lot.factory.*;
import org.nailyourinterview.lld.parking_lot.model.*;
import org.nailyourinterview.lld.parking_lot.strategy.payment.PaymentStrategy;
import org.nailyourinterview.lld.parking_lot.strategy.pricing.PricingStrategy;

import java.time.LocalDateTime;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;

public class ParkingProcessor {
    private final ParkingLot parkingLot;
    private final ConcurrentHashMap<String, Ticket> activeTickets = new ConcurrentHashMap<>();

    public ParkingProcessor(ParkingLot parkingLot) {
        this.parkingLot = parkingLot;
    }

    public Ticket processEntry(Vehicle vehicle) {
        ParkingSpot spot = parkingLot.findSpot(vehicle.getType());
        if (spot == null) throw new RuntimeException("No spot available for " + vehicle.getType());

        ParkingFloor floor = findFloorForSpot(spot);

        Ticket ticket = Ticket.builder()
                .ticketId(UUID.randomUUID().toString())
                .entryTime(LocalDateTime.now())
                .vehicle(vehicle)
                .floorId(floor.getId())
                .spotId(spot.getId())
                .paymentStatus(PaymentStatus.PENDING)
                .build();

        activeTickets.put(ticket.getTicketId(), ticket);
        System.out.println("Vehicle " + vehicle.getNumber() + " parked. Ticket: " + ticket.getTicketId());
        return ticket;
    }

    public double processExit(String ticketId, PricingStrategyType pricingType, PaymentMode paymentMode) {
        Ticket ticket = activeTickets.get(ticketId);
        if (ticket == null) throw new RuntimeException("Invalid ticket: " + ticketId);

        PricingStrategy pricingStrategy = PricingStrategyFactory.get(pricingType);
        LocalDateTime exitTime = LocalDateTime.now();
        double fee = pricingStrategy.calculateFee(ticket.getVehicle().getType(), ticket.getEntryTime(), exitTime);

        PaymentStrategy paymentStrategy = PaymentStrategyFactory.get(paymentMode);
        boolean paid = paymentStrategy.processPayment(ticket, fee);

        if (paid) {
            ticket.setPaymentStatus(PaymentStatus.SUCCESS);
            freeSpot(ticket);
            activeTickets.remove(ticketId);
            System.out.println("Vehicle " + ticket.getVehicle().getNumber() + " exited. Fee: ₹" + fee);
        } else {
            ticket.setPaymentStatus(PaymentStatus.FAILED);
            System.out.println("Payment failed for ticket: " + ticketId);
        }

        return fee;
    }

    private ParkingFloor findFloorForSpot(ParkingSpot spot) {
        for (ParkingFloor floor : parkingLot.getFloors()) {
            if (floor.getSpots().containsValue(spot)) return floor;
        }
        return parkingLot.getFloors().get(0);
    }

    private void freeSpot(Ticket ticket) {
        for (ParkingFloor floor : parkingLot.getFloors()) {
            ParkingSpot spot = floor.getSpots().get(ticket.getSpotId());
            if (spot != null) { spot.free(); break; }
        }
    }
}
'''

import uuid
from datetime import datetime
from typing import Dict, Optional

from .ParkingLot import ParkingLot
from ..model.Ticket import Ticket
from ..model.Vehicle import Vehicle
from ..model.Parkingfloor import ParkingFloor
try:
    from ..enums.PaymentStatus import PaymentStatus
except ImportError:
    from ..enums.PaymentStatus import PaymentaMode as PaymentStatus
from ..factory.PricingStrategyFactory import PricingStrategyFactory
from ..factory.PaymentStrategyFactory import PaymentStrategyFactory


class ParkingProcessor:
    """Orchestrates vehicle entry and exit workflows."""

    def __init__(self, parking_lot: ParkingLot):
        self.parking_lot = parking_lot
        self.active_tickets: Dict[str, Ticket] = {}

    def process_entry(self, vehicle: Vehicle) -> Ticket:
        """Park a vehicle: find a spot, create a ticket, and return it."""
        v_type = vehicle.getType() if hasattr(vehicle, 'getType') else getattr(vehicle, 'type', None)
        spot = self.parking_lot.find_spot(v_type)
        if spot is None:
            raise RuntimeError(f"No spot available for {v_type}")

        floor = self._find_floor_for_spot(spot)
        floor_id = floor.id if floor and hasattr(floor, 'id') else "F-0"
        spot_id = spot.id if hasattr(spot, 'id') else getattr(spot, 'getId', lambda: "S-0")()

        ticket = Ticket(
            ticket_id=str(uuid.uuid4()),
            entry_time=datetime.now(),
            vehicle=vehicle,
            floor_id=floor_id,
            spot_id=spot_id,
        )

        self.active_tickets[ticket.ticket_id] = ticket
        v_num = vehicle.getNumber() if hasattr(vehicle, 'getNumber') else getattr(vehicle, 'number', '')
        print(f"Vehicle {v_num} parked. Ticket: {ticket.ticket_id}")
        return ticket

    processEntry = process_entry

    def process_exit(self, ticket_id: str, pricing_type: str, payment_mode: str) -> float:
        """Process vehicle exit: calculate fee, process payment, free the spot."""
        ticket = self.active_tickets.get(ticket_id)
        if ticket is None:
            raise RuntimeError(f"Invalid ticket: {ticket_id}")

        pricing_strategy = PricingStrategyFactory.get(pricing_type)
        exit_time = datetime.now()
        v_type = ticket.vehicle.getType() if hasattr(ticket.vehicle, 'getType') else getattr(ticket.vehicle, 'type', None)
        entry_time = ticket.entry_time if hasattr(ticket, 'entry_time') else ticket.getEntryTime()

        if hasattr(pricing_strategy, 'calculate_fee'):
            fee = pricing_strategy.calculate_fee(v_type, entry_time, exit_time)
        else:
            fee = pricing_strategy.calculateFee(v_type, entry_time, exit_time)

        payment_strategy = PaymentStrategyFactory.get(payment_mode)
        paid = payment_strategy.processPayment(ticket, fee)

        v_num = ticket.vehicle.getNumber() if hasattr(ticket.vehicle, 'getNumber') else getattr(ticket.vehicle, 'number', '')
        if paid:
            ticket.payment_status = PaymentStatus.SUCCESS
            self._free_spot(ticket)
            del self.active_tickets[ticket_id]
            print(f"Vehicle {v_num} exited. Fee: ₹{fee}")
        else:
            ticket.payment_status = PaymentStatus.FAILED
            print(f"Payment failed for ticket: {ticket_id}")

        return fee

    processExit = process_exit

    def _find_floor_for_spot(self, spot) -> Optional[ParkingFloor]:
        """Find which floor a given spot belongs to."""
        for floor in self.parking_lot.get_floors():
            spots = floor.spots if hasattr(floor, 'spots') else getattr(floor, 'getSpots', lambda: {})()
            if spot in spots.values():
                return floor
        floors = self.parking_lot.get_floors()
        return floors[0] if floors else None

    def _free_spot(self, ticket: Ticket) -> None:
        """Release the parking spot associated with a ticket."""
        spot_id = ticket.spot_id if hasattr(ticket, 'spot_id') else ticket.getSpotId()
        for floor in self.parking_lot.get_floors():
            spots = floor.spots if hasattr(floor, 'spots') else getattr(floor, 'getSpots', lambda: {})()
            spot = spots.get(spot_id)
            if spot is not None:
                if hasattr(spot, 'free'):
                    spot.free()
                elif hasattr(spot, 'occupied'):
                    spot.occupied = False
                break
