from enum import Enum


class GhlToolType(str, Enum):
    GHL = "ghl"

    def __str__(self) -> str:
        return str(self.value)
