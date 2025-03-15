from enum import Enum


class GoogleModelProvider(str, Enum):
    GOOGLE = "google"

    def __str__(self) -> str:
        return str(self.value)
