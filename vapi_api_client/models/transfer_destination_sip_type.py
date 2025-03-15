from enum import Enum


class TransferDestinationSipType(str, Enum):
    SIP = "sip"

    def __str__(self) -> str:
        return str(self.value)
