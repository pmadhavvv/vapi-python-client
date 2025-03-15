from enum import Enum


class ClientInboundMessageTransferType(str, Enum):
    TRANSFER = "transfer"

    def __str__(self) -> str:
        return str(self.value)
