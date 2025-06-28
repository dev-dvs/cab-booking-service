class User:
    def __init__(self, username: str, email: str, phone: str):
        self.username = username
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}')"
