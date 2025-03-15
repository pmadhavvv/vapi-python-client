from enum import Enum


class DeepInfraCredentialProvider(str, Enum):
    DEEPINFRA = "deepinfra"

    def __str__(self) -> str:
        return str(self.value)
