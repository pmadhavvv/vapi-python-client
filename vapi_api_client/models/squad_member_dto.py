from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_overrides import AssistantOverrides
    from ..models.create_assistant_dto import CreateAssistantDTO
    from ..models.transfer_destination_assistant import TransferDestinationAssistant


T = TypeVar("T", bound="SquadMemberDTO")


@_attrs_define
class SquadMemberDTO:
    """
    Attributes:
        assistant_id (Union[None, Unset, str]): This is the assistant that will be used for the call. To use a transient
            assistant, use `assistant` instead.
        assistant (Union[Unset, CreateAssistantDTO]):
        assistant_overrides (Union[Unset, AssistantOverrides]):
        assistant_destinations (Union[Unset, list['TransferDestinationAssistant']]): These are the others assistants
            that this assistant can transfer to.

            If the assistant already has transfer call tool, these destinations are just appended to existing ones.
    """

    assistant_id: Union[None, Unset, str] = UNSET
    assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    assistant_overrides: Union[Unset, "AssistantOverrides"] = UNSET
    assistant_destinations: Union[Unset, list["TransferDestinationAssistant"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistant_id: Union[None, Unset, str]
        if isinstance(self.assistant_id, Unset):
            assistant_id = UNSET
        else:
            assistant_id = self.assistant_id

        assistant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assistant, Unset):
            assistant = self.assistant.to_dict()

        assistant_overrides: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assistant_overrides, Unset):
            assistant_overrides = self.assistant_overrides.to_dict()

        assistant_destinations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.assistant_destinations, Unset):
            assistant_destinations = []
            for assistant_destinations_item_data in self.assistant_destinations:
                assistant_destinations_item = assistant_destinations_item_data.to_dict()
                assistant_destinations.append(assistant_destinations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assistant_id is not UNSET:
            field_dict["assistantId"] = assistant_id
        if assistant is not UNSET:
            field_dict["assistant"] = assistant
        if assistant_overrides is not UNSET:
            field_dict["assistantOverrides"] = assistant_overrides
        if assistant_destinations is not UNSET:
            field_dict["assistantDestinations"] = assistant_destinations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assistant_overrides import AssistantOverrides
        from ..models.create_assistant_dto import CreateAssistantDTO
        from ..models.transfer_destination_assistant import TransferDestinationAssistant

        d = dict(src_dict)

        def _parse_assistant_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assistant_id = _parse_assistant_id(d.pop("assistantId", UNSET))

        _assistant = d.pop("assistant", UNSET)
        assistant: Union[Unset, CreateAssistantDTO]
        if isinstance(_assistant, Unset):
            assistant = UNSET
        else:
            assistant = CreateAssistantDTO.from_dict(_assistant)

        _assistant_overrides = d.pop("assistantOverrides", UNSET)
        assistant_overrides: Union[Unset, AssistantOverrides]
        if isinstance(_assistant_overrides, Unset):
            assistant_overrides = UNSET
        else:
            assistant_overrides = AssistantOverrides.from_dict(_assistant_overrides)

        assistant_destinations = []
        _assistant_destinations = d.pop("assistantDestinations", UNSET)
        for assistant_destinations_item_data in _assistant_destinations or []:
            assistant_destinations_item = TransferDestinationAssistant.from_dict(assistant_destinations_item_data)

            assistant_destinations.append(assistant_destinations_item)

        squad_member_dto = cls(
            assistant_id=assistant_id,
            assistant=assistant,
            assistant_overrides=assistant_overrides,
            assistant_destinations=assistant_destinations,
        )

        squad_member_dto.additional_properties = d
        return squad_member_dto

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
