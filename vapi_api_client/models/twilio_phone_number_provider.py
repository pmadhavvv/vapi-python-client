from enum import Enum


class TwilioPhoneNumberProvider(str, Enum):
    TWILIO = "twilio"

    def __str__(self) -> str:
        return str(self.value)
