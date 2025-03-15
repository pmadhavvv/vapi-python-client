from enum import Enum


class VapiCostSubType(str, Enum):
    NORMAL = "normal"
    OVERAGE = "overage"

    def __str__(self) -> str:
        return str(self.value)
