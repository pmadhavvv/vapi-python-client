from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_play_ht_credential_dto_provider import CreatePlayHTCredentialDTOProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePlayHTCredentialDTO")


@_attrs_define
class CreatePlayHTCredentialDTO:
    """
    Attributes:
        provider (CreatePlayHTCredentialDTOProvider):
        api_key (str): This is not returned in the API.
        user_id (str):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: CreatePlayHTCredentialDTOProvider
    api_key: str
    user_id: str
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        api_key = self.api_key

        user_id = self.user_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "apiKey": api_key,
                "userId": user_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = CreatePlayHTCredentialDTOProvider(d.pop("provider"))

        api_key = d.pop("apiKey")

        user_id = d.pop("userId")

        name = d.pop("name", UNSET)

        create_play_ht_credential_dto = cls(
            provider=provider,
            api_key=api_key,
            user_id=user_id,
            name=name,
        )

        create_play_ht_credential_dto.additional_properties = d
        return create_play_ht_credential_dto

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
