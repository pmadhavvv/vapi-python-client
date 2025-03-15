from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_language_change_detected_type import ClientMessageLanguageChangeDetectedType

T = TypeVar("T", bound="ClientMessageLanguageChangeDetected")


@_attrs_define
class ClientMessageLanguageChangeDetected:
    """
    Attributes:
        type_ (ClientMessageLanguageChangeDetectedType): This is the type of the message. "language-change-detected" is
            sent when the transcriber is automatically switched based on the detected language.
        language (str): This is the language the transcriber is switched to.
    """

    type_: ClientMessageLanguageChangeDetectedType
    language: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "language": language,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = ClientMessageLanguageChangeDetectedType(d.pop("type"))

        language = d.pop("language")

        client_message_language_change_detected = cls(
            type_=type_,
            language=language,
        )

        client_message_language_change_detected.additional_properties = d
        return client_message_language_change_detected

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
