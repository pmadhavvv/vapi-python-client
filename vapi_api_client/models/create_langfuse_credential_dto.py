from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_langfuse_credential_dto_provider import CreateLangfuseCredentialDTOProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLangfuseCredentialDTO")


@_attrs_define
class CreateLangfuseCredentialDTO:
    """
    Attributes:
        provider (CreateLangfuseCredentialDTOProvider):
        public_key (str): The public key for Langfuse project. Eg: pk-lf-...
        api_key (str): The secret key for Langfuse project. Eg: sk-lf-... .This is not returned in the API.
        api_url (str): The host URL for Langfuse project. Eg: https://cloud.langfuse.com
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: CreateLangfuseCredentialDTOProvider
    public_key: str
    api_key: str
    api_url: str
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        public_key = self.public_key

        api_key = self.api_key

        api_url = self.api_url

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "publicKey": public_key,
                "apiKey": api_key,
                "apiUrl": api_url,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = CreateLangfuseCredentialDTOProvider(d.pop("provider"))

        public_key = d.pop("publicKey")

        api_key = d.pop("apiKey")

        api_url = d.pop("apiUrl")

        name = d.pop("name", UNSET)

        create_langfuse_credential_dto = cls(
            provider=provider,
            public_key=public_key,
            api_key=api_key,
            api_url=api_url,
            name=name,
        )

        create_langfuse_credential_dto.additional_properties = d
        return create_langfuse_credential_dto

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
