"""
package org.nailyourinterview.lld.parking_lot.factory;

import org.nailyourinterview.lld.parking_lot.enums.PaymentMode;
import org.nailyourinterview.lld.parking_lot.strategy.payment.*;

public class PaymentStrategyFactory {
    public static PaymentStrategy get(PaymentMode mode) {
        return switch (mode) {
            case CASH -> new CashPayment();
            case UPI -> new UpiPayment();
            case CARD -> new CardPayment();
        };
    }
}
"""

from ..enums.PaymentMode import PaymentMode
from ..strategy.payment.PaymentStrategy import PaymentStrategy
from ..strategy.payment.CashPayment import CashPayment
from ..strategy.payment.UpiPayment import UpiPayment
from ..strategy.payment.CardPayment import CardPayment
from ..strategy.payment.NetBankingPayment import NetBankingPayment


class PaymentStrategyFactory:
    @staticmethod
    def get(mode: PaymentMode) -> PaymentStrategy:
        match mode:
            case PaymentMode.CASH:
                return CashPayment()
            case PaymentMode.UPI:
                return UpiPayment()
            case PaymentMode.CARD:
                return CardPayment()
            case PaymentMode.NETBANKING:
                return NetBankingPayment()