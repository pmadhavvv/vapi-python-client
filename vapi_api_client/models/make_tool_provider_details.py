from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.make_tool_provider_details_type import MakeToolProviderDetailsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_template_setup import ToolTemplateSetup


T = TypeVar("T", bound="MakeToolProviderDetails")


@_attrs_define
class MakeToolProviderDetails:
    """
    Attributes:
        type_ (MakeToolProviderDetailsType): The type of tool. "make" for Make tool.
        template_url (Union[Unset, str]): This is the Template URL or the Snapshot URL corresponding to the Template.
        setup_instructions (Union[Unset, list['ToolTemplateSetup']]):
        scenario_id (Union[Unset, float]):
        scenario_name (Union[Unset, str]):
        trigger_hook_id (Union[Unset, float]):
        trigger_hook_name (Union[Unset, str]):
    """

    type_: MakeToolProviderDetailsType
    template_url: Union[Unset, str] = UNSET
    setup_instructions: Union[Unset, list["ToolTemplateSetup"]] = UNSET
    scenario_id: Union[Unset, float] = UNSET
    scenario_name: Union[Unset, str] = UNSET
    trigger_hook_id: Union[Unset, float] = UNSET
    trigger_hook_name: Union[Unset, str] = UNSET
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

        scenario_id = self.scenario_id

        scenario_name = self.scenario_name

        trigger_hook_id = self.trigger_hook_id

        trigger_hook_name = self.trigger_hook_name

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
        if scenario_id is not UNSET:
            field_dict["scenarioId"] = scenario_id
        if scenario_name is not UNSET:
            field_dict["scenarioName"] = scenario_name
        if trigger_hook_id is not UNSET:
            field_dict["triggerHookId"] = trigger_hook_id
        if trigger_hook_name is not UNSET:
            field_dict["triggerHookName"] = trigger_hook_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_template_setup import ToolTemplateSetup

        d = dict(src_dict)
        type_ = MakeToolProviderDetailsType(d.pop("type"))

        template_url = d.pop("templateUrl", UNSET)

        setup_instructions = []
        _setup_instructions = d.pop("setupInstructions", UNSET)
        for setup_instructions_item_data in _setup_instructions or []:
            setup_instructions_item = ToolTemplateSetup.from_dict(setup_instructions_item_data)

            setup_instructions.append(setup_instructions_item)

        scenario_id = d.pop("scenarioId", UNSET)

        scenario_name = d.pop("scenarioName", UNSET)

        trigger_hook_id = d.pop("triggerHookId", UNSET)

        trigger_hook_name = d.pop("triggerHookName", UNSET)

        make_tool_provider_details = cls(
            type_=type_,
            template_url=template_url,
            setup_instructions=setup_instructions,
            scenario_id=scenario_id,
            scenario_name=scenario_name,
            trigger_hook_id=trigger_hook_id,
            trigger_hook_name=trigger_hook_name,
        )

        make_tool_provider_details.additional_properties = d
        return make_tool_provider_details

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
