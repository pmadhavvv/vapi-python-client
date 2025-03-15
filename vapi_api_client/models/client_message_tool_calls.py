from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_tool_calls_type import ClientMessageToolCallsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bash_tool_with_tool_call import BashToolWithToolCall
    from ..models.computer_tool_with_tool_call import ComputerToolWithToolCall
    from ..models.function_tool_with_tool_call import FunctionToolWithToolCall
    from ..models.ghl_tool_with_tool_call import GhlToolWithToolCall
    from ..models.make_tool_with_tool_call import MakeToolWithToolCall
    from ..models.text_editor_tool_with_tool_call import TextEditorToolWithToolCall
    from ..models.tool_call import ToolCall


T = TypeVar("T", bound="ClientMessageToolCalls")


@_attrs_define
class ClientMessageToolCalls:
    """
    Attributes:
        tool_with_tool_call_list (list[Union['BashToolWithToolCall', 'ComputerToolWithToolCall',
            'FunctionToolWithToolCall', 'GhlToolWithToolCall', 'MakeToolWithToolCall', 'TextEditorToolWithToolCall']]): This
            is the list of tools calls that the model is requesting along with the original tool configuration.
        tool_call_list (list['ToolCall']): This is the list of tool calls that the model is requesting.
        type_ (Union[Unset, ClientMessageToolCallsType]): This is the type of the message. "tool-calls" is sent to call
            a tool.
    """

    tool_with_tool_call_list: list[
        Union[
            "BashToolWithToolCall",
            "ComputerToolWithToolCall",
            "FunctionToolWithToolCall",
            "GhlToolWithToolCall",
            "MakeToolWithToolCall",
            "TextEditorToolWithToolCall",
        ]
    ]
    tool_call_list: list["ToolCall"]
    type_: Union[Unset, ClientMessageToolCallsType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bash_tool_with_tool_call import BashToolWithToolCall
        from ..models.computer_tool_with_tool_call import ComputerToolWithToolCall
        from ..models.function_tool_with_tool_call import FunctionToolWithToolCall
        from ..models.ghl_tool_with_tool_call import GhlToolWithToolCall
        from ..models.make_tool_with_tool_call import MakeToolWithToolCall

        tool_with_tool_call_list = []
        for tool_with_tool_call_list_item_data in self.tool_with_tool_call_list:
            tool_with_tool_call_list_item: dict[str, Any]
            if isinstance(tool_with_tool_call_list_item_data, FunctionToolWithToolCall):
                tool_with_tool_call_list_item = tool_with_tool_call_list_item_data.to_dict()
            elif isinstance(tool_with_tool_call_list_item_data, GhlToolWithToolCall):
                tool_with_tool_call_list_item = tool_with_tool_call_list_item_data.to_dict()
            elif isinstance(tool_with_tool_call_list_item_data, MakeToolWithToolCall):
                tool_with_tool_call_list_item = tool_with_tool_call_list_item_data.to_dict()
            elif isinstance(tool_with_tool_call_list_item_data, BashToolWithToolCall):
                tool_with_tool_call_list_item = tool_with_tool_call_list_item_data.to_dict()
            elif isinstance(tool_with_tool_call_list_item_data, ComputerToolWithToolCall):
                tool_with_tool_call_list_item = tool_with_tool_call_list_item_data.to_dict()
            else:
                tool_with_tool_call_list_item = tool_with_tool_call_list_item_data.to_dict()

            tool_with_tool_call_list.append(tool_with_tool_call_list_item)

        tool_call_list = []
        for tool_call_list_item_data in self.tool_call_list:
            tool_call_list_item = tool_call_list_item_data.to_dict()
            tool_call_list.append(tool_call_list_item)

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "toolWithToolCallList": tool_with_tool_call_list,
                "toolCallList": tool_call_list,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.bash_tool_with_tool_call import BashToolWithToolCall
        from ..models.computer_tool_with_tool_call import ComputerToolWithToolCall
        from ..models.function_tool_with_tool_call import FunctionToolWithToolCall
        from ..models.ghl_tool_with_tool_call import GhlToolWithToolCall
        from ..models.make_tool_with_tool_call import MakeToolWithToolCall
        from ..models.text_editor_tool_with_tool_call import TextEditorToolWithToolCall
        from ..models.tool_call import ToolCall

        d = src_dict.copy()
        tool_with_tool_call_list = []
        _tool_with_tool_call_list = d.pop("toolWithToolCallList")
        for tool_with_tool_call_list_item_data in _tool_with_tool_call_list:

            def _parse_tool_with_tool_call_list_item(
                data: object,
            ) -> Union[
                "BashToolWithToolCall",
                "ComputerToolWithToolCall",
                "FunctionToolWithToolCall",
                "GhlToolWithToolCall",
                "MakeToolWithToolCall",
                "TextEditorToolWithToolCall",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tool_with_tool_call_list_item_type_0 = FunctionToolWithToolCall.from_dict(data)

                    return tool_with_tool_call_list_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tool_with_tool_call_list_item_type_1 = GhlToolWithToolCall.from_dict(data)

                    return tool_with_tool_call_list_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tool_with_tool_call_list_item_type_2 = MakeToolWithToolCall.from_dict(data)

                    return tool_with_tool_call_list_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tool_with_tool_call_list_item_type_3 = BashToolWithToolCall.from_dict(data)

                    return tool_with_tool_call_list_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tool_with_tool_call_list_item_type_4 = ComputerToolWithToolCall.from_dict(data)

                    return tool_with_tool_call_list_item_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                tool_with_tool_call_list_item_type_5 = TextEditorToolWithToolCall.from_dict(data)

                return tool_with_tool_call_list_item_type_5

            tool_with_tool_call_list_item = _parse_tool_with_tool_call_list_item(tool_with_tool_call_list_item_data)

            tool_with_tool_call_list.append(tool_with_tool_call_list_item)

        tool_call_list = []
        _tool_call_list = d.pop("toolCallList")
        for tool_call_list_item_data in _tool_call_list:
            tool_call_list_item = ToolCall.from_dict(tool_call_list_item_data)

            tool_call_list.append(tool_call_list_item)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ClientMessageToolCallsType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ClientMessageToolCallsType(_type_)

        client_message_tool_calls = cls(
            tool_with_tool_call_list=tool_with_tool_call_list,
            tool_call_list=tool_call_list,
            type_=type_,
        )

        client_message_tool_calls.additional_properties = d
        return client_message_tool_calls

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
