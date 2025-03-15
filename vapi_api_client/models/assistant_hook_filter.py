from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assistant_hook_filter_type import AssistantHookFilterType

T = TypeVar("T", bound="AssistantHookFilter")


@_attrs_define
class AssistantHookFilter:
    """
    Attributes:
        type_ (AssistantHookFilterType): This is the type of filter - currently only "oneOf" is supported
        key (str): This is the key to filter on (e.g. "call.endedReason")
        one_of (list[str]): This is the array of possible values to match against
    """

    type_: AssistantHookFilterType
    key: str
    one_of: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        key = self.key

        one_of = self.one_of

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "key": key,
                "oneOf": one_of,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = AssistantHookFilterType(d.pop("type"))

        key = d.pop("key")

        one_of = cast(list[str], d.pop("oneOf"))

        assistant_hook_filter = cls(
            type_=type_,
            key=key,
            one_of=one_of,
        )

        assistant_hook_filter.additional_properties = d
        return assistant_hook_filter

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
