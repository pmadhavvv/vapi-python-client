from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.regex_option_type import RegexOptionType

T = TypeVar("T", bound="RegexOption")


@_attrs_define
class RegexOption:
    """
    Attributes:
        type_ (RegexOptionType): This is the type of the regex option. Options are:
            - `ignore-case`: Ignores the case of the text being matched. Add
            - `whole-word`: Matches whole words only.
            - `multi-line`: Matches across multiple lines.
        enabled (bool): This is whether to enable the option.

            @default false
    """

    type_: RegexOptionType
    enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = RegexOptionType(d.pop("type"))

        enabled = d.pop("enabled")

        regex_option = cls(
            type_=type_,
            enabled=enabled,
        )

        regex_option.additional_properties = d
        return regex_option

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
