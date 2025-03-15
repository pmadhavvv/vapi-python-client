from enum import Enum


class ToolMessageCompleteType(str, Enum):
    REQUEST_COMPLETE = "request-complete"

    def __str__(self) -> str:
        return str(self.value)
