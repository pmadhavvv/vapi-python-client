from enum import Enum


class SipTrunkGatewayOutboundProtocol(str, Enum):
    TCP = "tcp"
    TLS = "tls"
    TLSSRTP = "tls/srtp"
    UDP = "udp"

    def __str__(self) -> str:
        return str(self.value)
