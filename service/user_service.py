from model.user import User
from service.location_service import LocationService


class UserService:
    users: {str, User}

    def __init__(self, location_service: LocationService):
        self.users = {}
        self.location_service = location_service

    def get_user_by_username(self, username):
        return self.users.get(username, None)

    def add_user(self, username: str, email: str, phone: str):
        existing_user = self.get_user_by_username(username)

        if existing_user:
            raise ValueError(f"User with username '{username}' already exists.")
        new_user = User(username, email, phone)
        self.users[username] = new_user

    def update_user(self, username: str, email: str, phone: str):
        existing_user = self.get_user_by_username(username)

        if not existing_user:
            raise ValueError(f"User with username '{username}' does not exist.")

        if email:
            existing_user.email = email

        if phone:
            existing_user.phone = phone

        return existing_user

    def update_user_location(self, username: str, coordinates: tuple[float, float]):
        existing_user = self.get_user_by_username(username)

        if not existing_user:
            raise ValueError(f"User with username '{username}' does not exist.")

        return self.location_service.update_user_location("user:" + username, coordinates)
