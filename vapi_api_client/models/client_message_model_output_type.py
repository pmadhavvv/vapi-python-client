from enum import Enum


class ClientMessageModelOutputType(str, Enum):
    MODEL_OUTPUT = "model-output"

    def __str__(self) -> str:
        return str(self.value)
