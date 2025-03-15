from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_perplexity_ai_credential_dto_provider import CreatePerplexityAICredentialDTOProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePerplexityAICredentialDTO")


@_attrs_define
class CreatePerplexityAICredentialDTO:
    """
    Attributes:
        provider (CreatePerplexityAICredentialDTOProvider):
        api_key (str): This is not returned in the API.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: CreatePerplexityAICredentialDTOProvider
    api_key: str
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        api_key = self.api_key

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "apiKey": api_key,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = CreatePerplexityAICredentialDTOProvider(d.pop("provider"))

        api_key = d.pop("apiKey")

        name = d.pop("name", UNSET)

        create_perplexity_ai_credential_dto = cls(
            provider=provider,
            api_key=api_key,
            name=name,
        )

        create_perplexity_ai_credential_dto.additional_properties = d
        return create_perplexity_ai_credential_dto

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
