from enum import Enum


class TwilioPhoneNumberStatus(str, Enum):
    ACTIVATING = "activating"
    ACTIVE = "active"
    BLOCKED = "blocked"

    def __str__(self) -> str:
        return str(self.value)
