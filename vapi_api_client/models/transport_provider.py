from enum import Enum


class TransportProvider(str, Enum):
    DAILY = "daily"
    TELNYX = "telnyx"
    TWILIO = "twilio"
    VAPI = "vapi"
    VONAGE = "vonage"

    def __str__(self) -> str:
        return str(self.value)
