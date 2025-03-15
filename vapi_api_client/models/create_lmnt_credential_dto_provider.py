from enum import Enum


class CreateLmntCredentialDTOProvider(str, Enum):
    LMNT = "lmnt"

    def __str__(self) -> str:
        return str(self.value)
