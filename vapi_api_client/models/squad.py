import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_overrides import AssistantOverrides
    from ..models.squad_member_dto import SquadMemberDTO


T = TypeVar("T", bound="Squad")


@_attrs_define
class Squad:
    """
    Attributes:
        members (list['SquadMemberDTO']): This is the list of assistants that make up the squad.

            The call will start with the first assistant in the list.
        id (str): This is the unique identifier for the squad.
        org_id (str): This is the unique identifier for the org that this squad belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the squad was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the squad was last updated.
        name (Union[Unset, str]): This is the name of the squad.
        members_overrides (Union[Unset, AssistantOverrides]):
    """

    members: list["SquadMemberDTO"]
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: Union[Unset, str] = UNSET
    members_overrides: Union[Unset, "AssistantOverrides"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        members_overrides: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.members_overrides, Unset):
            members_overrides = self.members_overrides.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "members": members,
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if members_overrides is not UNSET:
            field_dict["membersOverrides"] = members_overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assistant_overrides import AssistantOverrides
        from ..models.squad_member_dto import SquadMemberDTO

        d = dict(src_dict)
        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = SquadMemberDTO.from_dict(members_item_data)

            members.append(members_item)

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        name = d.pop("name", UNSET)

        _members_overrides = d.pop("membersOverrides", UNSET)
        members_overrides: Union[Unset, AssistantOverrides]
        if isinstance(_members_overrides, Unset):
            members_overrides = UNSET
        else:
            members_overrides = AssistantOverrides.from_dict(_members_overrides)

        squad = cls(
            members=members,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            members_overrides=members_overrides,
        )

        squad.additional_properties = d
        return squad

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
