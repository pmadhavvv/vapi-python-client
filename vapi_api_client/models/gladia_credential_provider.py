from enum import Enum


class GladiaCredentialProvider(str, Enum):
    GLADIA = "gladia"

    def __str__(self) -> str:
        return str(self.value)
