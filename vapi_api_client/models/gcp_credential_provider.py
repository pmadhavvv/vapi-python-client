from enum import Enum


class GcpCredentialProvider(str, Enum):
    GCP = "gcp"

    def __str__(self) -> str:
        return str(self.value)
