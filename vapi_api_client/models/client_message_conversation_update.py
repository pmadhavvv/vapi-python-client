from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_conversation_update_type import ClientMessageConversationUpdateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bot_message import BotMessage
    from ..models.open_ai_message import OpenAIMessage
    from ..models.system_message import SystemMessage
    from ..models.tool_call_message import ToolCallMessage
    from ..models.tool_call_result_message import ToolCallResultMessage
    from ..models.user_message import UserMessage


T = TypeVar("T", bound="ClientMessageConversationUpdate")


@_attrs_define
class ClientMessageConversationUpdate:
    """
    Attributes:
        type_ (ClientMessageConversationUpdateType): This is the type of the message. "conversation-update" is sent when
            an update is committed to the conversation history.
        messages_open_ai_formatted (list['OpenAIMessage']): This is the most up-to-date conversation history at the time
            the message is sent, formatted for OpenAI.
        messages (Union[Unset, list[Union['BotMessage', 'SystemMessage', 'ToolCallMessage', 'ToolCallResultMessage',
            'UserMessage']]]): This is the most up-to-date conversation history at the time the message is sent.
    """

    type_: ClientMessageConversationUpdateType
    messages_open_ai_formatted: list["OpenAIMessage"]
    messages: Union[
        Unset, list[Union["BotMessage", "SystemMessage", "ToolCallMessage", "ToolCallResultMessage", "UserMessage"]]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_message import BotMessage
        from ..models.system_message import SystemMessage
        from ..models.tool_call_message import ToolCallMessage
        from ..models.user_message import UserMessage

        type_ = self.type_.value

        messages_open_ai_formatted = []
        for messages_open_ai_formatted_item_data in self.messages_open_ai_formatted:
            messages_open_ai_formatted_item = messages_open_ai_formatted_item_data.to_dict()
            messages_open_ai_formatted.append(messages_open_ai_formatted_item)

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item: dict[str, Any]
                if isinstance(messages_item_data, UserMessage):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, SystemMessage):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, BotMessage):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, ToolCallMessage):
                    messages_item = messages_item_data.to_dict()
                else:
                    messages_item = messages_item_data.to_dict()

                messages.append(messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "messagesOpenAIFormatted": messages_open_ai_formatted,
            }
        )
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bot_message import BotMessage
        from ..models.open_ai_message import OpenAIMessage
        from ..models.system_message import SystemMessage
        from ..models.tool_call_message import ToolCallMessage
        from ..models.tool_call_result_message import ToolCallResultMessage
        from ..models.user_message import UserMessage

        d = dict(src_dict)
        type_ = ClientMessageConversationUpdateType(d.pop("type"))

        messages_open_ai_formatted = []
        _messages_open_ai_formatted = d.pop("messagesOpenAIFormatted")
        for messages_open_ai_formatted_item_data in _messages_open_ai_formatted:
            messages_open_ai_formatted_item = OpenAIMessage.from_dict(messages_open_ai_formatted_item_data)

            messages_open_ai_formatted.append(messages_open_ai_formatted_item)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:

            def _parse_messages_item(
                data: object,
            ) -> Union["BotMessage", "SystemMessage", "ToolCallMessage", "ToolCallResultMessage", "UserMessage"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_0 = UserMessage.from_dict(data)

                    return messages_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_1 = SystemMessage.from_dict(data)

                    return messages_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_2 = BotMessage.from_dict(data)

                    return messages_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_3 = ToolCallMessage.from_dict(data)

                    return messages_item_type_3
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                messages_item_type_4 = ToolCallResultMessage.from_dict(data)

                return messages_item_type_4

            messages_item = _parse_messages_item(messages_item_data)

            messages.append(messages_item)

        client_message_conversation_update = cls(
            type_=type_,
            messages_open_ai_formatted=messages_open_ai_formatted,
            messages=messages,
        )

        client_message_conversation_update.additional_properties = d
        return client_message_conversation_update

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
