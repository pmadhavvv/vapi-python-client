from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SipAuthentication")


@_attrs_define
class SipAuthentication:
    """
    Attributes:
        username (str): This will be expected in the `username` field of the `authorization` header of the SIP INVITE.
        password (str): This will be expected to generate the `response` field of the `authorization` header of the SIP
            INVITE, through digest authentication.
        realm (Union[Unset, str]): This will be expected in the `realm` field of the `authorization` header of the SIP
            INVITE. Defaults to sip.vapi.ai.
    """

    username: str
    password: str
    realm: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        realm = self.realm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )
        if realm is not UNSET:
            field_dict["realm"] = realm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

        realm = d.pop("realm", UNSET)

        sip_authentication = cls(
            username=username,
            password=password,
            realm=realm,
        )

        sip_authentication.additional_properties = d
        return sip_authentication

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
