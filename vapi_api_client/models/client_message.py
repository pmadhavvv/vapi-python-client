from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.client_message_conversation_update import ClientMessageConversationUpdate
    from ..models.client_message_hang import ClientMessageHang
    from ..models.client_message_language_change_detected import ClientMessageLanguageChangeDetected
    from ..models.client_message_metadata import ClientMessageMetadata
    from ..models.client_message_model_output import ClientMessageModelOutput
    from ..models.client_message_speech_update import ClientMessageSpeechUpdate
    from ..models.client_message_tool_calls import ClientMessageToolCalls
    from ..models.client_message_tool_calls_result import ClientMessageToolCallsResult
    from ..models.client_message_transcript import ClientMessageTranscript
    from ..models.client_message_transfer_update import ClientMessageTransferUpdate
    from ..models.client_message_user_interrupted import ClientMessageUserInterrupted
    from ..models.client_message_voice_input import ClientMessageVoiceInput
    from ..models.client_message_workflow_node_started import ClientMessageWorkflowNodeStarted


T = TypeVar("T", bound="ClientMessage")


@_attrs_define
class ClientMessage:
    """
    Attributes:
        message (Union['ClientMessageConversationUpdate', 'ClientMessageHang', 'ClientMessageLanguageChangeDetected',
            'ClientMessageMetadata', 'ClientMessageModelOutput', 'ClientMessageSpeechUpdate', 'ClientMessageToolCalls',
            'ClientMessageToolCallsResult', 'ClientMessageTranscript', 'ClientMessageTransferUpdate',
            'ClientMessageUserInterrupted', 'ClientMessageVoiceInput', 'ClientMessageWorkflowNodeStarted']): These are all
            the messages that can be sent to the client-side SDKs during the call. Configure the messages you'd like to
            receive in `assistant.clientMessages`.
    """

    message: Union[
        "ClientMessageConversationUpdate",
        "ClientMessageHang",
        "ClientMessageLanguageChangeDetected",
        "ClientMessageMetadata",
        "ClientMessageModelOutput",
        "ClientMessageSpeechUpdate",
        "ClientMessageToolCalls",
        "ClientMessageToolCallsResult",
        "ClientMessageTranscript",
        "ClientMessageTransferUpdate",
        "ClientMessageUserInterrupted",
        "ClientMessageVoiceInput",
        "ClientMessageWorkflowNodeStarted",
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.client_message_conversation_update import ClientMessageConversationUpdate
        from ..models.client_message_hang import ClientMessageHang
        from ..models.client_message_language_change_detected import ClientMessageLanguageChangeDetected
        from ..models.client_message_metadata import ClientMessageMetadata
        from ..models.client_message_model_output import ClientMessageModelOutput
        from ..models.client_message_speech_update import ClientMessageSpeechUpdate
        from ..models.client_message_tool_calls import ClientMessageToolCalls
        from ..models.client_message_tool_calls_result import ClientMessageToolCallsResult
        from ..models.client_message_transcript import ClientMessageTranscript
        from ..models.client_message_transfer_update import ClientMessageTransferUpdate
        from ..models.client_message_user_interrupted import ClientMessageUserInterrupted
        from ..models.client_message_workflow_node_started import ClientMessageWorkflowNodeStarted

        message: dict[str, Any]
        if isinstance(self.message, ClientMessageWorkflowNodeStarted):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientMessageConversationUpdate):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientMessageHang):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientMessageMetadata):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientMessageModelOutput):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientMessageSpeechUpdate):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientMessageTranscript):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientMessageToolCalls):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientMessageToolCallsResult):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientMessageTransferUpdate):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientMessageUserInterrupted):
            message = self.message.to_dict()
        elif isinstance(self.message, ClientMessageLanguageChangeDetected):
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
        from ..models.client_message_conversation_update import ClientMessageConversationUpdate
        from ..models.client_message_hang import ClientMessageHang
        from ..models.client_message_language_change_detected import ClientMessageLanguageChangeDetected
        from ..models.client_message_metadata import ClientMessageMetadata
        from ..models.client_message_model_output import ClientMessageModelOutput
        from ..models.client_message_speech_update import ClientMessageSpeechUpdate
        from ..models.client_message_tool_calls import ClientMessageToolCalls
        from ..models.client_message_tool_calls_result import ClientMessageToolCallsResult
        from ..models.client_message_transcript import ClientMessageTranscript
        from ..models.client_message_transfer_update import ClientMessageTransferUpdate
        from ..models.client_message_user_interrupted import ClientMessageUserInterrupted
        from ..models.client_message_voice_input import ClientMessageVoiceInput
        from ..models.client_message_workflow_node_started import ClientMessageWorkflowNodeStarted

        d = src_dict.copy()

        def _parse_message(
            data: object,
        ) -> Union[
            "ClientMessageConversationUpdate",
            "ClientMessageHang",
            "ClientMessageLanguageChangeDetected",
            "ClientMessageMetadata",
            "ClientMessageModelOutput",
            "ClientMessageSpeechUpdate",
            "ClientMessageToolCalls",
            "ClientMessageToolCallsResult",
            "ClientMessageTranscript",
            "ClientMessageTransferUpdate",
            "ClientMessageUserInterrupted",
            "ClientMessageVoiceInput",
            "ClientMessageWorkflowNodeStarted",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_0 = ClientMessageWorkflowNodeStarted.from_dict(data)

                return message_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_1 = ClientMessageConversationUpdate.from_dict(data)

                return message_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_2 = ClientMessageHang.from_dict(data)

                return message_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_3 = ClientMessageMetadata.from_dict(data)

                return message_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_4 = ClientMessageModelOutput.from_dict(data)

                return message_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_5 = ClientMessageSpeechUpdate.from_dict(data)

                return message_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_6 = ClientMessageTranscript.from_dict(data)

                return message_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_7 = ClientMessageToolCalls.from_dict(data)

                return message_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_8 = ClientMessageToolCallsResult.from_dict(data)

                return message_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_9 = ClientMessageTransferUpdate.from_dict(data)

                return message_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_10 = ClientMessageUserInterrupted.from_dict(data)

                return message_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_11 = ClientMessageLanguageChangeDetected.from_dict(data)

                return message_type_11
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            message_type_12 = ClientMessageVoiceInput.from_dict(data)

            return message_type_12

        message = _parse_message(d.pop("message"))

        client_message = cls(
            message=message,
        )

        client_message.additional_properties = d
        return client_message

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
