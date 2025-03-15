from enum import Enum


class AnalyticsQueryTable(str, Enum):
    CALL = "call"
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
