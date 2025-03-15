from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voice_library_voice_response_age import VoiceLibraryVoiceResponseAge


T = TypeVar("T", bound="VoiceLibraryVoiceResponse")


@_attrs_define
class VoiceLibraryVoiceResponse:
    """
    Attributes:
        voice_id (str):
        name (str):
        public_owner_id (Union[Unset, str]):
        description (Union[Unset, str]):
        gender (Union[Unset, str]):
        age (Union[Unset, VoiceLibraryVoiceResponseAge]):
        accent (Union[Unset, str]):
    """

    voice_id: str
    name: str
    public_owner_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    gender: Union[Unset, str] = UNSET
    age: Union[Unset, "VoiceLibraryVoiceResponseAge"] = UNSET
    accent: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        voice_id = self.voice_id

        name = self.name

        public_owner_id = self.public_owner_id

        description = self.description

        gender = self.gender

        age: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.age, Unset):
            age = self.age.to_dict()

        accent = self.accent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "voiceId": voice_id,
                "name": name,
            }
        )
        if public_owner_id is not UNSET:
            field_dict["publicOwnerId"] = public_owner_id
        if description is not UNSET:
            field_dict["description"] = description
        if gender is not UNSET:
            field_dict["gender"] = gender
        if age is not UNSET:
            field_dict["age"] = age
        if accent is not UNSET:
            field_dict["accent"] = accent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.voice_library_voice_response_age import VoiceLibraryVoiceResponseAge

        d = src_dict.copy()
        voice_id = d.pop("voiceId")

        name = d.pop("name")

        public_owner_id = d.pop("publicOwnerId", UNSET)

        description = d.pop("description", UNSET)

        gender = d.pop("gender", UNSET)

        _age = d.pop("age", UNSET)
        age: Union[Unset, VoiceLibraryVoiceResponseAge]
        if isinstance(_age, Unset):
            age = UNSET
        else:
            age = VoiceLibraryVoiceResponseAge.from_dict(_age)

        accent = d.pop("accent", UNSET)

        voice_library_voice_response = cls(
            voice_id=voice_id,
            name=name,
            public_owner_id=public_owner_id,
            description=description,
            gender=gender,
            age=age,
            accent=accent,
        )

        voice_library_voice_response.additional_properties = d
        return voice_library_voice_response

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
