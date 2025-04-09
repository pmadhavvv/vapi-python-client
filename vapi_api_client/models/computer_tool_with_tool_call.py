from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.computer_tool_with_tool_call_name import ComputerToolWithToolCallName
from ..models.computer_tool_with_tool_call_sub_type import ComputerToolWithToolCallSubType
from ..models.computer_tool_with_tool_call_type import ComputerToolWithToolCallType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_ai_function import OpenAIFunction
    from ..models.server import Server
    from ..models.tool_call import ToolCall
    from ..models.tool_message_complete import ToolMessageComplete
    from ..models.tool_message_delayed import ToolMessageDelayed
    from ..models.tool_message_failed import ToolMessageFailed
    from ..models.tool_message_start import ToolMessageStart


T = TypeVar("T", bound="ComputerToolWithToolCall")


@_attrs_define
class ComputerToolWithToolCall:
    """
    Attributes:
        type_ (ComputerToolWithToolCallType): The type of tool. "computer" for Computer tool.
        sub_type (ComputerToolWithToolCallSubType): The sub type of tool.
        tool_call (ToolCall):
        name (ComputerToolWithToolCallName): The name of the tool, fixed to 'computer'
        display_width_px (float): The display width in pixels
        display_height_px (float): The display height in pixels
        async_ (Union[Unset, bool]): This determines if the tool is async.

            If async, the assistant will move forward without waiting for your server to respond. This is useful if you just
            want to trigger something on your server.

            If sync, the assistant will wait for your server to respond. This is useful if want assistant to respond with
            the result from your server.

            Defaults to synchronous (`false`).
        messages (Union[Unset, list[Union['ToolMessageComplete', 'ToolMessageDelayed', 'ToolMessageFailed',
            'ToolMessageStart']]]): These are the messages that will be spoken to the user as the tool is running.

            For some tools, this is auto-filled based on special fields like `tool.destinations`. For others like the
            function tool, these can be custom configured.
        display_number (Union[Unset, float]): Optional display number
        function (Union[Unset, OpenAIFunction]):
        server (Union[Unset, Server]):
    """

    type_: ComputerToolWithToolCallType
    sub_type: ComputerToolWithToolCallSubType
    tool_call: "ToolCall"
    name: ComputerToolWithToolCallName
    display_width_px: float
    display_height_px: float
    async_: Union[Unset, bool] = UNSET
    messages: Union[
        Unset, list[Union["ToolMessageComplete", "ToolMessageDelayed", "ToolMessageFailed", "ToolMessageStart"]]
    ] = UNSET
    display_number: Union[Unset, float] = UNSET
    function: Union[Unset, "OpenAIFunction"] = UNSET
    server: Union[Unset, "Server"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_message_complete import ToolMessageComplete
        from ..models.tool_message_failed import ToolMessageFailed
        from ..models.tool_message_start import ToolMessageStart

        type_ = self.type_.value

        sub_type = self.sub_type.value

        tool_call = self.tool_call.to_dict()

        name = self.name.value

        display_width_px = self.display_width_px

        display_height_px = self.display_height_px

        async_ = self.async_

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item: dict[str, Any]
                if isinstance(messages_item_data, ToolMessageStart):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, ToolMessageComplete):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, ToolMessageFailed):
                    messages_item = messages_item_data.to_dict()
                else:
                    messages_item = messages_item_data.to_dict()

                messages.append(messages_item)

        display_number = self.display_number

        function: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.function, Unset):
            function = self.function.to_dict()

        server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "subType": sub_type,
                "toolCall": tool_call,
                "name": name,
                "displayWidthPx": display_width_px,
                "displayHeightPx": display_height_px,
            }
        )
        if async_ is not UNSET:
            field_dict["async"] = async_
        if messages is not UNSET:
            field_dict["messages"] = messages
        if display_number is not UNSET:
            field_dict["displayNumber"] = display_number
        if function is not UNSET:
            field_dict["function"] = function
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_ai_function import OpenAIFunction
        from ..models.server import Server
        from ..models.tool_call import ToolCall
        from ..models.tool_message_complete import ToolMessageComplete
        from ..models.tool_message_delayed import ToolMessageDelayed
        from ..models.tool_message_failed import ToolMessageFailed
        from ..models.tool_message_start import ToolMessageStart

        d = dict(src_dict)
        type_ = ComputerToolWithToolCallType(d.pop("type"))

        sub_type = ComputerToolWithToolCallSubType(d.pop("subType"))

        tool_call = ToolCall.from_dict(d.pop("toolCall"))

        name = ComputerToolWithToolCallName(d.pop("name"))

        display_width_px = d.pop("displayWidthPx")

        display_height_px = d.pop("displayHeightPx")

        async_ = d.pop("async", UNSET)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:

            def _parse_messages_item(
                data: object,
            ) -> Union["ToolMessageComplete", "ToolMessageDelayed", "ToolMessageFailed", "ToolMessageStart"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_0 = ToolMessageStart.from_dict(data)

                    return messages_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_1 = ToolMessageComplete.from_dict(data)

                    return messages_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_2 = ToolMessageFailed.from_dict(data)

                    return messages_item_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                messages_item_type_3 = ToolMessageDelayed.from_dict(data)

                return messages_item_type_3

            messages_item = _parse_messages_item(messages_item_data)

            messages.append(messages_item)

        display_number = d.pop("displayNumber", UNSET)

        _function = d.pop("function", UNSET)
        function: Union[Unset, OpenAIFunction]
        if isinstance(_function, Unset):
            function = UNSET
        else:
            function = OpenAIFunction.from_dict(_function)

        _server = d.pop("server", UNSET)
        server: Union[Unset, Server]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = Server.from_dict(_server)

        computer_tool_with_tool_call = cls(
            type_=type_,
            sub_type=sub_type,
            tool_call=tool_call,
            name=name,
            display_width_px=display_width_px,
            display_height_px=display_height_px,
            async_=async_,
            messages=messages,
            display_number=display_number,
            function=function,
            server=server,
        )

        computer_tool_with_tool_call.additional_properties = d
        return computer_tool_with_tool_call

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
