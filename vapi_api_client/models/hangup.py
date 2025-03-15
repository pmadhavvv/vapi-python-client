from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hangup_type import HangupType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hangup_metadata import HangupMetadata


T = TypeVar("T", bound="Hangup")


@_attrs_define
class Hangup:
    """
    Attributes:
        type_ (HangupType):
        name (str):
        metadata (Union[Unset, HangupMetadata]): This is for metadata you want to store on the task.
    """

    type_: HangupType
    name: str
    metadata: Union[Unset, "HangupMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.hangup_metadata import HangupMetadata

        d = src_dict.copy()
        type_ = HangupType(d.pop("type"))

        name = d.pop("name")

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, HangupMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = HangupMetadata.from_dict(_metadata)

        hangup = cls(
            type_=type_,
            name=name,
            metadata=metadata,
        )

        hangup.additional_properties = d
        return hangup

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
