from enum import Enum


class FunctionToolWithToolCallType(str, Enum):
    FUNCTION = "function"

    def __str__(self) -> str:
        return str(self.value)
