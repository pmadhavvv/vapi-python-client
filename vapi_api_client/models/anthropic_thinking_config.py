from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.anthropic_thinking_config_type import AnthropicThinkingConfigType

T = TypeVar("T", bound="AnthropicThinkingConfig")


@_attrs_define
class AnthropicThinkingConfig:
    """
    Attributes:
        type_ (AnthropicThinkingConfigType):
        budget_tokens (float): The maximum number of tokens to allocate for thinking.
            Must be between 1024 and 100000 tokens.
    """

    type_: AnthropicThinkingConfigType
    budget_tokens: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        budget_tokens = self.budget_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "budgetTokens": budget_tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AnthropicThinkingConfigType(d.pop("type"))

        budget_tokens = d.pop("budgetTokens")

        anthropic_thinking_config = cls(
            type_=type_,
            budget_tokens=budget_tokens,
        )

        anthropic_thinking_config.additional_properties = d
        return anthropic_thinking_config

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
