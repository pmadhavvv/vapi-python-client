from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transfer_type import TransferType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transfer_destination import TransferDestination
    from ..models.transfer_metadata import TransferMetadata


T = TypeVar("T", bound="Transfer")


@_attrs_define
class Transfer:
    """
    Attributes:
        type_ (TransferType):
        destination (TransferDestination):
        name (str):
        metadata (Union[Unset, TransferMetadata]): This is for metadata you want to store on the task.
    """

    type_: TransferType
    destination: "TransferDestination"
    name: str
    metadata: Union[Unset, "TransferMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        destination = self.destination.to_dict()

        name = self.name

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "destination": destination,
                "name": name,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transfer_destination import TransferDestination
        from ..models.transfer_metadata import TransferMetadata

        d = dict(src_dict)
        type_ = TransferType(d.pop("type"))

        destination = TransferDestination.from_dict(d.pop("destination"))

        name = d.pop("name")

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, TransferMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = TransferMetadata.from_dict(_metadata)

        transfer = cls(
            type_=type_,
            destination=destination,
            name=name,
            metadata=metadata,
        )

        transfer.additional_properties = d
        return transfer

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
