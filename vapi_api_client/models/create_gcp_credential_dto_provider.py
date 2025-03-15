from enum import Enum


class CreateGcpCredentialDTOProvider(str, Enum):
    GCP = "gcp"

    def __str__(self) -> str:
        return str(self.value)
