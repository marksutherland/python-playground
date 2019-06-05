import bridge
import pytest


@pytest.fixture
def src():
    return bridge.TrafficSource()


@pytest.fixture
def sink():
    return bridge.TrafficSink()


class TestTrafficSource:

    def test_source_issues_traffic(self, src):
        vehicle = next(src)
        assert isinstance(vehicle, bridge.Vehicle)

    def source_issues_vehicle(self, src, vehicle_type):
        tries = 10
        for i in range(tries):
            try:
                assert isinstance(next(src), vehicle_type)
                return
            except AssertionError:
                pass
        assert False, f'No {vehicle_type} seen after {tries} tries'

    def test_source_issues_cars(self, src):
        for vehicle in (bridge.Car, bridge.Bus, bridge.Lorry):
            self.source_issues_vehicle(src, vehicle)

    def test_sink_consumes_traffic(self, src, sink):
        result = sink.consume(next(src))
        assert result == 1

    def test_sink_consumes_lots_of_traffic(self, src, sink):
        total = 10
        result = sink.consume([next(src) for i in range(total)])
        assert result == total
        assert sink.total == total

    def test_road_carries_traffic(self, src, sink):
        road = bridge.Road(100, src, sink)
        road.simulate(10)
        sink.total
        assert sink.total > 0
