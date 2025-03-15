from enum import Enum


class CreateDeepInfraCredentialDTOProvider(str, Enum):
    DEEPINFRA = "deepinfra"

    def __str__(self) -> str:
        return str(self.value)
