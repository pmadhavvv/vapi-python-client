from enum import Enum


class GhlToolProviderDetailsType(str, Enum):
    GHL = "ghl"

    def __str__(self) -> str:
        return str(self.value)
