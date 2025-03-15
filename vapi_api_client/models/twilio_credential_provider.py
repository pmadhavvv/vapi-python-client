from enum import Enum


class TwilioCredentialProvider(str, Enum):
    TWILIO = "twilio"

    def __str__(self) -> str:
        return str(self.value)
