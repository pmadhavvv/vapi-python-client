from enum import Enum


class CreateWebhookCredentialDTOProvider(str, Enum):
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
