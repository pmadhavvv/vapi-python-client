from enum import Enum


class ClientMessageLanguageChangeDetectedType(str, Enum):
    LANGUAGE_CHANGE_DETECTED = "language-change-detected"

    def __str__(self) -> str:
        return str(self.value)
