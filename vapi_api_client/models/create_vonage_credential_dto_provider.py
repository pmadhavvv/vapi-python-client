from enum import Enum


class CreateVonageCredentialDTOProvider(str, Enum):
    VONAGE = "vonage"

    def __str__(self) -> str:
        return str(self.value)
