from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_metadata_type import ClientMessageMetadataType

T = TypeVar("T", bound="ClientMessageMetadata")


@_attrs_define
class ClientMessageMetadata:
    """
    Attributes:
        type_ (ClientMessageMetadataType): This is the type of the message. "metadata" is sent to forward metadata to
            the client.
        metadata (str): This is the metadata content
    """

    type_: ClientMessageMetadataType
    metadata: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = ClientMessageMetadataType(d.pop("type"))

        metadata = d.pop("metadata")

        client_message_metadata = cls(
            type_=type_,
            metadata=metadata,
        )

        client_message_metadata.additional_properties = d
        return client_message_metadata

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
