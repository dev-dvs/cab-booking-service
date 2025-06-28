# Start: 11:30
# Code complete: 12:30
# Working demo: 12:45

from enums.driver_status import DriverStatus
from service.booking_service import BookingService
from service.driver_service import DriverService
from service.location_service import LocationService
from service.user_service import UserService


def main():
    location_service = LocationService()
    user_service = UserService(location_service)
    driver_service = DriverService(location_service)
    booking_service = BookingService(user_service, driver_service, location_service)

    user_service.add_user("Abhishek", "Abhishek@gmail.com", "23")
    user_service.update_user_location("Abhishek", (0, 0))

    user_service.add_user("Rahul", "Rahul@gmail.com", "25")
    user_service.update_user_location("Rahul", (10, 0))

    user_service.add_user("Nandini", "Nandini@gmail.com", "23")
    user_service.update_user_location("Nandini", (15, 6))

    driver_service.add_driver("Driver1", 22, "Swift", "KA - 01 - 12345")
    driver_service.update_driver_location("Driver1", (10, 1))
    driver_service.add_driver("Driver2", 29, "Swift", "KA - 01 - 12345")
    driver_service.update_driver_location("Driver2", (11, 10))
    driver_service.add_driver("Driver3", 24, "Swift", "KA - 01 - 12345")
    driver_service.update_driver_location("Driver3", (5, 3))

    print(booking_service.find_rides("Abhishek", (0, 0), (20, 1)))
    print(booking_service.find_rides("Rahul", (10, 0), (15, 3)))

    print(booking_service.choose_ride("Rahul", "Driver1"))
    print(booking_service.calculate_bill("Rahul"))

    print(driver_service.change_driver_status("Driver1", DriverStatus.OFFLINE))
    print(booking_service.find_rides("Nandini", (10, 1), (20, 4)))

    print(driver_service.change_driver_status("Driver1", DriverStatus.ONLINE))
    print(booking_service.find_rides("Nandini", (10, 1), (20, 4)))


if __name__ == '__main__':
    main()
