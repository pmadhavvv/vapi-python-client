from enum import Enum


class UpdateOrgDTOChannel(str, Enum):
    DEFAULT = "default"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
