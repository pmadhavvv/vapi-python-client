from enum import Enum


class ToolMessageFailedType(str, Enum):
    REQUEST_FAILED = "request-failed"

    def __str__(self) -> str:
        return str(self.value)
