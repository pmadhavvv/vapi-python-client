from enum import Enum


class CreateRunpodCredentialDTOProvider(str, Enum):
    RUNPOD = "runpod"

    def __str__(self) -> str:
        return str(self.value)
