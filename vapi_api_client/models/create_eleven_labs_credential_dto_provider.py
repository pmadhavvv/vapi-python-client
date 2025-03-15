from enum import Enum


class CreateElevenLabsCredentialDTOProvider(str, Enum):
    VALUE_0 = "11labs"

    def __str__(self) -> str:
        return str(self.value)
