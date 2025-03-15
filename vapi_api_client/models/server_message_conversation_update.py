from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_message_conversation_update_type import ServerMessageConversationUpdateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artifact import Artifact
    from ..models.bot_message import BotMessage
    from ..models.call import Call
    from ..models.create_assistant_dto import CreateAssistantDTO
    from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
    from ..models.create_customer_dto import CreateCustomerDTO
    from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
    from ..models.create_vapi_phone_number_dto import CreateVapiPhoneNumberDTO
    from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
    from ..models.open_ai_message import OpenAIMessage
    from ..models.system_message import SystemMessage
    from ..models.tool_call_message import ToolCallMessage
    from ..models.tool_call_result_message import ToolCallResultMessage
    from ..models.user_message import UserMessage


T = TypeVar("T", bound="ServerMessageConversationUpdate")


@_attrs_define
class ServerMessageConversationUpdate:
    """
    Attributes:
        type_ (ServerMessageConversationUpdateType): This is the type of the message. "conversation-update" is sent when
            an update is committed to the conversation history.
        messages_open_ai_formatted (list['OpenAIMessage']): This is the most up-to-date conversation history at the time
            the message is sent, formatted for OpenAI.
        phone_number (Union['CreateByoPhoneNumberDTO', 'CreateTwilioPhoneNumberDTO', 'CreateVapiPhoneNumberDTO',
            'CreateVonagePhoneNumberDTO', Unset]): This is the phone number associated with the call.

            This matches one of the following:
            - `call.phoneNumber`,
            - `call.phoneNumberId`.
        messages (Union[Unset, list[Union['BotMessage', 'SystemMessage', 'ToolCallMessage', 'ToolCallResultMessage',
            'UserMessage']]]): This is the most up-to-date conversation history at the time the message is sent.
        timestamp (Union[Unset, str]): This is the ISO-8601 formatted timestamp of when the message was sent.
        artifact (Union[Unset, Artifact]):
        assistant (Union[Unset, CreateAssistantDTO]):
        customer (Union[Unset, CreateCustomerDTO]):
        call (Union[Unset, Call]):
    """

    type_: ServerMessageConversationUpdateType
    messages_open_ai_formatted: list["OpenAIMessage"]
    phone_number: Union[
        "CreateByoPhoneNumberDTO",
        "CreateTwilioPhoneNumberDTO",
        "CreateVapiPhoneNumberDTO",
        "CreateVonagePhoneNumberDTO",
        Unset,
    ] = UNSET
    messages: Union[
        Unset, list[Union["BotMessage", "SystemMessage", "ToolCallMessage", "ToolCallResultMessage", "UserMessage"]]
    ] = UNSET
    timestamp: Union[Unset, str] = UNSET
    artifact: Union[Unset, "Artifact"] = UNSET
    assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    customer: Union[Unset, "CreateCustomerDTO"] = UNSET
    call: Union[Unset, "Call"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_message import BotMessage
        from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
        from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
        from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
        from ..models.system_message import SystemMessage
        from ..models.tool_call_message import ToolCallMessage
        from ..models.user_message import UserMessage

        type_ = self.type_.value

        messages_open_ai_formatted = []
        for messages_open_ai_formatted_item_data in self.messages_open_ai_formatted:
            messages_open_ai_formatted_item = messages_open_ai_formatted_item_data.to_dict()
            messages_open_ai_formatted.append(messages_open_ai_formatted_item)

        phone_number: Union[Unset, dict[str, Any]]
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        elif isinstance(self.phone_number, CreateByoPhoneNumberDTO):
            phone_number = self.phone_number.to_dict()
        elif isinstance(self.phone_number, CreateTwilioPhoneNumberDTO):
            phone_number = self.phone_number.to_dict()
        elif isinstance(self.phone_number, CreateVonagePhoneNumberDTO):
            phone_number = self.phone_number.to_dict()
        else:
            phone_number = self.phone_number.to_dict()

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

        timestamp = self.timestamp

        artifact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artifact, Unset):
            artifact = self.artifact.to_dict()

        assistant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assistant, Unset):
            assistant = self.assistant.to_dict()

        customer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        call: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.call, Unset):
            call = self.call.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "messagesOpenAIFormatted": messages_open_ai_formatted,
            }
        )
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if messages is not UNSET:
            field_dict["messages"] = messages
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if artifact is not UNSET:
            field_dict["artifact"] = artifact
        if assistant is not UNSET:
            field_dict["assistant"] = assistant
        if customer is not UNSET:
            field_dict["customer"] = customer
        if call is not UNSET:
            field_dict["call"] = call

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.artifact import Artifact
        from ..models.bot_message import BotMessage
        from ..models.call import Call
        from ..models.create_assistant_dto import CreateAssistantDTO
        from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
        from ..models.create_customer_dto import CreateCustomerDTO
        from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
        from ..models.create_vapi_phone_number_dto import CreateVapiPhoneNumberDTO
        from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
        from ..models.open_ai_message import OpenAIMessage
        from ..models.system_message import SystemMessage
        from ..models.tool_call_message import ToolCallMessage
        from ..models.tool_call_result_message import ToolCallResultMessage
        from ..models.user_message import UserMessage

        d = src_dict.copy()
        type_ = ServerMessageConversationUpdateType(d.pop("type"))

        messages_open_ai_formatted = []
        _messages_open_ai_formatted = d.pop("messagesOpenAIFormatted")
        for messages_open_ai_formatted_item_data in _messages_open_ai_formatted:
            messages_open_ai_formatted_item = OpenAIMessage.from_dict(messages_open_ai_formatted_item_data)

            messages_open_ai_formatted.append(messages_open_ai_formatted_item)

        def _parse_phone_number(
            data: object,
        ) -> Union[
            "CreateByoPhoneNumberDTO",
            "CreateTwilioPhoneNumberDTO",
            "CreateVapiPhoneNumberDTO",
            "CreateVonagePhoneNumberDTO",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                phone_number_type_0 = CreateByoPhoneNumberDTO.from_dict(data)

                return phone_number_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                phone_number_type_1 = CreateTwilioPhoneNumberDTO.from_dict(data)

                return phone_number_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                phone_number_type_2 = CreateVonagePhoneNumberDTO.from_dict(data)

                return phone_number_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            phone_number_type_3 = CreateVapiPhoneNumberDTO.from_dict(data)

            return phone_number_type_3

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

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

        timestamp = d.pop("timestamp", UNSET)

        _artifact = d.pop("artifact", UNSET)
        artifact: Union[Unset, Artifact]
        if isinstance(_artifact, Unset):
            artifact = UNSET
        else:
            artifact = Artifact.from_dict(_artifact)

        _assistant = d.pop("assistant", UNSET)
        assistant: Union[Unset, CreateAssistantDTO]
        if isinstance(_assistant, Unset):
            assistant = UNSET
        else:
            assistant = CreateAssistantDTO.from_dict(_assistant)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, CreateCustomerDTO]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CreateCustomerDTO.from_dict(_customer)

        _call = d.pop("call", UNSET)
        call: Union[Unset, Call]
        if isinstance(_call, Unset):
            call = UNSET
        else:
            call = Call.from_dict(_call)

        server_message_conversation_update = cls(
            type_=type_,
            messages_open_ai_formatted=messages_open_ai_formatted,
            phone_number=phone_number,
            messages=messages,
            timestamp=timestamp,
            artifact=artifact,
            assistant=assistant,
            customer=customer,
            call=call,
        )

        server_message_conversation_update.additional_properties = d
        return server_message_conversation_update

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
