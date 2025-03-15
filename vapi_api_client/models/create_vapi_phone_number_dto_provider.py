from enum import Enum


class CreateVapiPhoneNumberDTOProvider(str, Enum):
    VAPI = "vapi"

    def __str__(self) -> str:
        return str(self.value)
