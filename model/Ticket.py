'''
package org.nailyourinterview.lld.parking_lot.model;

import lombok.Builder;
import lombok.Data;
import org.nailyourinterview.lld.parking_lot.enums.PaymentStatus;

import java.time.LocalDateTime;

@Data
@Builder
public class Ticket {
    private String ticketId;
    private LocalDateTime entryTime;
    private Vehicle vehicle;
    private String floorId;
    private String spotId;
    private PaymentStatus paymentStatus = PaymentStatus.PENDING;
}'''

from .Vehicle import Vehicle
from ..enums.PaymentStatus import PaymentStatus
from datetime import datetime

class Ticket:
    def __init__(self, ticket_id: str, entry_time: datetime, vehicle: Vehicle, floor_id: str, spot_id: str):
        self.ticket_id = ticket_id
        self.entry_time = entry_time
        self.vehicle = vehicle
        self.floor_id = floor_id
        self.spot_id = spot_id
        self.payment_status = PaymentStatus.PENDING