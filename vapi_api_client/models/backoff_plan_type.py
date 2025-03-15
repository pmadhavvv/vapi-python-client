from enum import Enum


class BackoffPlanType(str, Enum):
    EXPONENTIAL = "exponential"
    FIXED = "fixed"

    def __str__(self) -> str:
        return str(self.value)
