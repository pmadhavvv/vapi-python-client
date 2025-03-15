from enum import Enum


class TelnyxPhoneNumberProvider(str, Enum):
    TELNYX = "telnyx"

    def __str__(self) -> str:
        return str(self.value)
