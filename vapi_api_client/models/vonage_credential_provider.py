from enum import Enum


class VonageCredentialProvider(str, Enum):
    VONAGE = "vonage"

    def __str__(self) -> str:
        return str(self.value)
