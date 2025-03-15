from enum import Enum


class CloudflareCredentialProvider(str, Enum):
    CLOUDFLARE = "cloudflare"

    def __str__(self) -> str:
        return str(self.value)
