from enum import Enum


class CallType(str, Enum):
    INBOUNDPHONECALL = "inboundPhoneCall"
    OUTBOUNDPHONECALL = "outboundPhoneCall"
    WEBCALL = "webCall"

    def __str__(self) -> str:
        return str(self.value)
