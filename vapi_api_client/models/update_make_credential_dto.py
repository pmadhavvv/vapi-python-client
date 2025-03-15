from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateMakeCredentialDTO")


@_attrs_define
class UpdateMakeCredentialDTO:
    """
    Attributes:
        team_id (Union[Unset, str]): Team ID
        region (Union[Unset, str]): Region of your application. For example: eu1, eu2, us1, us2
        api_key (Union[Unset, str]): This is not returned in the API.
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    team_id: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    api_key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        region = self.region

        api_key = self.api_key

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if region is not UNSET:
            field_dict["region"] = region
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        team_id = d.pop("teamId", UNSET)

        region = d.pop("region", UNSET)

        api_key = d.pop("apiKey", UNSET)

        name = d.pop("name", UNSET)

        update_make_credential_dto = cls(
            team_id=team_id,
            region=region,
            api_key=api_key,
            name=name,
        )

        update_make_credential_dto.additional_properties = d
        return update_make_credential_dto

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
