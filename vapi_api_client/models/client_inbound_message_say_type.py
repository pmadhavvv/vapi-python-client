from enum import Enum


class ClientInboundMessageSayType(str, Enum):
    SAY = "say"

    def __str__(self) -> str:
        return str(self.value)
