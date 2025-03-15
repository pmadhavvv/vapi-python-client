from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sip_trunk_gateway_outbound_protocol import SipTrunkGatewayOutboundProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="SipTrunkGateway")


@_attrs_define
class SipTrunkGateway:
    """
    Attributes:
        ip (str): This is the address of the gateway. It can be an IPv4 address like 1.1.1.1 or a fully qualified domain
            name like my-sip-trunk.pstn.twilio.com.
        port (Union[Unset, float]): This is the port number of the gateway. Default is 5060.

            @default 5060
        netmask (Union[Unset, float]): This is the netmask of the gateway. Defaults to 32.

            @default 32
        inbound_enabled (Union[Unset, bool]): This is whether inbound calls are allowed from this gateway. Default is
            true.

            @default true
        outbound_enabled (Union[Unset, bool]): This is whether outbound calls should be sent to this gateway. Default is
            true.

            Note, if netmask is less than 32, it doesn't affect the outbound IPs that are tried. 1 attempt is made to
            `ip:port`.

            @default true
        outbound_protocol (Union[Unset, SipTrunkGatewayOutboundProtocol]): This is the protocol to use for SIP signaling
            outbound calls. Default is udp.

            @default udp
        options_ping_enabled (Union[Unset, bool]): This is whether to send options ping to the gateway. This can be used
            to check if the gateway is reachable. Default is false.

            This is useful for high availability setups where you want to check if the gateway is reachable before routing
            calls to it. Note, if no gateway for a trunk is reachable, outbound calls will be rejected.

            @default false
    """

    ip: str
    port: Union[Unset, float] = UNSET
    netmask: Union[Unset, float] = UNSET
    inbound_enabled: Union[Unset, bool] = UNSET
    outbound_enabled: Union[Unset, bool] = UNSET
    outbound_protocol: Union[Unset, SipTrunkGatewayOutboundProtocol] = UNSET
    options_ping_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip = self.ip

        port = self.port

        netmask = self.netmask

        inbound_enabled = self.inbound_enabled

        outbound_enabled = self.outbound_enabled

        outbound_protocol: Union[Unset, str] = UNSET
        if not isinstance(self.outbound_protocol, Unset):
            outbound_protocol = self.outbound_protocol.value

        options_ping_enabled = self.options_ping_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip": ip,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port
        if netmask is not UNSET:
            field_dict["netmask"] = netmask
        if inbound_enabled is not UNSET:
            field_dict["inboundEnabled"] = inbound_enabled
        if outbound_enabled is not UNSET:
            field_dict["outboundEnabled"] = outbound_enabled
        if outbound_protocol is not UNSET:
            field_dict["outboundProtocol"] = outbound_protocol
        if options_ping_enabled is not UNSET:
            field_dict["optionsPingEnabled"] = options_ping_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ip = d.pop("ip")

        port = d.pop("port", UNSET)

        netmask = d.pop("netmask", UNSET)

        inbound_enabled = d.pop("inboundEnabled", UNSET)

        outbound_enabled = d.pop("outboundEnabled", UNSET)

        _outbound_protocol = d.pop("outboundProtocol", UNSET)
        outbound_protocol: Union[Unset, SipTrunkGatewayOutboundProtocol]
        if isinstance(_outbound_protocol, Unset):
            outbound_protocol = UNSET
        else:
            outbound_protocol = SipTrunkGatewayOutboundProtocol(_outbound_protocol)

        options_ping_enabled = d.pop("optionsPingEnabled", UNSET)

        sip_trunk_gateway = cls(
            ip=ip,
            port=port,
            netmask=netmask,
            inbound_enabled=inbound_enabled,
            outbound_enabled=outbound_enabled,
            outbound_protocol=outbound_protocol,
            options_ping_enabled=options_ping_enabled,
        )

        sip_trunk_gateway.additional_properties = d
        return sip_trunk_gateway

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
