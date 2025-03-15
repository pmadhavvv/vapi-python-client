from enum import Enum


class TransportCostProvider(str, Enum):
    TWILIO = "twilio"
    VAPI = "vapi"
    VONAGE = "vonage"

    def __str__(self) -> str:
        return str(self.value)
