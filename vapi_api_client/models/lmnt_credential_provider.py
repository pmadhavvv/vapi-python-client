from enum import Enum


class LmntCredentialProvider(str, Enum):
    LMNT = "lmnt"

    def __str__(self) -> str:
        return str(self.value)
