from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_message_type import CustomMessageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_content import TextContent


T = TypeVar("T", bound="CustomMessage")


@_attrs_define
class CustomMessage:
    """
    Attributes:
        type_ (CustomMessageType): This is a custom message.
        contents (Union[Unset, list['TextContent']]): This is an alternative to the `content` property. It allows to
            specify variants of the same content, one per language.

            Usage:
            - If your assistants are multilingual, you can provide content for each language.
            - If you don't provide content for a language, the first item in the array will be automatically translated to
            the active language at that moment.

            This will override the `content` property.
        content (Union[Unset, str]): This is the content that the assistant will say when this message is triggered.
    """

    type_: CustomMessageType
    contents: Union[Unset, list["TextContent"]] = UNSET
    content: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        contents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.contents, Unset):
            contents = []
            for contents_item_data in self.contents:
                contents_item = contents_item_data.to_dict()
                contents.append(contents_item)

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if contents is not UNSET:
            field_dict["contents"] = contents
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_content import TextContent

        d = dict(src_dict)
        type_ = CustomMessageType(d.pop("type"))

        contents = []
        _contents = d.pop("contents", UNSET)
        for contents_item_data in _contents or []:
            contents_item = TextContent.from_dict(contents_item_data)

            contents.append(contents_item)

        content = d.pop("content", UNSET)

        custom_message = cls(
            type_=type_,
            contents=contents,
            content=content,
        )

        custom_message.additional_properties = d
        return custom_message

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
