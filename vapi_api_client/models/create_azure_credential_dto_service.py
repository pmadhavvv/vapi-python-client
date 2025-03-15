from enum import Enum


class CreateAzureCredentialDTOService(str, Enum):
    BLOB_STORAGE = "blob_storage"
    SPEECH = "speech"

    def __str__(self) -> str:
        return str(self.value)
