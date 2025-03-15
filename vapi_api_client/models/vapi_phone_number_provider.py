from enum import Enum


class VapiPhoneNumberProvider(str, Enum):
    VAPI = "vapi"

    def __str__(self) -> str:
        return str(self.value)
