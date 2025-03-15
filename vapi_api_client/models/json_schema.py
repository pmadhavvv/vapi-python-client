from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.json_schema_type import JsonSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_schema_items import JsonSchemaItems
    from ..models.json_schema_properties import JsonSchemaProperties


T = TypeVar("T", bound="JsonSchema")


@_attrs_define
class JsonSchema:
    """
    Attributes:
        type_ (JsonSchemaType): This is the type of output you'd like.

            `string`, `number`, `integer`, `boolean` are the primitive types and should be obvious.

            `array` and `object` are more interesting and quite powerful. They allow you to define nested structures.

            For `array`, you can define the schema of the items in the array using the `items` property.

            For `object`, you can define the properties of the object using the `properties` property.
        items (Union[Unset, JsonSchemaItems]): This is required if the type is "array". This is the schema of the items
            in the array.

            This is of type JsonSchema. However, Swagger doesn't support circular references.
        properties (Union[Unset, JsonSchemaProperties]): This is required if the type is "object". This specifies the
            properties of the object.

            This is a map of string to JsonSchema. However, Swagger doesn't support circular references.
        description (Union[Unset, str]): This is the description to help the model understand what it needs to output.
        required (Union[Unset, list[str]]): This is a list of properties that are required.

            This only makes sense if the type is "object".
        regex (Union[Unset, str]): This is a regex that will be used to validate data in question.
        value (Union[Unset, str]): This the value that will be used in filling the property.
        target (Union[Unset, str]): This the target variable that will be filled with the value of this property.
        enum (Union[Unset, list[str]]): This array specifies the allowed values that can be used to restrict the output
            of the model.
    """

    type_: JsonSchemaType
    items: Union[Unset, "JsonSchemaItems"] = UNSET
    properties: Union[Unset, "JsonSchemaProperties"] = UNSET
    description: Union[Unset, str] = UNSET
    required: Union[Unset, list[str]] = UNSET
    regex: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    target: Union[Unset, str] = UNSET
    enum: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        items: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        description = self.description

        required: Union[Unset, list[str]] = UNSET
        if not isinstance(self.required, Unset):
            required = self.required

        regex = self.regex

        value = self.value

        target = self.target

        enum: Union[Unset, list[str]] = UNSET
        if not isinstance(self.enum, Unset):
            enum = self.enum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if items is not UNSET:
            field_dict["items"] = items
        if properties is not UNSET:
            field_dict["properties"] = properties
        if description is not UNSET:
            field_dict["description"] = description
        if required is not UNSET:
            field_dict["required"] = required
        if regex is not UNSET:
            field_dict["regex"] = regex
        if value is not UNSET:
            field_dict["value"] = value
        if target is not UNSET:
            field_dict["target"] = target
        if enum is not UNSET:
            field_dict["enum"] = enum

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.json_schema_items import JsonSchemaItems
        from ..models.json_schema_properties import JsonSchemaProperties

        d = src_dict.copy()
        type_ = JsonSchemaType(d.pop("type"))

        _items = d.pop("items", UNSET)
        items: Union[Unset, JsonSchemaItems]
        if isinstance(_items, Unset):
            items = UNSET
        else:
            items = JsonSchemaItems.from_dict(_items)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, JsonSchemaProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = JsonSchemaProperties.from_dict(_properties)

        description = d.pop("description", UNSET)

        required = cast(list[str], d.pop("required", UNSET))

        regex = d.pop("regex", UNSET)

        value = d.pop("value", UNSET)

        target = d.pop("target", UNSET)

        enum = cast(list[str], d.pop("enum", UNSET))

        json_schema = cls(
            type_=type_,
            items=items,
            properties=properties,
            description=description,
            required=required,
            regex=regex,
            value=value,
            target=target,
            enum=enum,
        )

        json_schema.additional_properties = d
        return json_schema

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
