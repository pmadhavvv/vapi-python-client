from enum import Enum


class GladiaTranscriberProvider(str, Enum):
    GLADIA = "gladia"

    def __str__(self) -> str:
        return str(self.value)
