from enum import Enum


class SubscriptionStatus(str, Enum):
    ACTIVE = "active"
    FROZEN = "frozen"

    def __str__(self) -> str:
        return str(self.value)
