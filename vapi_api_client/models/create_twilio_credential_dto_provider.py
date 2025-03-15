from enum import Enum


class CreateTwilioCredentialDTOProvider(str, Enum):
    TWILIO = "twilio"

    def __str__(self) -> str:
        return str(self.value)
