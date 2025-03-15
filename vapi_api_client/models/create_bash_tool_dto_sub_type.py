from enum import Enum


class CreateBashToolDTOSubType(str, Enum):
    BASH_20241022 = "bash_20241022"

    def __str__(self) -> str:
        return str(self.value)
