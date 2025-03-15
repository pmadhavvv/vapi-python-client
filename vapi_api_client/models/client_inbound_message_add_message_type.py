from enum import Enum


class ClientInboundMessageAddMessageType(str, Enum):
    ADD_MESSAGE = "add-message"

    def __str__(self) -> str:
        return str(self.value)
