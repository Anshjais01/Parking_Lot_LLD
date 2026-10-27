'''
package org.nailyourinterview.lld.parking_lot.strategy.pricing;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.time.Duration;
import java.time.LocalDateTime;
import java.util.Map;

public class EventBasedPricing implements PricingStrategy {
    // Event pricing: Higher per-hour rates
    private static final Map<VehicleType, Double> EVENT_HOURLY_RATES = Map.of(
            VehicleType.CAR, 50.0,
            VehicleType.BIKE, 30.0,
            VehicleType.TRUCK, 70.0
    );

    @Override
    public double calculateFee(VehicleType type, LocalDateTime entryTime, LocalDateTime exitTime) {
        long durationMinutes = Duration.between(entryTime, exitTime).toMinutes();
        long hours = (long) Math.ceil(durationMinutes / 60.0);

        double ratePerHour = EVENT_HOURLY_RATES.getOrDefault(type, 0.0);
        return ratePerHour * hours;
    }
}
'''

import math
from datetime import datetime

# Robust imports to work both as package submodule and standalone
try:
    from .PricingStrategy import PricingStrategy
except (ImportError, ValueError):
    from strategy.pricing.PricingStrategy import PricingStrategy

try:
    from ...enums.VehicleType import VehicleType
except (ImportError, ValueError):
    try:
        from enums.VehicleType import VehicleType
    except (ImportError, ValueError):
        import importlib
        VehicleType = importlib.import_module("Parking_Lot_LLD.enums.VehicleType").VehicleType

try:
    from ...utils.DateTimeParser import DateTimeParser
except (ImportError, ValueError):
    try:
        from utils.DateTimeParser import DateTimeParser
    except (ImportError, ValueError):
        try:
            import importlib
            DateTimeParser = importlib.import_module("Parking_Lot_LLD.utils.DateTimeParser").DateTimeParser
        except (ImportError, ValueError):
            DateTimeParser = None


class EventBasedPricing(PricingStrategy):
    """Event-based pricing with flat higher hourly rates."""

    EVENT_HOURLY_RATES = {
        "CAR": 50.0,
        "BIKE": 30.0,
        "TRUCK": 70.0,
    }

    def calculate_fee(self, vehicle_type, entry_time, exit_time) -> float:
        if isinstance(entry_time, str):
            if DateTimeParser:
                entry_time = DateTimeParser.parse(entry_time)
            else:
                entry_time = datetime.fromisoformat(entry_time.strip())

        if isinstance(exit_time, str):
            if DateTimeParser:
                exit_time = DateTimeParser.parse(exit_time)
            else:
                exit_time = datetime.fromisoformat(exit_time.strip())

        if exit_time < entry_time:
            raise ValueError("Exit time before entry time")

        duration_minutes = int((exit_time - entry_time).total_seconds() // 60)
        hours = max(1, math.ceil(duration_minutes / 60.0))

        # Normalize vehicle_type
        if hasattr(vehicle_type, "getType"):
            vehicle_type = vehicle_type.getType()
        if hasattr(vehicle_type, "value"):
            vehicle_type = vehicle_type.value
        if isinstance(vehicle_type, str):
            v_key = vehicle_type.upper().strip()
        else:
            v_key = str(vehicle_type).upper()

        rate_per_hour = self.EVENT_HOURLY_RATES.get(v_key, 0.0)
        return rate_per_hour * hours

    calculateFee = calculate_fee
