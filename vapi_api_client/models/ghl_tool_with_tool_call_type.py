from enum import Enum


class GhlToolWithToolCallType(str, Enum):
    GHL = "ghl"

    def __str__(self) -> str:
        return str(self.value)
