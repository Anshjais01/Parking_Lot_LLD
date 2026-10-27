from .PaymentStrategy import PaymentStrategy
from ...model.Ticket import Ticket


class NetBankingPayment(PaymentStrategy):
    def processPayment(self, ticket: Ticket, amount: float) -> bool:
        print(f"Paid ₹{amount} for ticket {ticket.getTicketId()} via NetBanking.")
        return True

