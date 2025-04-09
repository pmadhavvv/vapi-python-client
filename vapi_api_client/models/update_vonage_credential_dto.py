from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateVonageCredentialDTO")


@_attrs_define
class UpdateVonageCredentialDTO:
    """
    Attributes:
        api_secret (Union[Unset, str]): This is not returned in the API.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
        api_key (Union[Unset, str]):
    """

    api_secret: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    api_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_secret = self.api_secret

        name = self.name

        api_key = self.api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_secret is not UNSET:
            field_dict["apiSecret"] = api_secret
        if name is not UNSET:
            field_dict["name"] = name
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_secret = d.pop("apiSecret", UNSET)

        name = d.pop("name", UNSET)

        api_key = d.pop("apiKey", UNSET)

        update_vonage_credential_dto = cls(
            api_secret=api_secret,
            name=name,
            api_key=api_key,
        )

        update_vonage_credential_dto.additional_properties = d
        return update_vonage_credential_dto

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
