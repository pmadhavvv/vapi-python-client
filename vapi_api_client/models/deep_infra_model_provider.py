from enum import Enum


class DeepInfraModelProvider(str, Enum):
    DEEPINFRA = "deepinfra"

    def __str__(self) -> str:
        return str(self.value)
