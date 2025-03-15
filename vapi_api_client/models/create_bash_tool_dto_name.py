from enum import Enum


class CreateBashToolDTOName(str, Enum):
    BASH = "bash"

    def __str__(self) -> str:
        return str(self.value)
