from enum import Enum


class ServerMessageTransferDestinationRequestType(str, Enum):
    TRANSFER_DESTINATION_REQUEST = "transfer-destination-request"

    def __str__(self) -> str:
        return str(self.value)
