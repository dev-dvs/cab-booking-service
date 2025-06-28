from enums.booking_status import BookingStatus
from model.booking import Booking
from service.driver_service import DriverService
from service.location_service import LocationService
from service.user_service import UserService
from utils.utils import compute_distance


class BookingService:
    booking_map: {int, Booking}
    user_booking_map: {str, list[int]}
    driver_booking_map: {str, list[int]}

    def __init__(self, user_service: UserService, driver_service: DriverService, location_service: LocationService):
        self.booking_map = {}
        self.user_booking_map = {}
        self.driver_booking_map = {}

        self.user_service = user_service
        self.driver_service = driver_service
        self.location_service = location_service

    def find_rides(self, username: str, source_coordinates: tuple[float, float], destination_coordinates: tuple[float, float]) -> list[str]:
        drivers = self.driver_service.get_available_drivers()
        if not drivers:
            return []

        nereby_rides = []

        for driver in drivers:
            driver_location = self.location_service.get_user_location("driver:" + driver)
            if not driver_location:
                continue

            if compute_distance(source_coordinates, driver_location) <= 5:
                nereby_rides.append(self.driver_service.get_driver_by_name(driver))

        booking: Booking = Booking(source_coordinates, destination_coordinates, compute_distance(source_coordinates, destination_coordinates) * 1,
                                   BookingStatus.PENDING)
        self.booking_map[booking.id] = booking

        if username not in self.driver_booking_map:
            self.user_booking_map[username] = []

        self.user_booking_map[username].append(booking.id)

        return [driver.name for driver in nereby_rides]

    def choose_ride(self, username: str, driver_name: str) -> Booking:
        if not self.user_service.get_user_by_username(username):
            raise ValueError(f"User '{username}' is not registered.")

        driver = self.driver_service.get_driver_by_name(driver_name)
        if not driver:
            raise ValueError(f"Driver '{driver_name}' does not exist.")

        if driver_name not in self.driver_booking_map:
            self.driver_booking_map[driver_name] = []

        for booking_id in self.user_booking_map.get(username, []):
            booking = self.booking_map.get(booking_id)
            if booking and booking.status == BookingStatus.PENDING:
                booking.status = BookingStatus.CONFIRMED
                self.driver_booking_map[driver_name].append(booking.id)
                return booking

        raise ValueError(f"No pending bookings found for user '{username}'.")

    def calculate_bill(self, username: str):
        if not self.user_service.get_user_by_username(username):
            raise ValueError(f"User '{username}' is not registered.")

        for booking_id in self.user_booking_map.get(username, []):
            booking: Booking = self.booking_map.get(booking_id)
            if booking and booking.status == BookingStatus.CONFIRMED:
                booking.status = BookingStatus.COMPLETED
                return booking.cost

        raise ValueError(f"No confirmed bookings found for user '{username}'.")

    def get_total_earnings(self, driver_name: str):
        total_earnings = 0

        for booking_id in self.driver_booking_map.get(driver_name, []):
            total_earnings += self.booking_map.get(booking_id).cost

        return total_earnings
