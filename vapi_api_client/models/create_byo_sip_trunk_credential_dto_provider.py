from enum import Enum


class CreateByoSipTrunkCredentialDTOProvider(str, Enum):
    BYO_SIP_TRUNK = "byo-sip-trunk"

    def __str__(self) -> str:
        return str(self.value)
