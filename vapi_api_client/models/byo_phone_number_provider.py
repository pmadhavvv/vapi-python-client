from enum import Enum


class ByoPhoneNumberProvider(str, Enum):
    BYO_PHONE_NUMBER = "byo-phone-number"

    def __str__(self) -> str:
        return str(self.value)
