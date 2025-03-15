from enum import Enum


class TransportConfigurationTwilioProvider(str, Enum):
    TWILIO = "twilio"

    def __str__(self) -> str:
        return str(self.value)
