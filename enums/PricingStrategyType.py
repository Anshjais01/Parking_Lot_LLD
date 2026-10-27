"""
package org.nailyourinterview.lld.parking_lot.enums;

public enum PricingStrategyType {
    TIME_BASED, EVENT_BASED
}
"""
from enum import Enum

class PriceStrategyType:
    TIME_BASED="TIME_BASED"
    EVENT_BASED="EVENT_BASED"