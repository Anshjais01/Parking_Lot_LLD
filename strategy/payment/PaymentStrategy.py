'''
package org.nailyourinterview.lld.parking_lot.strategy.payment;

import org.nailyourinterview.lld.parking_lot.model.Ticket;

public interface PaymentStrategy {
    boolean processPayment(Ticket ticket, double amount);
}
'''


from abc import ABC, abstractmethod
from ...model.Ticket import Ticket


class PaymentStrategy(ABC):
    @abstractmethod
    def processPayment(self, ticket: Ticket, amount: float) -> bool:
        pass