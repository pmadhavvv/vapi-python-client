from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.server_message_response_assistant_request import ServerMessageResponseAssistantRequest
    from ..models.server_message_response_knowledge_base_request import ServerMessageResponseKnowledgeBaseRequest
    from ..models.server_message_response_tool_calls import ServerMessageResponseToolCalls
    from ..models.server_message_response_transfer_destination_request import (
        ServerMessageResponseTransferDestinationRequest,
    )
    from ..models.server_message_response_voice_request import ServerMessageResponseVoiceRequest


T = TypeVar("T", bound="ServerMessageResponse")


@_attrs_define
class ServerMessageResponse:
    """
    Attributes:
        message_response (Union['ServerMessageResponseAssistantRequest', 'ServerMessageResponseKnowledgeBaseRequest',
            'ServerMessageResponseToolCalls', 'ServerMessageResponseTransferDestinationRequest',
            'ServerMessageResponseVoiceRequest']): This is the response that is expected from the server to the message.

            Note: Most messages don't expect a response. Only "assistant-request", "tool-calls" and "transfer-destination-
            request" do.
    """

    message_response: Union[
        "ServerMessageResponseAssistantRequest",
        "ServerMessageResponseKnowledgeBaseRequest",
        "ServerMessageResponseToolCalls",
        "ServerMessageResponseTransferDestinationRequest",
        "ServerMessageResponseVoiceRequest",
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_message_response_assistant_request import ServerMessageResponseAssistantRequest
        from ..models.server_message_response_knowledge_base_request import ServerMessageResponseKnowledgeBaseRequest
        from ..models.server_message_response_tool_calls import ServerMessageResponseToolCalls
        from ..models.server_message_response_transfer_destination_request import (
            ServerMessageResponseTransferDestinationRequest,
        )

        message_response: dict[str, Any]
        if isinstance(self.message_response, ServerMessageResponseAssistantRequest):
            message_response = self.message_response.to_dict()
        elif isinstance(self.message_response, ServerMessageResponseKnowledgeBaseRequest):
            message_response = self.message_response.to_dict()
        elif isinstance(self.message_response, ServerMessageResponseToolCalls):
            message_response = self.message_response.to_dict()
        elif isinstance(self.message_response, ServerMessageResponseTransferDestinationRequest):
            message_response = self.message_response.to_dict()
        else:
            message_response = self.message_response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageResponse": message_response,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_message_response_assistant_request import ServerMessageResponseAssistantRequest
        from ..models.server_message_response_knowledge_base_request import ServerMessageResponseKnowledgeBaseRequest
        from ..models.server_message_response_tool_calls import ServerMessageResponseToolCalls
        from ..models.server_message_response_transfer_destination_request import (
            ServerMessageResponseTransferDestinationRequest,
        )
        from ..models.server_message_response_voice_request import ServerMessageResponseVoiceRequest

        d = dict(src_dict)

        def _parse_message_response(
            data: object,
        ) -> Union[
            "ServerMessageResponseAssistantRequest",
            "ServerMessageResponseKnowledgeBaseRequest",
            "ServerMessageResponseToolCalls",
            "ServerMessageResponseTransferDestinationRequest",
            "ServerMessageResponseVoiceRequest",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_response_type_0 = ServerMessageResponseAssistantRequest.from_dict(data)

                return message_response_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_response_type_1 = ServerMessageResponseKnowledgeBaseRequest.from_dict(data)

                return message_response_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_response_type_2 = ServerMessageResponseToolCalls.from_dict(data)

                return message_response_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_response_type_3 = ServerMessageResponseTransferDestinationRequest.from_dict(data)

                return message_response_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            message_response_type_4 = ServerMessageResponseVoiceRequest.from_dict(data)

            return message_response_type_4

        message_response = _parse_message_response(d.pop("messageResponse"))

        server_message_response = cls(
            message_response=message_response,
        )

        server_message_response.additional_properties = d
        return server_message_response

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
