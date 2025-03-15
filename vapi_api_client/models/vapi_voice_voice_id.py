from enum import Enum


class VapiVoiceVoiceId(str, Enum):
    COLE = "Cole"
    ELLIOT = "Elliot"
    HANA = "Hana"
    HARRY = "Harry"
    LILY = "Lily"
    NEHA = "Neha"
    PAIGE = "Paige"
    ROHAN = "Rohan"
    SAVANNAH = "Savannah"

    def __str__(self) -> str:
        return str(self.value)
