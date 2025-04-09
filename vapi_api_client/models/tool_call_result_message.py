from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ToolCallResultMessage")


@_attrs_define
class ToolCallResultMessage:
    """
    Attributes:
        role (str): The role of the tool call result in the conversation.
        tool_call_id (str): The ID of the tool call.
        name (str): The name of the tool that returned the result.
        result (str): The result of the tool call in JSON format.
        time (float): The timestamp when the message was sent.
        seconds_from_start (float): The number of seconds from the start of the conversation.
    """

    role: str
    tool_call_id: str
    name: str
    result: str
    time: float
    seconds_from_start: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        tool_call_id = self.tool_call_id

        name = self.name

        result = self.result

        time = self.time

        seconds_from_start = self.seconds_from_start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "toolCallId": tool_call_id,
                "name": name,
                "result": result,
                "time": time,
                "secondsFromStart": seconds_from_start,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = d.pop("role")

        tool_call_id = d.pop("toolCallId")

        name = d.pop("name")

        result = d.pop("result")

        time = d.pop("time")

        seconds_from_start = d.pop("secondsFromStart")

        tool_call_result_message = cls(
            role=role,
            tool_call_id=tool_call_id,
            name=name,
            result=result,
            time=time,
            seconds_from_start=seconds_from_start,
        )

        tool_call_result_message.additional_properties = d
        return tool_call_result_message

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
