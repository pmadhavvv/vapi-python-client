from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateLangfuseCredentialDTO")


@_attrs_define
class UpdateLangfuseCredentialDTO:
    """
    Attributes:
        public_key (Union[Unset, str]): The public key for Langfuse project. Eg: pk-lf-...
        api_key (Union[Unset, str]): The secret key for Langfuse project. Eg: sk-lf-... .This is not returned in the
            API.
        api_url (Union[Unset, str]): The host URL for Langfuse project. Eg: https://cloud.langfuse.com
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    public_key: Union[Unset, str] = UNSET
    api_key: Union[Unset, str] = UNSET
    api_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_key = self.public_key

        api_key = self.api_key

        api_url = self.api_url

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if api_url is not UNSET:
            field_dict["apiUrl"] = api_url
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        public_key = d.pop("publicKey", UNSET)

        api_key = d.pop("apiKey", UNSET)

        api_url = d.pop("apiUrl", UNSET)

        name = d.pop("name", UNSET)

        update_langfuse_credential_dto = cls(
            public_key=public_key,
            api_key=api_key,
            api_url=api_url,
            name=name,
        )

        update_langfuse_credential_dto.additional_properties = d
        return update_langfuse_credential_dto

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
