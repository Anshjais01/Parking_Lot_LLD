'''
package org.nailyourinterview.lld.parking_lot.strategy.pricing;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;

import java.time.LocalDateTime;

public interface PricingStrategy {
    double calculateFee(VehicleType type, LocalDateTime entryTime, LocalDateTime exitTime);
}
'''

from abc import ABC, abstractmethod
from datetime import datetime


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, vehicle_type: str, entry_time: datetime, exit_time: datetime) -> float:
        pass

    def calculateFee(self, vehicle_type: str, entry_time: datetime, exit_time: datetime) -> float:
        return self.calculate_fee(vehicle_type, entry_time, exit_time)
