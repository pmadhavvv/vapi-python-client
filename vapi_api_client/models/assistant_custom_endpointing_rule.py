from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assistant_custom_endpointing_rule_type import AssistantCustomEndpointingRuleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.regex_option import RegexOption


T = TypeVar("T", bound="AssistantCustomEndpointingRule")


@_attrs_define
class AssistantCustomEndpointingRule:
    r"""
    Attributes:
        type_ (AssistantCustomEndpointingRuleType): This endpointing rule is based on the last assistant message before
            customer started speaking.

            Flow:
            - Assistant speaks
            - Customer starts speaking
            - Customer transcription comes in
            - This rule is evaluated on the last assistant message
            - If a match is found based on `regex`, the endpointing timeout is set to `timeoutSeconds`

            Usage:
            - If you have yes/no questions in your use case like "are you interested in a loan?", you can set a shorter
            timeout.
            - If you have questions where the customer may pause to look up information like "what's my account number?",
            you can set a longer timeout.
        regex (str): This is the regex pattern to match.

            Note:
            - This works by using the `RegExp.test` method in Node.JS. Eg. `/hello/.test("hello there")` will return `true`.

            Hot tip:
            - In JavaScript, escape `\` when sending the regex pattern. Eg. `"hello\sthere"` will be sent over the wire as
            `"hellosthere"`. Send `"hello\\sthere"` instead.
            - `RegExp.test` does substring matching, so `/cat/.test("I love cats")` will return `true`. To do full string
            matching, send "^cat$".
        timeout_seconds (float): This is the endpointing timeout in seconds, if the rule is matched.
        regex_options (Union[Unset, list['RegexOption']]): These are the options for the regex match. Defaults to all
            disabled.

            @default []
    """

    type_: AssistantCustomEndpointingRuleType
    regex: str
    timeout_seconds: float
    regex_options: Union[Unset, list["RegexOption"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        regex = self.regex

        timeout_seconds = self.timeout_seconds

        regex_options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.regex_options, Unset):
            regex_options = []
            for regex_options_item_data in self.regex_options:
                regex_options_item = regex_options_item_data.to_dict()
                regex_options.append(regex_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "regex": regex,
                "timeoutSeconds": timeout_seconds,
            }
        )
        if regex_options is not UNSET:
            field_dict["regexOptions"] = regex_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.regex_option import RegexOption

        d = src_dict.copy()
        type_ = AssistantCustomEndpointingRuleType(d.pop("type"))

        regex = d.pop("regex")

        timeout_seconds = d.pop("timeoutSeconds")

        regex_options = []
        _regex_options = d.pop("regexOptions", UNSET)
        for regex_options_item_data in _regex_options or []:
            regex_options_item = RegexOption.from_dict(regex_options_item_data)

            regex_options.append(regex_options_item)

        assistant_custom_endpointing_rule = cls(
            type_=type_,
            regex=regex,
            timeout_seconds=timeout_seconds,
            regex_options=regex_options,
        )

        assistant_custom_endpointing_rule.additional_properties = d
        return assistant_custom_endpointing_rule

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
