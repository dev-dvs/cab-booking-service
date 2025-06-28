from enums.driver_status import DriverStatus
from model.driver import Driver
from service.location_service import LocationService


class DriverService:
    driver_map: {str, Driver}
    driver_current_status: {str, int}  # Maps driver name to their current status

    def __init__(self, location_service: LocationService):
        self.driver_map = {}
        self.driver_current_status = {}
        self.location_service = location_service

    def get_driver_by_name(self, name):
        return self.driver_map.get(name, None)

    def add_driver(self, name: str, age: int, car_model: str, car_number: str):
        existing_driver = self.get_driver_by_name(name)

        if existing_driver:
            raise ValueError(f"Driver with username '{name}' already exists.")

        new_driver = Driver(name, age, car_model, car_number)
        self.driver_map[name] = new_driver
        self.driver_current_status[name] = DriverStatus.ONLINE.value

    def update_driver_location(self, driver_name: str, coordinates: tuple[float, float]):
        driver = self.get_driver_by_name(driver_name)
        if not driver:
            raise ValueError(f"Driver with name '{driver_name}' does not exist.")
        return self.location_service.update_user_location("driver:" + driver_name, coordinates)

    def change_driver_status(self, driver_name: str, status: DriverStatus):
        driver = self.get_driver_by_name(driver_name)
        if not driver:
            raise ValueError(f"Driver with name '{driver_name}' does not exist.")
        self.driver_current_status[driver_name] = status.value
        return True

    def get_available_drivers(self):
        available_drivers = []
        for driver_name, status in self.driver_current_status.items():
            if status == DriverStatus.ONLINE.value:
                available_drivers.append(driver_name)
        return available_drivers
