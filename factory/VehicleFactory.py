'''
package org.nailyourinterview.lld.parking_lot.factory;

import org.nailyourinterview.lld.parking_lot.enums.VehicleType;
import org.nailyourinterview.lld.parking_lot.model.*;

public class VehicleFactory {
    public static Vehicle create(String number, VehicleType type) {
        return switch (type) {
            case CAR -> new Car(number);
            case BIKE -> new Bike(number);
            case TRUCK -> new Truck(number);
        };
    }
}
'''

from ..enums.VehicleType import VehicleType
from ..model.Car import Car
from ..model.Bike import Bike
from ..model.Truck import Truck


class VehicleFactory:
    @staticmethod
    def create(number: str, vehicle_type: str):
        match vehicle_type:
            case VehicleType.CAR:
                return Car(number)
            case VehicleType.BIKE:
                return Bike(number)
            case VehicleType.TRUCK:
                return Truck(number)
            case _:
                raise ValueError(f"Unknown vehicle type: {vehicle_type}")
