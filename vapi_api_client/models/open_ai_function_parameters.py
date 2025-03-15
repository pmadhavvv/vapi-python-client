from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.open_ai_function_parameters_type import OpenAIFunctionParametersType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_ai_function_parameters_properties import OpenAIFunctionParametersProperties


T = TypeVar("T", bound="OpenAIFunctionParameters")


@_attrs_define
class OpenAIFunctionParameters:
    """
    Attributes:
        type_ (OpenAIFunctionParametersType): This must be set to 'object'. It instructs the model to return a JSON
            object containing the function call properties.
        properties (OpenAIFunctionParametersProperties): This provides a description of the properties required by the
            function.
            JSON Schema can be used to specify expectations for each property.
            Refer to [this doc](https://ajv.js.org/json-schema.html#json-data-type) for a comprehensive guide on JSON
            Schema.
        required (Union[Unset, list[str]]): This specifies the properties that are required by the function.
    """

    type_: OpenAIFunctionParametersType
    properties: "OpenAIFunctionParametersProperties"
    required: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        properties = self.properties.to_dict()

        required: Union[Unset, list[str]] = UNSET
        if not isinstance(self.required, Unset):
            required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "properties": properties,
            }
        )
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.open_ai_function_parameters_properties import OpenAIFunctionParametersProperties

        d = src_dict.copy()
        type_ = OpenAIFunctionParametersType(d.pop("type"))

        properties = OpenAIFunctionParametersProperties.from_dict(d.pop("properties"))

        required = cast(list[str], d.pop("required", UNSET))

        open_ai_function_parameters = cls(
            type_=type_,
            properties=properties,
            required=required,
        )

        open_ai_function_parameters.additional_properties = d
        return open_ai_function_parameters

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
