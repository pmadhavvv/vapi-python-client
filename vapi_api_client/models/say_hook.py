from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.say_hook_type import SayHookType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.say_hook_metadata import SayHookMetadata


T = TypeVar("T", bound="SayHook")


@_attrs_define
class SayHook:
    """
    Attributes:
        type_ (SayHookType):
        metadata (Union[Unset, SayHookMetadata]): This is for metadata you want to store on the task.
        exact (Union[Unset, str]):
        prompt (Union[Unset, str]):
    """

    type_: SayHookType
    metadata: Union[Unset, "SayHookMetadata"] = UNSET
    exact: Union[Unset, str] = UNSET
    prompt: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        exact = self.exact

        prompt = self.prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if exact is not UNSET:
            field_dict["exact"] = exact
        if prompt is not UNSET:
            field_dict["prompt"] = prompt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.say_hook_metadata import SayHookMetadata

        d = dict(src_dict)
        type_ = SayHookType(d.pop("type"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, SayHookMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SayHookMetadata.from_dict(_metadata)

        exact = d.pop("exact", UNSET)

        prompt = d.pop("prompt", UNSET)

        say_hook = cls(
            type_=type_,
            metadata=metadata,
            exact=exact,
            prompt=prompt,
        )

        say_hook.additional_properties = d
        return say_hook

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
