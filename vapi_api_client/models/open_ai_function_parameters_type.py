from enum import Enum


class OpenAIFunctionParametersType(str, Enum):
    OBJECT = "object"

    def __str__(self) -> str:
        return str(self.value)
