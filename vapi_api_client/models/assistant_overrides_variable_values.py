from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssistantOverridesVariableValues")


@_attrs_define
class AssistantOverridesVariableValues:
    """These are values that will be used to replace the template variables in the assistant messages and other text-based
    fields.
    This uses LiquidJS syntax. https://liquidjs.com/tutorials/intro-to-liquid.html

    So for example, `{{ name }}` will be replaced with the value of `name` in `variableValues`.
    `{{"now" | date: "%b %d, %Y, %I:%M %p", "America/New_York"}}` will be replaced with the current date and time in New
    York.
     Some VAPI reserved defaults:
     - *customer* - the customer object

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        assistant_overrides_variable_values = cls()

        assistant_overrides_variable_values.additional_properties = d
        return assistant_overrides_variable_values

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
