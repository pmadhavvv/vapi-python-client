from enum import Enum


class LogicEdgeConditionType(str, Enum):
    LOGIC = "logic"

    def __str__(self) -> str:
        return str(self.value)
