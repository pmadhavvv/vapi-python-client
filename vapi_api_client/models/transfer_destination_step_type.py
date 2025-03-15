from enum import Enum


class TransferDestinationStepType(str, Enum):
    STEP = "step"

    def __str__(self) -> str:
        return str(self.value)
