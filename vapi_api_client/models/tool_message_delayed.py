from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tool_message_delayed_type import ToolMessageDelayedType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition import Condition
    from ..models.text_content import TextContent


T = TypeVar("T", bound="ToolMessageDelayed")


@_attrs_define
class ToolMessageDelayed:
    """
    Attributes:
        type_ (ToolMessageDelayedType): This message is triggered when the tool call is delayed.

            There are the two things that can trigger this message:
            1. The user talks with the assistant while your server is processing the request. Default is "Sorry, a few more
            seconds."
            2. The server doesn't respond within `timingMilliseconds`.

            This message is never triggered for async tool calls.
        contents (Union[Unset, list['TextContent']]): This is an alternative to the `content` property. It allows to
            specify variants of the same content, one per language.

            Usage:
            - If your assistants are multilingual, you can provide content for each language.
            - If you don't provide content for a language, the first item in the array will be automatically translated to
            the active language at that moment.

            This will override the `content` property.
        timing_milliseconds (Union[Unset, float]): The number of milliseconds to wait for the server response before
            saying this message. Example: 1000.
        content (Union[Unset, str]): This is the content that the assistant says when this message is triggered.
        conditions (Union[Unset, list['Condition']]): This is an optional array of conditions that the tool call
            arguments must meet in order for this message to be triggered.
    """

    type_: ToolMessageDelayedType
    contents: Union[Unset, list["TextContent"]] = UNSET
    timing_milliseconds: Union[Unset, float] = UNSET
    content: Union[Unset, str] = UNSET
    conditions: Union[Unset, list["Condition"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        contents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.contents, Unset):
            contents = []
            for contents_item_data in self.contents:
                contents_item = contents_item_data.to_dict()
                contents.append(contents_item)

        timing_milliseconds = self.timing_milliseconds

        content = self.content

        conditions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if contents is not UNSET:
            field_dict["contents"] = contents
        if timing_milliseconds is not UNSET:
            field_dict["timingMilliseconds"] = timing_milliseconds
        if content is not UNSET:
            field_dict["content"] = content
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.condition import Condition
        from ..models.text_content import TextContent

        d = src_dict.copy()
        type_ = ToolMessageDelayedType(d.pop("type"))

        contents = []
        _contents = d.pop("contents", UNSET)
        for contents_item_data in _contents or []:
            contents_item = TextContent.from_dict(contents_item_data)

            contents.append(contents_item)

        timing_milliseconds = d.pop("timingMilliseconds", UNSET)

        content = d.pop("content", UNSET)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = Condition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        tool_message_delayed = cls(
            type_=type_,
            contents=contents,
            timing_milliseconds=timing_milliseconds,
            content=content,
            conditions=conditions,
        )

        tool_message_delayed.additional_properties = d
        return tool_message_delayed

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
