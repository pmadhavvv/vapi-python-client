from enum import Enum


class ToolMessageDelayedType(str, Enum):
    REQUEST_RESPONSE_DELAYED = "request-response-delayed"

    def __str__(self) -> str:
        return str(self.value)
