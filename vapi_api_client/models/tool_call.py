from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tool_call_type import ToolCallType

if TYPE_CHECKING:
    from ..models.tool_call_function import ToolCallFunction


T = TypeVar("T", bound="ToolCall")


@_attrs_define
class ToolCall:
    """
    Attributes:
        type_ (ToolCallType): This is the type of tool the model called.
        function (ToolCallFunction):
        id (str): This is the unique identifier for the tool call.
    """

    type_: ToolCallType
    function: "ToolCallFunction"
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        function = self.function.to_dict()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "function": function,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tool_call_function import ToolCallFunction

        d = src_dict.copy()
        type_ = ToolCallType(d.pop("type"))

        function = ToolCallFunction.from_dict(d.pop("function"))

        id = d.pop("id")

        tool_call = cls(
            type_=type_,
            function=function,
            id=id,
        )

        tool_call.additional_properties = d
        return tool_call

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
