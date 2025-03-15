from enum import Enum


class DtmfToolType(str, Enum):
    DTMF = "dtmf"

    def __str__(self) -> str:
        return str(self.value)
