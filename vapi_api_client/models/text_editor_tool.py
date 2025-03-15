import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.text_editor_tool_name import TextEditorToolName
from ..models.text_editor_tool_sub_type import TextEditorToolSubType
from ..models.text_editor_tool_type import TextEditorToolType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_ai_function import OpenAIFunction
    from ..models.server import Server
    from ..models.tool_message_complete import ToolMessageComplete
    from ..models.tool_message_delayed import ToolMessageDelayed
    from ..models.tool_message_failed import ToolMessageFailed
    from ..models.tool_message_start import ToolMessageStart


T = TypeVar("T", bound="TextEditorTool")


@_attrs_define
class TextEditorTool:
    """
    Attributes:
        type_ (TextEditorToolType): The type of tool. "textEditor" for Text Editor tool.
        sub_type (TextEditorToolSubType): The sub type of tool.
        id (str): This is the unique identifier for the tool.
        org_id (str): This is the unique identifier for the organization that this tool belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the tool was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the tool was last updated.
        name (TextEditorToolName): The name of the tool, fixed to 'str_replace_editor'
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
        function (Union[Unset, OpenAIFunction]):
        server (Union[Unset, Server]):
    """

    type_: TextEditorToolType
    sub_type: TextEditorToolSubType
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: TextEditorToolName
    async_: Union[Unset, bool] = UNSET
    messages: Union[
        Unset, list[Union["ToolMessageComplete", "ToolMessageDelayed", "ToolMessageFailed", "ToolMessageStart"]]
    ] = UNSET
    function: Union[Unset, "OpenAIFunction"] = UNSET
    server: Union[Unset, "Server"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_message_complete import ToolMessageComplete
        from ..models.tool_message_failed import ToolMessageFailed
        from ..models.tool_message_start import ToolMessageStart

        type_ = self.type_.value

        sub_type = self.sub_type.value

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name.value

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
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "name": name,
            }
        )
        if async_ is not UNSET:
            field_dict["async"] = async_
        if messages is not UNSET:
            field_dict["messages"] = messages
        if function is not UNSET:
            field_dict["function"] = function
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.open_ai_function import OpenAIFunction
        from ..models.server import Server
        from ..models.tool_message_complete import ToolMessageComplete
        from ..models.tool_message_delayed import ToolMessageDelayed
        from ..models.tool_message_failed import ToolMessageFailed
        from ..models.tool_message_start import ToolMessageStart

        d = src_dict.copy()
        type_ = TextEditorToolType(d.pop("type"))

        sub_type = TextEditorToolSubType(d.pop("subType"))

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        name = TextEditorToolName(d.pop("name"))

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

        text_editor_tool = cls(
            type_=type_,
            sub_type=sub_type,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            async_=async_,
            messages=messages,
            function=function,
            server=server,
        )

        text_editor_tool.additional_properties = d
        return text_editor_tool

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
