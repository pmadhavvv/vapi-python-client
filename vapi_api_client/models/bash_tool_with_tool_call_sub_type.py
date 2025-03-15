from enum import Enum


class BashToolWithToolCallSubType(str, Enum):
    BASH_20241022 = "bash_20241022"

    def __str__(self) -> str:
        return str(self.value)
