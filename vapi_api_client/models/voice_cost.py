from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voice_cost_type import VoiceCostType

if TYPE_CHECKING:
    from ..models.voice_cost_voice import VoiceCostVoice


T = TypeVar("T", bound="VoiceCost")


@_attrs_define
class VoiceCost:
    """
    Attributes:
        type_ (VoiceCostType): This is the type of cost, always 'voice' for this class.
        voice (VoiceCostVoice): This is the voice that was used during the call.

            This matches one of the following:
            - `call.assistant.voice`,
            - `call.assistantId->voice`,
            - `call.squad[n].assistant.voice`,
            - `call.squad[n].assistantId->voice`,
            - `call.squadId->[n].assistant.voice`,
            - `call.squadId->[n].assistantId->voice`.
        characters (float): This is the number of characters that were generated during the call. These should be total
            characters used in the call for single assistant calls, while squad calls will have multiple voice costs one for
            each assistant that was used.
        cost (float): This is the cost of the component in USD.
    """

    type_: VoiceCostType
    voice: "VoiceCostVoice"
    characters: float
    cost: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        voice = self.voice.to_dict()

        characters = self.characters

        cost = self.cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "voice": voice,
                "characters": characters,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.voice_cost_voice import VoiceCostVoice

        d = src_dict.copy()
        type_ = VoiceCostType(d.pop("type"))

        voice = VoiceCostVoice.from_dict(d.pop("voice"))

        characters = d.pop("characters")

        cost = d.pop("cost")

        voice_cost = cls(
            type_=type_,
            voice=voice,
            characters=characters,
            cost=cost,
        )

        voice_cost.additional_properties = d
        return voice_cost

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
