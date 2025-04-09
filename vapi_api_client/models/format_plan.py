from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.format_plan_formatters_enabled import FormatPlanFormattersEnabled
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exact_replacement import ExactReplacement
    from ..models.regex_replacement import RegexReplacement


T = TypeVar("T", bound="FormatPlan")


@_attrs_define
class FormatPlan:
    r"""
    Attributes:
        enabled (Union[Unset, bool]): This determines whether the chunk is formatted before being sent to the voice
            provider. This helps with enunciation. This includes phone numbers, emails and addresses. Default `true`.

            Usage:
            - To rely on the voice provider's formatting logic, set this to `false`.

            If `voice.chunkPlan.enabled` is `false`, this is automatically `false` since there's no chunk to format.

            @default true Example: True.
        number_to_digits_cutoff (Union[Unset, float]): This is the cutoff after which a number is converted to
            individual digits instead of being spoken as words.

            Example:
            - If cutoff 2025, "12345" is converted to "1 2 3 4 5" while "1200" is converted to "twelve hundred".

            Usage:
            - If your use case doesn't involve IDs like zip codes, set this to a high value.
            - If your use case involves IDs that are shorter than 5 digits, set this to a lower value.

            @default 2025 Example: 2025.
        replacements (Union[Unset, list[Union['ExactReplacement', 'RegexReplacement']]]): These are the custom
            replacements you can make to the chunk before it is sent to the voice provider.

            Usage:
            - To replace a specific word or phrase with a different word or phrase, use the `ExactReplacement` type. Eg. `{
            type: 'exact', key: 'hello', value: 'hi' }`
            - To replace a word or phrase that matches a pattern, use the `RegexReplacement` type. Eg. `{ type: 'regex',
            regex: '\\b[a-zA-Z]{5}\\b', value: 'hi' }`

            @default []
        formatters_enabled (Union[Unset, FormatPlanFormattersEnabled]): List of formatters to apply. If not provided,
            all default formatters will be applied.
            If provided, only the specified formatters will be applied.
            Note: Some essential formatters like angle bracket removal will always be applied.
            @default undefined
    """

    enabled: Union[Unset, bool] = UNSET
    number_to_digits_cutoff: Union[Unset, float] = UNSET
    replacements: Union[Unset, list[Union["ExactReplacement", "RegexReplacement"]]] = UNSET
    formatters_enabled: Union[Unset, FormatPlanFormattersEnabled] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.exact_replacement import ExactReplacement

        enabled = self.enabled

        number_to_digits_cutoff = self.number_to_digits_cutoff

        replacements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.replacements, Unset):
            replacements = []
            for replacements_item_data in self.replacements:
                replacements_item: dict[str, Any]
                if isinstance(replacements_item_data, ExactReplacement):
                    replacements_item = replacements_item_data.to_dict()
                else:
                    replacements_item = replacements_item_data.to_dict()

                replacements.append(replacements_item)

        formatters_enabled: Union[Unset, str] = UNSET
        if not isinstance(self.formatters_enabled, Unset):
            formatters_enabled = self.formatters_enabled.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if number_to_digits_cutoff is not UNSET:
            field_dict["numberToDigitsCutoff"] = number_to_digits_cutoff
        if replacements is not UNSET:
            field_dict["replacements"] = replacements
        if formatters_enabled is not UNSET:
            field_dict["formattersEnabled"] = formatters_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exact_replacement import ExactReplacement
        from ..models.regex_replacement import RegexReplacement

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        number_to_digits_cutoff = d.pop("numberToDigitsCutoff", UNSET)

        replacements = []
        _replacements = d.pop("replacements", UNSET)
        for replacements_item_data in _replacements or []:

            def _parse_replacements_item(data: object) -> Union["ExactReplacement", "RegexReplacement"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    replacements_item_type_0 = ExactReplacement.from_dict(data)

                    return replacements_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                replacements_item_type_1 = RegexReplacement.from_dict(data)

                return replacements_item_type_1

            replacements_item = _parse_replacements_item(replacements_item_data)

            replacements.append(replacements_item)

        _formatters_enabled = d.pop("formattersEnabled", UNSET)
        formatters_enabled: Union[Unset, FormatPlanFormattersEnabled]
        if isinstance(_formatters_enabled, Unset):
            formatters_enabled = UNSET
        else:
            formatters_enabled = FormatPlanFormattersEnabled(_formatters_enabled)

        format_plan = cls(
            enabled=enabled,
            number_to_digits_cutoff=number_to_digits_cutoff,
            replacements=replacements,
            formatters_enabled=formatters_enabled,
        )

        format_plan.additional_properties = d
        return format_plan

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
