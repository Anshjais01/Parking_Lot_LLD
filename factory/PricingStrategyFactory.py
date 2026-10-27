'''
package org.nailyourinterview.lld.parking_lot.factory;

import org.nailyourinterview.lld.parking_lot.enums.PricingStrategyType;
import org.nailyourinterview.lld.parking_lot.strategy.pricing.*;

public class PricingStrategyFactory {
    public static PricingStrategy get(PricingStrategyType type) {
        return switch (type) {
            case TIME_BASED -> new TimeBasedPricing();
            case EVENT_BASED -> new EventBasedPricing();
        };
    }
}
'''

from ..enums.PricingStrategyType import PriceStrategyType
from ..strategy.pricing.TimeBasedPricing import TimeBasedPricing
from ..strategy.pricing.EventBasedPricing import EventBasedPricing


class PricingStrategyFactory:
    @staticmethod
    def get(pricing_type: str):
        match pricing_type:
            case PriceStrategyType.TIME_BASED:
                return TimeBasedPricing()
            case PriceStrategyType.EVENT_BASED:
                return EventBasedPricing()
            case _:
                raise ValueError(f"Unknown pricing strategy type: {pricing_type}")
