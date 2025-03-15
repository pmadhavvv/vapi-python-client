from enum import Enum


class CreateS3CredentialDTOProvider(str, Enum):
    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
