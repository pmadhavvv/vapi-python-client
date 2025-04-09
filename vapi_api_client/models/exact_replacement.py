from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exact_replacement_type import ExactReplacementType

T = TypeVar("T", bound="ExactReplacement")


@_attrs_define
class ExactReplacement:
    """
    Attributes:
        type_ (ExactReplacementType): This is the exact replacement type. You can use this to replace a specific word or
            phrase with a different word or phrase.

            Usage:
            - Replace "hello" with "hi": { type: 'exact', key: 'hello', value: 'hi' }
            - Replace "good morning" with "good day": { type: 'exact', key: 'good morning', value: 'good day' }
            - Replace a specific name: { type: 'exact', key: 'John Doe', value: 'Jane Smith' }
            - Replace an acronym: { type: 'exact', key: 'AI', value: 'Artificial Intelligence' }
            - Replace a company name with its phonetic pronunciation: { type: 'exact', key: 'Vapi', value: 'Vappy' }
        key (str): This is the key to replace.
        value (str): This is the value that will replace the match.
    """

    type_: ExactReplacementType
    key: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ExactReplacementType(d.pop("type"))

        key = d.pop("key")

        value = d.pop("value")

        exact_replacement = cls(
            type_=type_,
            key=key,
            value=value,
        )

        exact_replacement.additional_properties = d
        return exact_replacement

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
