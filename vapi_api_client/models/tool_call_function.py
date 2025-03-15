from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tool_call_function_arguments import ToolCallFunctionArguments


T = TypeVar("T", bound="ToolCallFunction")


@_attrs_define
class ToolCallFunction:
    """
    Attributes:
        name (str): This is the name of the function the model called.
        arguments (ToolCallFunctionArguments): These are the arguments that the function was called with.
    """

    name: str
    arguments: "ToolCallFunctionArguments"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        arguments = self.arguments.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "arguments": arguments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tool_call_function_arguments import ToolCallFunctionArguments

        d = src_dict.copy()
        name = d.pop("name")

        arguments = ToolCallFunctionArguments.from_dict(d.pop("arguments"))

        tool_call_function = cls(
            name=name,
            arguments=arguments,
        )

        tool_call_function.additional_properties = d
        return tool_call_function

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
