from enum import Enum


class CreateVonagePhoneNumberDTOProvider(str, Enum):
    VONAGE = "vonage"

    def __str__(self) -> str:
        return str(self.value)
