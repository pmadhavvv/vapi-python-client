from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_voice_input_type import ClientMessageVoiceInputType

T = TypeVar("T", bound="ClientMessageVoiceInput")


@_attrs_define
class ClientMessageVoiceInput:
    """
    Attributes:
        type_ (ClientMessageVoiceInputType): This is the type of the message. "voice-input" is sent when a generation is
            requested from voice provider.
        input_ (str): This is the voice input content
    """

    type_: ClientMessageVoiceInputType
    input_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        input_ = self.input_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "input": input_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ClientMessageVoiceInputType(d.pop("type"))

        input_ = d.pop("input")

        client_message_voice_input = cls(
            type_=type_,
            input_=input_,
        )

        client_message_voice_input.additional_properties = d
        return client_message_voice_input

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
