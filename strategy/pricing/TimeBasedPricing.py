'''
package org.nailyourinterview.lld.parking_lot.strategy.pricing;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.temporal.ChronoUnit;

public class TimeBasedPricing implements PricingStrategy {
    // Peak period hours (e.g., 8:00 to 17:00)
    private static final LocalTime PEAK_START = LocalTime.of(8, 0);
    private static final LocalTime PEAK_END = LocalTime.of(17, 0);

    private boolean isPeak(LocalTime time) {
        return !time.isBefore(PEAK_START) && !time.isAfter(PEAK_END);
    }

    @Override
    public double calculateFee(VehicleType type, LocalDateTime entryTime, LocalDateTime exitTime) {
        if (exitTime.isBefore(entryTime)) throw new IllegalArgumentException("Exit time before entry time");

        long durationMinutes = Duration.between(entryTime, exitTime).toMinutes();
        long totalHours = (long) Math.ceil(durationMinutes / 60.0);

        // Count peak hours and non-peak hours by iterating hour by hour
        int peakHours = 0;
        int nonPeakHours = 0;

        LocalDateTime cursor = entryTime.truncatedTo(ChronoUnit.HOURS);
        // If entry time has minutes, consider first hour partially occupied, count as 1 hour anyway (already rounded)
        for (int i = 0; i < totalHours; i++) {
            LocalTime hourStart = cursor.toLocalTime();
            if (isPeak(hourStart)) peakHours++;
            else nonPeakHours++;
            cursor = cursor.plusHours(1);
        }

        double peakRate = switch (type) {
            case CAR -> 30.0;
            case BIKE -> 15.0;
            case TRUCK -> 50.0;
        };

        double nonPeakRate = switch (type) {
            case CAR -> 20.0;
            case BIKE -> 10.0;
            case TRUCK -> 30.0;
        };

        return peakHours * peakRate + nonPeakHours * nonPeakRate;
    }
}
'''

import math
from datetime import datetime, time, timedelta

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


class TimeBasedPricing(PricingStrategy):
    """Time-based pricing strategy with peak (08:00–17:00) and non-peak hourly rates."""

    PEAK_START = time(8, 0)
    PEAK_END = time(17, 0)

    PEAK_RATES = {
        "CAR": 30.0,
        "BIKE": 15.0,
        "TRUCK": 50.0,
    }

    NON_PEAK_RATES = {
        "CAR": 20.0,
        "BIKE": 10.0,
        "TRUCK": 30.0,
    }

    @staticmethod
    def is_peak(t: time) -> bool:
        """Check if a time falls within peak hours (08:00 to 17:00 inclusive)."""
        return TimeBasedPricing.PEAK_START <= t <= TimeBasedPricing.PEAK_END

    isPeak = is_peak
    _is_peak = is_peak

    def calculate_fee(self, vehicle_type, entry_time, exit_time) -> float:
        """
        Calculate total parking fee based on hourly peak and non-peak rates.
        Accepts datetime objects or date strings parsed via DateTimeParser.
        """
        # Convert strings to datetime if needed
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

        # Duration in whole minutes matching Java Duration.between(...).toMinutes()
        duration_minutes = int((exit_time - entry_time).total_seconds() // 60)
        total_hours = max(1, math.ceil(duration_minutes / 60.0))

        # Count peak hours and non-peak hours by iterating hour by hour
        peak_hours = 0
        non_peak_hours = 0
        cursor = entry_time.replace(minute=0, second=0, microsecond=0)

        for _ in range(int(total_hours)):
            hour_start = cursor.time()
            if self.is_peak(hour_start):
                peak_hours += 1
            else:
                non_peak_hours += 1
            cursor += timedelta(hours=1)

        # Normalize vehicle_type (supports Enum, string, or Vehicle instances)
        if hasattr(vehicle_type, "getType"):
            vehicle_type = vehicle_type.getType()
        if hasattr(vehicle_type, "value"):
            vehicle_type = vehicle_type.value
        if isinstance(vehicle_type, str):
            v_key = vehicle_type.upper().strip()
        else:
            v_key = str(vehicle_type).upper()

        if v_key not in self.PEAK_RATES:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

        peak_rate = self.PEAK_RATES[v_key]
        non_peak_rate = self.NON_PEAK_RATES[v_key]

        return peak_hours * peak_rate + non_peak_hours * non_peak_rate

    calculateFee = calculate_fee
