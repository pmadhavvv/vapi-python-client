from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddVoiceToProviderDTO")


@_attrs_define
class AddVoiceToProviderDTO:
    """
    Attributes:
        owner_id (str): This is the owner_id of your shared voice which you want to add to your provider Account from
            Provider Voice Library
        voice_id (str): This is the voice_id of the shared voice which you want to add to your provider Account from
            Provider Voice Library
        name (str): This is the new name of the voice which you want to have once you have added voice to your provider
            Account from Provider Voice Library
    """

    owner_id: str
    voice_id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        voice_id = self.voice_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ownerId": owner_id,
                "voiceId": voice_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        owner_id = d.pop("ownerId")

        voice_id = d.pop("voiceId")

        name = d.pop("name")

        add_voice_to_provider_dto = cls(
            owner_id=owner_id,
            voice_id=voice_id,
            name=name,
        )

        add_voice_to_provider_dto.additional_properties = d
        return add_voice_to_provider_dto

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
