from enum import Enum


class CallPhoneCallProvider(str, Enum):
    TELNYX = "telnyx"
    TWILIO = "twilio"
    VAPI = "vapi"
    VONAGE = "vonage"

    def __str__(self) -> str:
        return str(self.value)
