from enum import Enum


class AIEdgeConditionType(str, Enum):
    AI = "ai"

    def __str__(self) -> str:
        return str(self.value)
