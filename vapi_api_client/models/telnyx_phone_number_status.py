from enum import Enum


class TelnyxPhoneNumberStatus(str, Enum):
    ACTIVATING = "activating"
    ACTIVE = "active"
    BLOCKED = "blocked"

    def __str__(self) -> str:
        return str(self.value)
