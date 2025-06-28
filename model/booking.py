import threading

from enums.booking_status import BookingStatus


class Booking:
    auto_increment_id: int = 0
    lock = threading.Lock()

    def __init__(self, source_coordinates: tuple[float, float], destination_coordinates: tuple[float, float], cost: float, status: BookingStatus):
        with self.lock:
            self.auto_increment_id += 1
            self.id = self.auto_increment_id

        self.source_coordinates = source_coordinates
        self.destination_coordinates = destination_coordinates
        self.cost = cost
        self.status = status
