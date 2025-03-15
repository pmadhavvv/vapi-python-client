from enum import Enum


class ServerMessageTransferUpdateType(str, Enum):
    TRANSFER_UPDATE = "transfer-update"

    def __str__(self) -> str:
        return str(self.value)
