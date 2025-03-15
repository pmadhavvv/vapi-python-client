from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.function_tool_provider_details_type import FunctionToolProviderDetailsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_template_setup import ToolTemplateSetup


T = TypeVar("T", bound="FunctionToolProviderDetails")


@_attrs_define
class FunctionToolProviderDetails:
    """
    Attributes:
        type_ (FunctionToolProviderDetailsType): The type of tool. "function" for Function tool.
        template_url (Union[Unset, str]): This is the Template URL or the Snapshot URL corresponding to the Template.
        setup_instructions (Union[Unset, list['ToolTemplateSetup']]):
    """

    type_: FunctionToolProviderDetailsType
    template_url: Union[Unset, str] = UNSET
    setup_instructions: Union[Unset, list["ToolTemplateSetup"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        template_url = self.template_url

        setup_instructions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.setup_instructions, Unset):
            setup_instructions = []
            for setup_instructions_item_data in self.setup_instructions:
                setup_instructions_item = setup_instructions_item_data.to_dict()
                setup_instructions.append(setup_instructions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if template_url is not UNSET:
            field_dict["templateUrl"] = template_url
        if setup_instructions is not UNSET:
            field_dict["setupInstructions"] = setup_instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tool_template_setup import ToolTemplateSetup

        d = src_dict.copy()
        type_ = FunctionToolProviderDetailsType(d.pop("type"))

        template_url = d.pop("templateUrl", UNSET)

        setup_instructions = []
        _setup_instructions = d.pop("setupInstructions", UNSET)
        for setup_instructions_item_data in _setup_instructions or []:
            setup_instructions_item = ToolTemplateSetup.from_dict(setup_instructions_item_data)

            setup_instructions.append(setup_instructions_item)

        function_tool_provider_details = cls(
            type_=type_,
            template_url=template_url,
            setup_instructions=setup_instructions,
        )

        function_tool_provider_details.additional_properties = d
        return function_tool_provider_details

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
