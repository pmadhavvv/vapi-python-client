from enum import Enum


class TransportCostType(str, Enum):
    TRANSPORT = "transport"

    def __str__(self) -> str:
        return str(self.value)
