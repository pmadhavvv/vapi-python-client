from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDeepgramCredentialDTO")


@_attrs_define
class UpdateDeepgramCredentialDTO:
    """
    Attributes:
        api_key (Union[Unset, str]): This is not returned in the API.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
        api_url (Union[Unset, str]): This can be used to point to an onprem Deepgram instance. Defaults to
            api.deepgram.com.
    """

    api_key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    api_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        name = self.name

        api_url = self.api_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if name is not UNSET:
            field_dict["name"] = name
        if api_url is not UNSET:
            field_dict["apiUrl"] = api_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey", UNSET)

        name = d.pop("name", UNSET)

        api_url = d.pop("apiUrl", UNSET)

        update_deepgram_credential_dto = cls(
            api_key=api_key,
            name=name,
            api_url=api_url,
        )

        update_deepgram_credential_dto.additional_properties = d
        return update_deepgram_credential_dto

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
