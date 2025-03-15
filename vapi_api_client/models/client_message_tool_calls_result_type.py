from enum import Enum


class ClientMessageToolCallsResultType(str, Enum):
    TOOL_CALLS_RESULT = "tool-calls-result"

    def __str__(self) -> str:
        return str(self.value)
