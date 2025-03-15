from enum import Enum


class CreateCloudflareCredentialDTOProvider(str, Enum):
    CLOUDFLARE = "cloudflare"

    def __str__(self) -> str:
        return str(self.value)
