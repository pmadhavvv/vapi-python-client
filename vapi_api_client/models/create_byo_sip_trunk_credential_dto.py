from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_byo_sip_trunk_credential_dto_provider import CreateByoSipTrunkCredentialDTOProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sbc_configuration import SbcConfiguration
    from ..models.sip_trunk_gateway import SipTrunkGateway
    from ..models.sip_trunk_outbound_authentication_plan import SipTrunkOutboundAuthenticationPlan


T = TypeVar("T", bound="CreateByoSipTrunkCredentialDTO")


@_attrs_define
class CreateByoSipTrunkCredentialDTO:
    """
    Attributes:
        gateways (list['SipTrunkGateway']): This is the list of SIP trunk's gateways.
        provider (Union[Unset, CreateByoSipTrunkCredentialDTOProvider]): This can be used to bring your own SIP trunks
            or to connect to a Carrier.
        outbound_authentication_plan (Union[Unset, SipTrunkOutboundAuthenticationPlan]):
        outbound_leading_plus_enabled (Union[Unset, bool]): This ensures the outbound origination attempts have a
            leading plus. Defaults to false to match conventional telecom behavior.

            Usage:
            - Vonage/Twilio requires leading plus for all outbound calls. Set this to true.

            @default false
        tech_prefix (Union[Unset, str]): This can be used to configure the tech prefix on outbound calls. This is an
            advanced property.
        sip_diversion_header (Union[Unset, str]): This can be used to enable the SIP diversion header for authenticating
            the calling number if the SIP trunk supports it. This is an advanced property.
        sbc_configuration (Union[Unset, SbcConfiguration]):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    gateways: list["SipTrunkGateway"]
    provider: Union[Unset, CreateByoSipTrunkCredentialDTOProvider] = UNSET
    outbound_authentication_plan: Union[Unset, "SipTrunkOutboundAuthenticationPlan"] = UNSET
    outbound_leading_plus_enabled: Union[Unset, bool] = UNSET
    tech_prefix: Union[Unset, str] = UNSET
    sip_diversion_header: Union[Unset, str] = UNSET
    sbc_configuration: Union[Unset, "SbcConfiguration"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateways = []
        for gateways_item_data in self.gateways:
            gateways_item = gateways_item_data.to_dict()
            gateways.append(gateways_item)

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        outbound_authentication_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.outbound_authentication_plan, Unset):
            outbound_authentication_plan = self.outbound_authentication_plan.to_dict()

        outbound_leading_plus_enabled = self.outbound_leading_plus_enabled

        tech_prefix = self.tech_prefix

        sip_diversion_header = self.sip_diversion_header

        sbc_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sbc_configuration, Unset):
            sbc_configuration = self.sbc_configuration.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gateways": gateways,
            }
        )
        if provider is not UNSET:
            field_dict["provider"] = provider
        if outbound_authentication_plan is not UNSET:
            field_dict["outboundAuthenticationPlan"] = outbound_authentication_plan
        if outbound_leading_plus_enabled is not UNSET:
            field_dict["outboundLeadingPlusEnabled"] = outbound_leading_plus_enabled
        if tech_prefix is not UNSET:
            field_dict["techPrefix"] = tech_prefix
        if sip_diversion_header is not UNSET:
            field_dict["sipDiversionHeader"] = sip_diversion_header
        if sbc_configuration is not UNSET:
            field_dict["sbcConfiguration"] = sbc_configuration
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sbc_configuration import SbcConfiguration
        from ..models.sip_trunk_gateway import SipTrunkGateway
        from ..models.sip_trunk_outbound_authentication_plan import SipTrunkOutboundAuthenticationPlan

        d = src_dict.copy()
        gateways = []
        _gateways = d.pop("gateways")
        for gateways_item_data in _gateways:
            gateways_item = SipTrunkGateway.from_dict(gateways_item_data)

            gateways.append(gateways_item)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, CreateByoSipTrunkCredentialDTOProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = CreateByoSipTrunkCredentialDTOProvider(_provider)

        _outbound_authentication_plan = d.pop("outboundAuthenticationPlan", UNSET)
        outbound_authentication_plan: Union[Unset, SipTrunkOutboundAuthenticationPlan]
        if isinstance(_outbound_authentication_plan, Unset):
            outbound_authentication_plan = UNSET
        else:
            outbound_authentication_plan = SipTrunkOutboundAuthenticationPlan.from_dict(_outbound_authentication_plan)

        outbound_leading_plus_enabled = d.pop("outboundLeadingPlusEnabled", UNSET)

        tech_prefix = d.pop("techPrefix", UNSET)

        sip_diversion_header = d.pop("sipDiversionHeader", UNSET)

        _sbc_configuration = d.pop("sbcConfiguration", UNSET)
        sbc_configuration: Union[Unset, SbcConfiguration]
        if isinstance(_sbc_configuration, Unset):
            sbc_configuration = UNSET
        else:
            sbc_configuration = SbcConfiguration.from_dict(_sbc_configuration)

        name = d.pop("name", UNSET)

        create_byo_sip_trunk_credential_dto = cls(
            gateways=gateways,
            provider=provider,
            outbound_authentication_plan=outbound_authentication_plan,
            outbound_leading_plus_enabled=outbound_leading_plus_enabled,
            tech_prefix=tech_prefix,
            sip_diversion_header=sip_diversion_header,
            sbc_configuration=sbc_configuration,
            name=name,
        )

        create_byo_sip_trunk_credential_dto.additional_properties = d
        return create_byo_sip_trunk_credential_dto

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
