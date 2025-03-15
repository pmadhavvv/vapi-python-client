from enum import Enum


class VonagePhoneNumberProvider(str, Enum):
    VONAGE = "vonage"

    def __str__(self) -> str:
        return str(self.value)
