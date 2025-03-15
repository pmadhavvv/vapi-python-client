from enum import Enum


class EndCallToolType(str, Enum):
    ENDCALL = "endCall"

    def __str__(self) -> str:
        return str(self.value)
