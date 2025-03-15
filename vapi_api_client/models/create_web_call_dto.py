from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_overrides import AssistantOverrides
    from ..models.create_assistant_dto import CreateAssistantDTO
    from ..models.create_squad_dto import CreateSquadDTO


T = TypeVar("T", bound="CreateWebCallDTO")


@_attrs_define
class CreateWebCallDTO:
    """
    Attributes:
        assistant_id (Union[Unset, str]): This is the assistant that will be used for the call. To use a transient
            assistant, use `assistant` instead.
        assistant (Union[Unset, CreateAssistantDTO]):
        assistant_overrides (Union[Unset, AssistantOverrides]):
        squad_id (Union[Unset, str]): This is the squad that will be used for the call. To use a transient squad, use
            `squad` instead.
        squad (Union[Unset, CreateSquadDTO]):
    """

    assistant_id: Union[Unset, str] = UNSET
    assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    assistant_overrides: Union[Unset, "AssistantOverrides"] = UNSET
    squad_id: Union[Unset, str] = UNSET
    squad: Union[Unset, "CreateSquadDTO"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistant_id = self.assistant_id

        assistant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assistant, Unset):
            assistant = self.assistant.to_dict()

        assistant_overrides: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assistant_overrides, Unset):
            assistant_overrides = self.assistant_overrides.to_dict()

        squad_id = self.squad_id

        squad: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.squad, Unset):
            squad = self.squad.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assistant_id is not UNSET:
            field_dict["assistantId"] = assistant_id
        if assistant is not UNSET:
            field_dict["assistant"] = assistant
        if assistant_overrides is not UNSET:
            field_dict["assistantOverrides"] = assistant_overrides
        if squad_id is not UNSET:
            field_dict["squadId"] = squad_id
        if squad is not UNSET:
            field_dict["squad"] = squad

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.assistant_overrides import AssistantOverrides
        from ..models.create_assistant_dto import CreateAssistantDTO
        from ..models.create_squad_dto import CreateSquadDTO

        d = src_dict.copy()
        assistant_id = d.pop("assistantId", UNSET)

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

        squad_id = d.pop("squadId", UNSET)

        _squad = d.pop("squad", UNSET)
        squad: Union[Unset, CreateSquadDTO]
        if isinstance(_squad, Unset):
            squad = UNSET
        else:
            squad = CreateSquadDTO.from_dict(_squad)

        create_web_call_dto = cls(
            assistant_id=assistant_id,
            assistant=assistant,
            assistant_overrides=assistant_overrides,
            squad_id=squad_id,
            squad=squad,
        )

        create_web_call_dto.additional_properties = d
        return create_web_call_dto

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
