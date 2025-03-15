from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tool_call_message_tool_calls_item import ToolCallMessageToolCallsItem


T = TypeVar("T", bound="ToolCallMessage")


@_attrs_define
class ToolCallMessage:
    """
    Attributes:
        role (str): The role of the tool call in the conversation.
        tool_calls (list['ToolCallMessageToolCallsItem']): The list of tool calls made during the conversation.
        message (str): The message content for the tool call.
        time (float): The timestamp when the message was sent.
        seconds_from_start (float): The number of seconds from the start of the conversation.
    """

    role: str
    tool_calls: list["ToolCallMessageToolCallsItem"]
    message: str
    time: float
    seconds_from_start: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        tool_calls = []
        for tool_calls_item_data in self.tool_calls:
            tool_calls_item = tool_calls_item_data.to_dict()
            tool_calls.append(tool_calls_item)

        message = self.message

        time = self.time

        seconds_from_start = self.seconds_from_start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "toolCalls": tool_calls,
                "message": message,
                "time": time,
                "secondsFromStart": seconds_from_start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tool_call_message_tool_calls_item import ToolCallMessageToolCallsItem

        d = src_dict.copy()
        role = d.pop("role")

        tool_calls = []
        _tool_calls = d.pop("toolCalls")
        for tool_calls_item_data in _tool_calls:
            tool_calls_item = ToolCallMessageToolCallsItem.from_dict(tool_calls_item_data)

            tool_calls.append(tool_calls_item)

        message = d.pop("message")

        time = d.pop("time")

        seconds_from_start = d.pop("secondsFromStart")

        tool_call_message = cls(
            role=role,
            tool_calls=tool_calls,
            message=message,
            time=time,
            seconds_from_start=seconds_from_start,
        )

        tool_call_message.additional_properties = d
        return tool_call_message

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
