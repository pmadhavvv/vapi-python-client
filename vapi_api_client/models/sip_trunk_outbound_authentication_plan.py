from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sip_trunk_outbound_sip_register_plan import SipTrunkOutboundSipRegisterPlan


T = TypeVar("T", bound="SipTrunkOutboundAuthenticationPlan")


@_attrs_define
class SipTrunkOutboundAuthenticationPlan:
    """
    Attributes:
        auth_password (Union[Unset, str]): This is not returned in the API.
        auth_username (Union[Unset, str]):
        sip_register_plan (Union[Unset, SipTrunkOutboundSipRegisterPlan]):
    """

    auth_password: Union[Unset, str] = UNSET
    auth_username: Union[Unset, str] = UNSET
    sip_register_plan: Union[Unset, "SipTrunkOutboundSipRegisterPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_password = self.auth_password

        auth_username = self.auth_username

        sip_register_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sip_register_plan, Unset):
            sip_register_plan = self.sip_register_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_password is not UNSET:
            field_dict["authPassword"] = auth_password
        if auth_username is not UNSET:
            field_dict["authUsername"] = auth_username
        if sip_register_plan is not UNSET:
            field_dict["sipRegisterPlan"] = sip_register_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sip_trunk_outbound_sip_register_plan import SipTrunkOutboundSipRegisterPlan

        d = dict(src_dict)
        auth_password = d.pop("authPassword", UNSET)

        auth_username = d.pop("authUsername", UNSET)

        _sip_register_plan = d.pop("sipRegisterPlan", UNSET)
        sip_register_plan: Union[Unset, SipTrunkOutboundSipRegisterPlan]
        if isinstance(_sip_register_plan, Unset):
            sip_register_plan = UNSET
        else:
            sip_register_plan = SipTrunkOutboundSipRegisterPlan.from_dict(_sip_register_plan)

        sip_trunk_outbound_authentication_plan = cls(
            auth_password=auth_password,
            auth_username=auth_username,
            sip_register_plan=sip_register_plan,
        )

        sip_trunk_outbound_authentication_plan.additional_properties = d
        return sip_trunk_outbound_authentication_plan

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
