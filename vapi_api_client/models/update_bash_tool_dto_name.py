from enum import Enum


class UpdateBashToolDTOName(str, Enum):
    BASH = "bash"

    def __str__(self) -> str:
        return str(self.value)
