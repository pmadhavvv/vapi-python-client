from enum import Enum


class GladiaTranscriberModelType0(str, Enum):
    ACCURATE = "accurate"
    FAST = "fast"

    def __str__(self) -> str:
        return str(self.value)
