from enum import Enum


class TrieveCredentialProvider(str, Enum):
    TRIEVE = "trieve"

    def __str__(self) -> str:
        return str(self.value)
