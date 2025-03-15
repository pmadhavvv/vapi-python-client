from enum import Enum


class TransferPlanSipVerb(str, Enum):
    BYE = "bye"
    DIAL = "dial"
    REFER = "refer"

    def __str__(self) -> str:
        return str(self.value)
