from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SipTrunkOutboundSipRegisterPlan")


@_attrs_define
class SipTrunkOutboundSipRegisterPlan:
    """
    Attributes:
        domain (Union[Unset, str]):
        username (Union[Unset, str]):
        realm (Union[Unset, str]):
    """

    domain: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    realm: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        username = self.username

        realm = self.realm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if username is not UNSET:
            field_dict["username"] = username
        if realm is not UNSET:
            field_dict["realm"] = realm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        domain = d.pop("domain", UNSET)

        username = d.pop("username", UNSET)

        realm = d.pop("realm", UNSET)

        sip_trunk_outbound_sip_register_plan = cls(
            domain=domain,
            username=username,
            realm=realm,
        )

        sip_trunk_outbound_sip_register_plan.additional_properties = d
        return sip_trunk_outbound_sip_register_plan

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
