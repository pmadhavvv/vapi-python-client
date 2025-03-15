from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.say_type import SayType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.say_metadata import SayMetadata


T = TypeVar("T", bound="Say")


@_attrs_define
class Say:
    """
    Attributes:
        type_ (SayType):
        name (str):
        exact (Union[Unset, str]):
        prompt (Union[Unset, str]):
        metadata (Union[Unset, SayMetadata]): This is for metadata you want to store on the task.
    """

    type_: SayType
    name: str
    exact: Union[Unset, str] = UNSET
    prompt: Union[Unset, str] = UNSET
    metadata: Union[Unset, "SayMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        exact = self.exact

        prompt = self.prompt

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
        if exact is not UNSET:
            field_dict["exact"] = exact
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.say_metadata import SayMetadata

        d = src_dict.copy()
        type_ = SayType(d.pop("type"))

        name = d.pop("name")

        exact = d.pop("exact", UNSET)

        prompt = d.pop("prompt", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, SayMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SayMetadata.from_dict(_metadata)

        say = cls(
            type_=type_,
            name=name,
            exact=exact,
            prompt=prompt,
            metadata=metadata,
        )

        say.additional_properties = d
        return say

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
