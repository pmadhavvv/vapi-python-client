from enum import Enum


class CustomLLMModelMetadataSendMode(str, Enum):
    DESTRUCTURED = "destructured"
    OFF = "off"
    VARIABLE = "variable"

    def __str__(self) -> str:
        return str(self.value)
