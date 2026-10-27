'''
package org.nailyourinterview.lld.parking_lot.strategy.payment;

import org.nailyourinterview.lld.parking_lot.model.Ticket;

public interface PaymentStrategy {
    boolean processPayment(Ticket ticket, double amount);
}
'''
from .PaymentStrategy import PaymentStrategy
from ...model.Ticket import Ticket


class UpiPayment(PaymentStrategy):
    def processPayment(self, ticket: Ticket, amount: float) -> bool:
        print(f"Paid ₹{amount} for ticket {ticket.getTicketId()} via UPI.")
        return True