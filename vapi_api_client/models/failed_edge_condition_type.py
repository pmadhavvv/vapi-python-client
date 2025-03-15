from enum import Enum


class FailedEdgeConditionType(str, Enum):
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
