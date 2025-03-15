from enum import Enum


class CreateOrgDTOChannel(str, Enum):
    DEFAULT = "default"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
