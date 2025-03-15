from enum import Enum


class CreateGoHighLevelCredentialDTOProvider(str, Enum):
    GOHIGHLEVEL = "gohighlevel"

    def __str__(self) -> str:
        return str(self.value)
