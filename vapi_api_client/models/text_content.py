from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_content_language import TextContentLanguage
from ..models.text_content_type import TextContentType

T = TypeVar("T", bound="TextContent")


@_attrs_define
class TextContent:
    """
    Attributes:
        type_ (TextContentType):
        text (str):
        language (TextContentLanguage):
    """

    type_: TextContentType
    text: str
    language: TextContentLanguage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        text = self.text

        language = self.language.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "text": text,
                "language": language,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = TextContentType(d.pop("type"))

        text = d.pop("text")

        language = TextContentLanguage(d.pop("language"))

        text_content = cls(
            type_=type_,
            text=text,
            language=language,
        )

        text_content.additional_properties = d
        return text_content

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
