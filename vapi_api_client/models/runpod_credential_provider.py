from enum import Enum


class RunpodCredentialProvider(str, Enum):
    RUNPOD = "runpod"

    def __str__(self) -> str:
        return str(self.value)
