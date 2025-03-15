from enum import Enum


class AnalyticsOperationOperation(str, Enum):
    AVG = "avg"
    COUNT = "count"
    HISTORY = "history"
    MAX = "max"
    MIN = "min"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
