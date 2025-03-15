from enum import Enum


class CreateGhlToolDTOType(str, Enum):
    GHL = "ghl"

    def __str__(self) -> str:
        return str(self.value)
