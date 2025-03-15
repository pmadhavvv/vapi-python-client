from enum import Enum


class ClientMessageToolCallsType(str, Enum):
    TOOL_CALLS = "tool-calls"

    def __str__(self) -> str:
        return str(self.value)
