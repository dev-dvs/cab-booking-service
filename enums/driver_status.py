from enum import Enum


class DriverStatus(Enum):
    """
    Enum for driver status.
    """
    UNKNOWN = 0
    ONLINE = 1
    OFFLINE = 2
    BUSY = 3
    IDLE = 4

    def __str__(self):
        return self.name.lower()

    @classmethod
    def from_string(cls, status_str: str):
        """
        Convert a string to a DriverStatus enum.
        """
        try:
            return cls[status_str.upper()]
        except KeyError:
            return cls.UNKNOWN
