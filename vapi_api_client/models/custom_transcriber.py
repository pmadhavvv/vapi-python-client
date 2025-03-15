from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_transcriber_provider import CustomTranscriberProvider

if TYPE_CHECKING:
    from ..models.server import Server


T = TypeVar("T", bound="CustomTranscriber")


@_attrs_define
class CustomTranscriber:
    """
    Attributes:
        provider (CustomTranscriberProvider): This is the transcription provider that will be used. Use `custom-
            transcriber` for providers that are not natively supported.
        server (Server):
    """

    provider: CustomTranscriberProvider
    server: "Server"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        server = self.server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "server": server,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.server import Server

        d = src_dict.copy()
        provider = CustomTranscriberProvider(d.pop("provider"))

        server = Server.from_dict(d.pop("server"))

        custom_transcriber = cls(
            provider=provider,
            server=server,
        )

        custom_transcriber.additional_properties = d
        return custom_transcriber

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
