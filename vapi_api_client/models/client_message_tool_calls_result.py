from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_tool_calls_result_type import ClientMessageToolCallsResultType

if TYPE_CHECKING:
    from ..models.client_message_tool_calls_result_tool_call_result import ClientMessageToolCallsResultToolCallResult


T = TypeVar("T", bound="ClientMessageToolCallsResult")


@_attrs_define
class ClientMessageToolCallsResult:
    """
    Attributes:
        type_ (ClientMessageToolCallsResultType): This is the type of the message. "tool-calls-result" is sent to
            forward the result of a tool call to the client.
        tool_call_result (ClientMessageToolCallsResultToolCallResult): This is the result of the tool call.
    """

    type_: ClientMessageToolCallsResultType
    tool_call_result: "ClientMessageToolCallsResultToolCallResult"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        tool_call_result = self.tool_call_result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "toolCallResult": tool_call_result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.client_message_tool_calls_result_tool_call_result import (
            ClientMessageToolCallsResultToolCallResult,
        )

        d = src_dict.copy()
        type_ = ClientMessageToolCallsResultType(d.pop("type"))

        tool_call_result = ClientMessageToolCallsResultToolCallResult.from_dict(d.pop("toolCallResult"))

        client_message_tool_calls_result = cls(
            type_=type_,
            tool_call_result=tool_call_result,
        )

        client_message_tool_calls_result.additional_properties = d
        return client_message_tool_calls_result

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
