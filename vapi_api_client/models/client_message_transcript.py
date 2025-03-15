from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_transcript_role import ClientMessageTranscriptRole
from ..models.client_message_transcript_transcript_type import ClientMessageTranscriptTranscriptType
from ..models.client_message_transcript_type import ClientMessageTranscriptType

T = TypeVar("T", bound="ClientMessageTranscript")


@_attrs_define
class ClientMessageTranscript:
    """
    Attributes:
        type_ (ClientMessageTranscriptType): This is the type of the message. "transcript" is sent as transcriber
            outputs partial or final transcript.
        role (ClientMessageTranscriptRole): This is the role for which the transcript is for.
        transcript_type (ClientMessageTranscriptTranscriptType): This is the type of the transcript.
        transcript (str): This is the transcript content.
    """

    type_: ClientMessageTranscriptType
    role: ClientMessageTranscriptRole
    transcript_type: ClientMessageTranscriptTranscriptType
    transcript: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        role = self.role.value

        transcript_type = self.transcript_type.value

        transcript = self.transcript

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "role": role,
                "transcriptType": transcript_type,
                "transcript": transcript,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = ClientMessageTranscriptType(d.pop("type"))

        role = ClientMessageTranscriptRole(d.pop("role"))

        transcript_type = ClientMessageTranscriptTranscriptType(d.pop("transcriptType"))

        transcript = d.pop("transcript")

        client_message_transcript = cls(
            type_=type_,
            role=role,
            transcript_type=transcript_type,
            transcript=transcript,
        )

        client_message_transcript.additional_properties = d
        return client_message_transcript

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
