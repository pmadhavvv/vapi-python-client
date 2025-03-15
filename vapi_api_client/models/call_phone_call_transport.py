from enum import Enum


class CallPhoneCallTransport(str, Enum):
    PSTN = "pstn"
    SIP = "sip"

    def __str__(self) -> str:
        return str(self.value)
