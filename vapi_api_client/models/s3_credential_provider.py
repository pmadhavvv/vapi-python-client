from enum import Enum


class S3CredentialProvider(str, Enum):
    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
