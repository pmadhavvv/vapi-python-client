from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.regex_replacement_type import RegexReplacementType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.regex_option import RegexOption


T = TypeVar("T", bound="RegexReplacement")


@_attrs_define
class RegexReplacement:
    r"""
    Attributes:
        type_ (RegexReplacementType): This is the regex replacement type. You can use this to replace a word or phrase
            that matches a pattern.

            Usage:
            - Replace all numbers with "some number": { type: 'regex', regex: '\\d+', value: 'some number' }
            - Replace email addresses with "[EMAIL]": { type: 'regex', regex:
            '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b', value: '[EMAIL]' }
            - Replace phone numbers with a formatted version: { type: 'regex', regex: '(\\d{3})(\\d{3})(\\d{4})', value:
            '($1) $2-$3' }
            - Replace all instances of "color" or "colour" with "hue": { type: 'regex', regex: 'colou?r', value: 'hue' }
            - Capitalize the first letter of every sentence: { type: 'regex', regex: '(?<=\\. |^)[a-z]', value: (match) =>
            match.toUpperCase() }
        regex (str): This is the regex pattern to replace.

            Note:
            - This works by using the `string.replace` method in Node.JS. Eg. `"hello there".replace(/hello/g, "hi")` will
            return `"hi there"`.

            Hot tip:
            - In JavaScript, escape `\` when sending the regex pattern. Eg. `"hello\sthere"` will be sent over the wire as
            `"hellosthere"`. Send `"hello\\sthere"` instead.
        value (str): This is the value that will replace the match.
        options (Union[Unset, list['RegexOption']]): These are the options for the regex replacement. Defaults to all
            disabled.

            @default []
    """

    type_: RegexReplacementType
    regex: str
    value: str
    options: Union[Unset, list["RegexOption"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        regex = self.regex

        value = self.value

        options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "regex": regex,
                "value": value,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.regex_option import RegexOption

        d = dict(src_dict)
        type_ = RegexReplacementType(d.pop("type"))

        regex = d.pop("regex")

        value = d.pop("value")

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = RegexOption.from_dict(options_item_data)

            options.append(options_item)

        regex_replacement = cls(
            type_=type_,
            regex=regex,
            value=value,
            options=options,
        )

        regex_replacement.additional_properties = d
        return regex_replacement

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
