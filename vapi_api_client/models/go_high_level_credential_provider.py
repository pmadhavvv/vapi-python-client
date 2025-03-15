from enum import Enum


class GoHighLevelCredentialProvider(str, Enum):
    GOHIGHLEVEL = "gohighlevel"

    def __str__(self) -> str:
        return str(self.value)
