from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_message_assistant_request import ServerMessageAssistantRequest
    from ..models.server_message_conversation_update import ServerMessageConversationUpdate
    from ..models.server_message_end_of_call_report import ServerMessageEndOfCallReport
    from ..models.server_message_hang import ServerMessageHang
    from ..models.server_message_knowledge_base_request import ServerMessageKnowledgeBaseRequest
    from ..models.server_message_language_change_detected import ServerMessageLanguageChangeDetected
    from ..models.server_message_model_output import ServerMessageModelOutput
    from ..models.server_message_phone_call_control import ServerMessagePhoneCallControl
    from ..models.server_message_speech_update import ServerMessageSpeechUpdate
    from ..models.server_message_status_update import ServerMessageStatusUpdate
    from ..models.server_message_tool_calls import ServerMessageToolCalls
    from ..models.server_message_transcript import ServerMessageTranscript
    from ..models.server_message_transfer_destination_request import ServerMessageTransferDestinationRequest
    from ..models.server_message_transfer_update import ServerMessageTransferUpdate
    from ..models.server_message_user_interrupted import ServerMessageUserInterrupted
    from ..models.server_message_voice_input import ServerMessageVoiceInput
    from ..models.server_message_voice_request import ServerMessageVoiceRequest


T = TypeVar("T", bound="ServerMessage")


@_attrs_define
class ServerMessage:
    """
    Attributes:
        message (Union['ServerMessageAssistantRequest', 'ServerMessageConversationUpdate',
            'ServerMessageEndOfCallReport', 'ServerMessageHang', 'ServerMessageKnowledgeBaseRequest',
            'ServerMessageLanguageChangeDetected', 'ServerMessageModelOutput', 'ServerMessagePhoneCallControl',
            'ServerMessageSpeechUpdate', 'ServerMessageStatusUpdate', 'ServerMessageToolCalls', 'ServerMessageTranscript',
            'ServerMessageTransferDestinationRequest', 'ServerMessageTransferUpdate', 'ServerMessageUserInterrupted',
            'ServerMessageVoiceInput', 'ServerMessageVoiceRequest']): These are all the messages that can be sent to your
            server before, after and during the call. Configure the messages you'd like to receive in
            `assistant.serverMessages`.

            The server where the message is sent is determined by the following precedence order:

            1. `tool.server.url` (if configured, and only for "tool-calls" message)
            2. `assistant.serverUrl` (if configure)
            3. `phoneNumber.serverUrl` (if configured)
            4. `org.serverUrl` (if configured)
    """

    message: Union[
        "ServerMessageAssistantRequest",
        "ServerMessageConversationUpdate",
        "ServerMessageEndOfCallReport",
        "ServerMessageHang",
        "ServerMessageKnowledgeBaseRequest",
        "ServerMessageLanguageChangeDetected",
        "ServerMessageModelOutput",
        "ServerMessagePhoneCallControl",
        "ServerMessageSpeechUpdate",
        "ServerMessageStatusUpdate",
        "ServerMessageToolCalls",
        "ServerMessageTranscript",
        "ServerMessageTransferDestinationRequest",
        "ServerMessageTransferUpdate",
        "ServerMessageUserInterrupted",
        "ServerMessageVoiceInput",
        "ServerMessageVoiceRequest",
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_message_assistant_request import ServerMessageAssistantRequest
        from ..models.server_message_conversation_update import ServerMessageConversationUpdate
        from ..models.server_message_end_of_call_report import ServerMessageEndOfCallReport
        from ..models.server_message_hang import ServerMessageHang
        from ..models.server_message_knowledge_base_request import ServerMessageKnowledgeBaseRequest
        from ..models.server_message_language_change_detected import ServerMessageLanguageChangeDetected
        from ..models.server_message_model_output import ServerMessageModelOutput
        from ..models.server_message_phone_call_control import ServerMessagePhoneCallControl
        from ..models.server_message_speech_update import ServerMessageSpeechUpdate
        from ..models.server_message_status_update import ServerMessageStatusUpdate
        from ..models.server_message_tool_calls import ServerMessageToolCalls
        from ..models.server_message_transcript import ServerMessageTranscript
        from ..models.server_message_transfer_destination_request import ServerMessageTransferDestinationRequest
        from ..models.server_message_transfer_update import ServerMessageTransferUpdate
        from ..models.server_message_user_interrupted import ServerMessageUserInterrupted
        from ..models.server_message_voice_input import ServerMessageVoiceInput

        message: dict[str, Any]
        if isinstance(self.message, ServerMessageAssistantRequest):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageConversationUpdate):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageEndOfCallReport):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageHang):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageKnowledgeBaseRequest):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageModelOutput):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessagePhoneCallControl):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageSpeechUpdate):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageStatusUpdate):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageToolCalls):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageTransferDestinationRequest):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageTransferUpdate):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageTranscript):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageUserInterrupted):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageLanguageChangeDetected):
            message = self.message.to_dict()
        elif isinstance(self.message, ServerMessageVoiceInput):
            message = self.message.to_dict()
        else:
            message = self.message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.server_message_assistant_request import ServerMessageAssistantRequest
        from ..models.server_message_conversation_update import ServerMessageConversationUpdate
        from ..models.server_message_end_of_call_report import ServerMessageEndOfCallReport
        from ..models.server_message_hang import ServerMessageHang
        from ..models.server_message_knowledge_base_request import ServerMessageKnowledgeBaseRequest
        from ..models.server_message_language_change_detected import ServerMessageLanguageChangeDetected
        from ..models.server_message_model_output import ServerMessageModelOutput
        from ..models.server_message_phone_call_control import ServerMessagePhoneCallControl
        from ..models.server_message_speech_update import ServerMessageSpeechUpdate
        from ..models.server_message_status_update import ServerMessageStatusUpdate
        from ..models.server_message_tool_calls import ServerMessageToolCalls
        from ..models.server_message_transcript import ServerMessageTranscript
        from ..models.server_message_transfer_destination_request import ServerMessageTransferDestinationRequest
        from ..models.server_message_transfer_update import ServerMessageTransferUpdate
        from ..models.server_message_user_interrupted import ServerMessageUserInterrupted
        from ..models.server_message_voice_input import ServerMessageVoiceInput
        from ..models.server_message_voice_request import ServerMessageVoiceRequest

        d = src_dict.copy()

        def _parse_message(
            data: object,
        ) -> Union[
            "ServerMessageAssistantRequest",
            "ServerMessageConversationUpdate",
            "ServerMessageEndOfCallReport",
            "ServerMessageHang",
            "ServerMessageKnowledgeBaseRequest",
            "ServerMessageLanguageChangeDetected",
            "ServerMessageModelOutput",
            "ServerMessagePhoneCallControl",
            "ServerMessageSpeechUpdate",
            "ServerMessageStatusUpdate",
            "ServerMessageToolCalls",
            "ServerMessageTranscript",
            "ServerMessageTransferDestinationRequest",
            "ServerMessageTransferUpdate",
            "ServerMessageUserInterrupted",
            "ServerMessageVoiceInput",
            "ServerMessageVoiceRequest",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_0 = ServerMessageAssistantRequest.from_dict(data)

                return message_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_1 = ServerMessageConversationUpdate.from_dict(data)

                return message_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_2 = ServerMessageEndOfCallReport.from_dict(data)

                return message_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_3 = ServerMessageHang.from_dict(data)

                return message_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_4 = ServerMessageKnowledgeBaseRequest.from_dict(data)

                return message_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_5 = ServerMessageModelOutput.from_dict(data)

                return message_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_6 = ServerMessagePhoneCallControl.from_dict(data)

                return message_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_7 = ServerMessageSpeechUpdate.from_dict(data)

                return message_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_8 = ServerMessageStatusUpdate.from_dict(data)

                return message_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_9 = ServerMessageToolCalls.from_dict(data)

                return message_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_10 = ServerMessageTransferDestinationRequest.from_dict(data)

                return message_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_11 = ServerMessageTransferUpdate.from_dict(data)

                return message_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_12 = ServerMessageTranscript.from_dict(data)

                return message_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_13 = ServerMessageUserInterrupted.from_dict(data)

                return message_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_14 = ServerMessageLanguageChangeDetected.from_dict(data)

                return message_type_14
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_15 = ServerMessageVoiceInput.from_dict(data)

                return message_type_15
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            message_type_16 = ServerMessageVoiceRequest.from_dict(data)

            return message_type_16

        message = _parse_message(d.pop("message"))

        server_message = cls(
            message=message,
        )

        server_message.additional_properties = d
        return server_message

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
