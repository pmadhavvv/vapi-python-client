from enum import Enum


class OrgChannel(str, Enum):
    DEFAULT = "default"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
