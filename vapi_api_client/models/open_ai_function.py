from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_ai_function_parameters import OpenAIFunctionParameters


T = TypeVar("T", bound="OpenAIFunction")


@_attrs_define
class OpenAIFunction:
    """
    Attributes:
        name (str): This is the the name of the function to be called.

            Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
        strict (Union[Unset, bool]): This is a boolean that controls whether to enable strict schema adherence when
            generating the function call. If set to true, the model will follow the exact schema defined in the parameters
            field. Only a subset of JSON Schema is supported when strict is true. Learn more about Structured Outputs in the
            [OpenAI guide](https://openai.com/index/introducing-structured-outputs-in-the-api/).

            @default false
        description (Union[Unset, str]): This is the description of what the function does, used by the AI to choose
            when and how to call the function.
        parameters (Union[Unset, OpenAIFunctionParameters]):
    """

    name: str
    strict: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    parameters: Union[Unset, "OpenAIFunctionParameters"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        strict = self.strict

        description = self.description

        parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if strict is not UNSET:
            field_dict["strict"] = strict
        if description is not UNSET:
            field_dict["description"] = description
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.open_ai_function_parameters import OpenAIFunctionParameters

        d = src_dict.copy()
        name = d.pop("name")

        strict = d.pop("strict", UNSET)

        description = d.pop("description", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, OpenAIFunctionParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = OpenAIFunctionParameters.from_dict(_parameters)

        open_ai_function = cls(
            name=name,
            strict=strict,
            description=description,
            parameters=parameters,
        )

        open_ai_function.additional_properties = d
        return open_ai_function

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
