from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ServerMessageResponseVoiceRequest")


@_attrs_define
class ServerMessageResponseVoiceRequest:
    """
    Attributes:
        data (str): DO NOT respond to a `voice-request` webhook with this schema of { data }. This schema just exists to
            document what the response should look like. Follow these instructions:

            Here is what the request will look like:

            POST https://{assistant.voice.server.url}
            Content-Type: application/json

            {
              "messsage": {
                "type": "voice-request",
                "text": "Hello, world!",
                "sampleRate": 24000,
                ...other metadata about the call...
              }
            }

            The expected response is 1-channel 16-bit raw PCM audio at the sample rate specified in the request. Here is how
            the response will be piped to the transport:
            ```
            response.on('data', (chunk: Buffer) => {
              outputStream.write(chunk);
            });
            ```
    """

    data: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        data = d.pop("data")

        server_message_response_voice_request = cls(
            data=data,
        )

        server_message_response_voice_request.additional_properties = d
        return server_message_response_voice_request

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
