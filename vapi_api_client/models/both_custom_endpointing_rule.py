from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.both_custom_endpointing_rule_type import BothCustomEndpointingRuleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.regex_option import RegexOption


T = TypeVar("T", bound="BothCustomEndpointingRule")


@_attrs_define
class BothCustomEndpointingRule:
    r"""
    Attributes:
        type_ (BothCustomEndpointingRuleType): This endpointing rule is based on both the last assistant message and the
            current customer message as they are speaking.

            Flow:
            - Assistant speaks
            - Customer starts speaking
            - Customer transcription comes in
            - This rule is evaluated on the last assistant message and the current customer transcription
            - If assistant message matches `assistantRegex` AND customer message matches `customerRegex`, the endpointing
            timeout is set to `timeoutSeconds`

            Usage:
            - If you want to wait longer while customer is speaking numbers, you can set a longer timeout.
        assistant_regex (str): This is the regex pattern to match the assistant's message.

            Note:
            - This works by using the `RegExp.test` method in Node.JS. Eg. `/hello/.test("hello there")` will return `true`.

            Hot tip:
            - In JavaScript, escape `\` when sending the regex pattern. Eg. `"hello\sthere"` will be sent over the wire as
            `"hellosthere"`. Send `"hello\\sthere"` instead.
            - `RegExp.test` does substring matching, so `/cat/.test("I love cats")` will return `true`. To do full string
            matching, send "^cat$".
        customer_regex (str):
        timeout_seconds (float): This is the endpointing timeout in seconds, if the rule is matched.
        assistant_regex_options (Union[Unset, list['RegexOption']]): These are the options for the assistant's message
            regex match. Defaults to all disabled.

            @default []
        customer_regex_options (Union[Unset, list['RegexOption']]): These are the options for the customer's message
            regex match. Defaults to all disabled.

            @default []
    """

    type_: BothCustomEndpointingRuleType
    assistant_regex: str
    customer_regex: str
    timeout_seconds: float
    assistant_regex_options: Union[Unset, list["RegexOption"]] = UNSET
    customer_regex_options: Union[Unset, list["RegexOption"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        assistant_regex = self.assistant_regex

        customer_regex = self.customer_regex

        timeout_seconds = self.timeout_seconds

        assistant_regex_options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.assistant_regex_options, Unset):
            assistant_regex_options = []
            for assistant_regex_options_item_data in self.assistant_regex_options:
                assistant_regex_options_item = assistant_regex_options_item_data.to_dict()
                assistant_regex_options.append(assistant_regex_options_item)

        customer_regex_options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.customer_regex_options, Unset):
            customer_regex_options = []
            for customer_regex_options_item_data in self.customer_regex_options:
                customer_regex_options_item = customer_regex_options_item_data.to_dict()
                customer_regex_options.append(customer_regex_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "assistantRegex": assistant_regex,
                "customerRegex": customer_regex,
                "timeoutSeconds": timeout_seconds,
            }
        )
        if assistant_regex_options is not UNSET:
            field_dict["assistantRegexOptions"] = assistant_regex_options
        if customer_regex_options is not UNSET:
            field_dict["customerRegexOptions"] = customer_regex_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.regex_option import RegexOption

        d = dict(src_dict)
        type_ = BothCustomEndpointingRuleType(d.pop("type"))

        assistant_regex = d.pop("assistantRegex")

        customer_regex = d.pop("customerRegex")

        timeout_seconds = d.pop("timeoutSeconds")

        assistant_regex_options = []
        _assistant_regex_options = d.pop("assistantRegexOptions", UNSET)
        for assistant_regex_options_item_data in _assistant_regex_options or []:
            assistant_regex_options_item = RegexOption.from_dict(assistant_regex_options_item_data)

            assistant_regex_options.append(assistant_regex_options_item)

        customer_regex_options = []
        _customer_regex_options = d.pop("customerRegexOptions", UNSET)
        for customer_regex_options_item_data in _customer_regex_options or []:
            customer_regex_options_item = RegexOption.from_dict(customer_regex_options_item_data)

            customer_regex_options.append(customer_regex_options_item)

        both_custom_endpointing_rule = cls(
            type_=type_,
            assistant_regex=assistant_regex,
            customer_regex=customer_regex,
            timeout_seconds=timeout_seconds,
            assistant_regex_options=assistant_regex_options,
            customer_regex_options=customer_regex_options,
        )

        both_custom_endpointing_rule.additional_properties = d
        return both_custom_endpointing_rule

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
