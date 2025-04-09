from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ghl_tool_provider_details_type import GhlToolProviderDetailsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_template_setup import ToolTemplateSetup


T = TypeVar("T", bound="GhlToolProviderDetails")


@_attrs_define
class GhlToolProviderDetails:
    """
    Attributes:
        type_ (GhlToolProviderDetailsType): The type of tool. "ghl" for GHL tool.
        template_url (Union[Unset, str]): This is the Template URL or the Snapshot URL corresponding to the Template.
        setup_instructions (Union[Unset, list['ToolTemplateSetup']]):
        workflow_id (Union[Unset, str]):
        workflow_name (Union[Unset, str]):
        webhook_hook_id (Union[Unset, str]):
        webhook_hook_name (Union[Unset, str]):
        location_id (Union[Unset, str]):
    """

    type_: GhlToolProviderDetailsType
    template_url: Union[Unset, str] = UNSET
    setup_instructions: Union[Unset, list["ToolTemplateSetup"]] = UNSET
    workflow_id: Union[Unset, str] = UNSET
    workflow_name: Union[Unset, str] = UNSET
    webhook_hook_id: Union[Unset, str] = UNSET
    webhook_hook_name: Union[Unset, str] = UNSET
    location_id: Union[Unset, str] = UNSET
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

        workflow_id = self.workflow_id

        workflow_name = self.workflow_name

        webhook_hook_id = self.webhook_hook_id

        webhook_hook_name = self.webhook_hook_name

        location_id = self.location_id

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
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if workflow_name is not UNSET:
            field_dict["workflowName"] = workflow_name
        if webhook_hook_id is not UNSET:
            field_dict["webhookHookId"] = webhook_hook_id
        if webhook_hook_name is not UNSET:
            field_dict["webhookHookName"] = webhook_hook_name
        if location_id is not UNSET:
            field_dict["locationId"] = location_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_template_setup import ToolTemplateSetup

        d = dict(src_dict)
        type_ = GhlToolProviderDetailsType(d.pop("type"))

        template_url = d.pop("templateUrl", UNSET)

        setup_instructions = []
        _setup_instructions = d.pop("setupInstructions", UNSET)
        for setup_instructions_item_data in _setup_instructions or []:
            setup_instructions_item = ToolTemplateSetup.from_dict(setup_instructions_item_data)

            setup_instructions.append(setup_instructions_item)

        workflow_id = d.pop("workflowId", UNSET)

        workflow_name = d.pop("workflowName", UNSET)

        webhook_hook_id = d.pop("webhookHookId", UNSET)

        webhook_hook_name = d.pop("webhookHookName", UNSET)

        location_id = d.pop("locationId", UNSET)

        ghl_tool_provider_details = cls(
            type_=type_,
            template_url=template_url,
            setup_instructions=setup_instructions,
            workflow_id=workflow_id,
            workflow_name=workflow_name,
            webhook_hook_id=webhook_hook_id,
            webhook_hook_name=webhook_hook_name,
            location_id=location_id,
        )

        ghl_tool_provider_details.additional_properties = d
        return ghl_tool_provider_details

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
