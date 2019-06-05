"""Model a busy road.

   * Start with a single road and a variety of vehicles (car, lorry, bus) that
   can travel along it in both directions
   * Introduce a single track bridge in the middle. Manage traffic flow with a
   light system
   * If you get this far, optimize for different times of the day, e.g. assume
   rush hour traffic flows in the opposite direction at each end of the day
"""

import abc


class Vehicle(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def length(self):
        return NotImplementedError

    @abc.abstractmethod
    def speed(self):
        return NotImplementedError


class Car(Vehicle):
    def length(self):
        return 3

    def speed(self):
        return 13


class Bus(Vehicle):
    def length(self):
        return 10

    def speed(self):
        return 10


class Lorry(Vehicle):
    def length(self):
        return 8

    def speed(self):
        return 7


class TrafficSource:

    def __init__(self):
        self._vehicles = (Car, Bus, Lorry)
        self._next_vehicle_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        vehicle = self._vehicles[self._next_vehicle_index]()
        self._next_vehicle_index += 1
        self._next_vehicle_index %= len(self._vehicles)
        return vehicle


class TrafficSink:

    def __init__(self):
        self.total = 0

    def _consume_one_vehicle(self, vehicle):
        assert(isinstance(vehicle, Vehicle))
        del vehicle
        return 1

    def consume(self, vehicle):
        total = 0
        if isinstance(vehicle, list):
            for v in vehicle:
                total += self._consume_one_vehicle(v)
        else:
            total += self._consume_one_vehicle(vehicle)

        self.total += total
        return total


class Road:
    def __init__(self, length, src, sink):
        self.length = length
        self._src = src
        self._sink = sink

    def simulate(self, period):
        for i in range(period):
            self._sink.consume(next(self._src))
