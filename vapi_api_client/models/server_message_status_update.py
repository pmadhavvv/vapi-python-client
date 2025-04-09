from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_message_status_update_ended_reason import ServerMessageStatusUpdateEndedReason
from ..models.server_message_status_update_status import ServerMessageStatusUpdateStatus
from ..models.server_message_status_update_type import ServerMessageStatusUpdateType
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
    from ..models.server_message_status_update_inbound_phone_call_debugging_artifacts import (
        ServerMessageStatusUpdateInboundPhoneCallDebuggingArtifacts,
    )
    from ..models.system_message import SystemMessage
    from ..models.tool_call_message import ToolCallMessage
    from ..models.tool_call_result_message import ToolCallResultMessage
    from ..models.transfer_destination_number import TransferDestinationNumber
    from ..models.transfer_destination_sip import TransferDestinationSip
    from ..models.user_message import UserMessage


T = TypeVar("T", bound="ServerMessageStatusUpdate")


@_attrs_define
class ServerMessageStatusUpdate:
    """
    Attributes:
        type_ (ServerMessageStatusUpdateType): This is the type of the message. "status-update" is sent whenever the
            `call.status` changes.
        status (ServerMessageStatusUpdateStatus): This is the status of the call.
        phone_number (Union['CreateByoPhoneNumberDTO', 'CreateTwilioPhoneNumberDTO', 'CreateVapiPhoneNumberDTO',
            'CreateVonagePhoneNumberDTO', Unset]): This is the phone number associated with the call.

            This matches one of the following:
            - `call.phoneNumber`,
            - `call.phoneNumberId`.
        ended_reason (Union[Unset, ServerMessageStatusUpdateEndedReason]): This is the reason the call ended. This is
            only sent if the status is "ended".
        messages (Union[Unset, list[Union['BotMessage', 'SystemMessage', 'ToolCallMessage', 'ToolCallResultMessage',
            'UserMessage']]]): These are the conversation messages of the call. This is only sent if the status is
            "forwarding".
        messages_open_ai_formatted (Union[Unset, list['OpenAIMessage']]): These are the conversation messages of the
            call. This is only sent if the status is "forwarding".
        destination (Union['TransferDestinationNumber', 'TransferDestinationSip', Unset]): This is the destination the
            call is being transferred to. This is only sent if the status is "forwarding".
        timestamp (Union[Unset, str]): This is the ISO-8601 formatted timestamp of when the message was sent.
        artifact (Union[Unset, Artifact]):
        assistant (Union[Unset, CreateAssistantDTO]):
        customer (Union[Unset, CreateCustomerDTO]):
        call (Union[Unset, Call]):
        transcript (Union[Unset, str]): This is the transcript of the call. This is only sent if the status is
            "forwarding".
        summary (Union[Unset, str]): This is the summary of the call. This is only sent if the status is "forwarding".
        inbound_phone_call_debugging_artifacts (Union[Unset,
            ServerMessageStatusUpdateInboundPhoneCallDebuggingArtifacts]): This is the inbound phone call debugging
            artifacts. This is only sent if the status is "ended" and there was an error accepting the inbound phone call.

            This will include any errors related to the "assistant-request" if one was made.
    """

    type_: ServerMessageStatusUpdateType
    status: ServerMessageStatusUpdateStatus
    phone_number: Union[
        "CreateByoPhoneNumberDTO",
        "CreateTwilioPhoneNumberDTO",
        "CreateVapiPhoneNumberDTO",
        "CreateVonagePhoneNumberDTO",
        Unset,
    ] = UNSET
    ended_reason: Union[Unset, ServerMessageStatusUpdateEndedReason] = UNSET
    messages: Union[
        Unset, list[Union["BotMessage", "SystemMessage", "ToolCallMessage", "ToolCallResultMessage", "UserMessage"]]
    ] = UNSET
    messages_open_ai_formatted: Union[Unset, list["OpenAIMessage"]] = UNSET
    destination: Union["TransferDestinationNumber", "TransferDestinationSip", Unset] = UNSET
    timestamp: Union[Unset, str] = UNSET
    artifact: Union[Unset, "Artifact"] = UNSET
    assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    customer: Union[Unset, "CreateCustomerDTO"] = UNSET
    call: Union[Unset, "Call"] = UNSET
    transcript: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    inbound_phone_call_debugging_artifacts: Union[
        Unset, "ServerMessageStatusUpdateInboundPhoneCallDebuggingArtifacts"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_message import BotMessage
        from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
        from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
        from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
        from ..models.system_message import SystemMessage
        from ..models.tool_call_message import ToolCallMessage
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.user_message import UserMessage

        type_ = self.type_.value

        status = self.status.value

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

        ended_reason: Union[Unset, str] = UNSET
        if not isinstance(self.ended_reason, Unset):
            ended_reason = self.ended_reason.value

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

        messages_open_ai_formatted: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages_open_ai_formatted, Unset):
            messages_open_ai_formatted = []
            for messages_open_ai_formatted_item_data in self.messages_open_ai_formatted:
                messages_open_ai_formatted_item = messages_open_ai_formatted_item_data.to_dict()
                messages_open_ai_formatted.append(messages_open_ai_formatted_item)

        destination: Union[Unset, dict[str, Any]]
        if isinstance(self.destination, Unset):
            destination = UNSET
        elif isinstance(self.destination, TransferDestinationNumber):
            destination = self.destination.to_dict()
        else:
            destination = self.destination.to_dict()

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

        transcript = self.transcript

        summary = self.summary

        inbound_phone_call_debugging_artifacts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inbound_phone_call_debugging_artifacts, Unset):
            inbound_phone_call_debugging_artifacts = self.inbound_phone_call_debugging_artifacts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "status": status,
            }
        )
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if ended_reason is not UNSET:
            field_dict["endedReason"] = ended_reason
        if messages is not UNSET:
            field_dict["messages"] = messages
        if messages_open_ai_formatted is not UNSET:
            field_dict["messagesOpenAIFormatted"] = messages_open_ai_formatted
        if destination is not UNSET:
            field_dict["destination"] = destination
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
        if transcript is not UNSET:
            field_dict["transcript"] = transcript
        if summary is not UNSET:
            field_dict["summary"] = summary
        if inbound_phone_call_debugging_artifacts is not UNSET:
            field_dict["inboundPhoneCallDebuggingArtifacts"] = inbound_phone_call_debugging_artifacts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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
        from ..models.server_message_status_update_inbound_phone_call_debugging_artifacts import (
            ServerMessageStatusUpdateInboundPhoneCallDebuggingArtifacts,
        )
        from ..models.system_message import SystemMessage
        from ..models.tool_call_message import ToolCallMessage
        from ..models.tool_call_result_message import ToolCallResultMessage
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_sip import TransferDestinationSip
        from ..models.user_message import UserMessage

        d = dict(src_dict)
        type_ = ServerMessageStatusUpdateType(d.pop("type"))

        status = ServerMessageStatusUpdateStatus(d.pop("status"))

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

        _ended_reason = d.pop("endedReason", UNSET)
        ended_reason: Union[Unset, ServerMessageStatusUpdateEndedReason]
        if isinstance(_ended_reason, Unset):
            ended_reason = UNSET
        else:
            ended_reason = ServerMessageStatusUpdateEndedReason(_ended_reason)

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

        messages_open_ai_formatted = []
        _messages_open_ai_formatted = d.pop("messagesOpenAIFormatted", UNSET)
        for messages_open_ai_formatted_item_data in _messages_open_ai_formatted or []:
            messages_open_ai_formatted_item = OpenAIMessage.from_dict(messages_open_ai_formatted_item_data)

            messages_open_ai_formatted.append(messages_open_ai_formatted_item)

        def _parse_destination(data: object) -> Union["TransferDestinationNumber", "TransferDestinationSip", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                destination_type_0 = TransferDestinationNumber.from_dict(data)

                return destination_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            destination_type_1 = TransferDestinationSip.from_dict(data)

            return destination_type_1

        destination = _parse_destination(d.pop("destination", UNSET))

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

        transcript = d.pop("transcript", UNSET)

        summary = d.pop("summary", UNSET)

        _inbound_phone_call_debugging_artifacts = d.pop("inboundPhoneCallDebuggingArtifacts", UNSET)
        inbound_phone_call_debugging_artifacts: Union[
            Unset, ServerMessageStatusUpdateInboundPhoneCallDebuggingArtifacts
        ]
        if isinstance(_inbound_phone_call_debugging_artifacts, Unset):
            inbound_phone_call_debugging_artifacts = UNSET
        else:
            inbound_phone_call_debugging_artifacts = (
                ServerMessageStatusUpdateInboundPhoneCallDebuggingArtifacts.from_dict(
                    _inbound_phone_call_debugging_artifacts
                )
            )

        server_message_status_update = cls(
            type_=type_,
            status=status,
            phone_number=phone_number,
            ended_reason=ended_reason,
            messages=messages,
            messages_open_ai_formatted=messages_open_ai_formatted,
            destination=destination,
            timestamp=timestamp,
            artifact=artifact,
            assistant=assistant,
            customer=customer,
            call=call,
            transcript=transcript,
            summary=summary,
            inbound_phone_call_debugging_artifacts=inbound_phone_call_debugging_artifacts,
        )

        server_message_status_update.additional_properties = d
        return server_message_status_update

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
