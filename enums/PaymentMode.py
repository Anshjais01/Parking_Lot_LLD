"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum PaymentMode {
    CASH, UPI, CARD
}
"""
from enum import Enum

class PaymentMode:
    UPI="Upi"
    CASH="Cash"
    CARD="Card"