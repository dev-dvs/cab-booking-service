class LocationService:
    user_location_map: {str, tuple[float, float]}

    def __init__(self):
        self.user_location_map = {}

    def update_user_location(self, username: str, coordinates: tuple[float, float]):
        if not isinstance(coordinates, tuple) or len(coordinates) != 2:
            raise ValueError("Coordinates must be a tuple of (latitude, longitude).")

        self.user_location_map[username] = coordinates

    def get_user_location(self, username: str) -> tuple[float, float]:
        if username not in self.user_location_map:
            raise ValueError(f"No location found for user '{username}'.")

        return self.user_location_map[username]
