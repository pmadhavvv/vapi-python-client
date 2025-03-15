import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.token_tag import TokenTag
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token_restrictions import TokenRestrictions


T = TypeVar("T", bound="Token")


@_attrs_define
class Token:
    """
    Attributes:
        id (str): This is the unique identifier for the token.
        org_id (str): This is unique identifier for the org that this token belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the token was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the token was last updated.
        value (str): This is the token key.
        tag (Union[Unset, TokenTag]): This is the tag for the token. It represents its scope.
        name (Union[Unset, str]): This is the name of the token. This is just for your own reference.
        restrictions (Union[Unset, TokenRestrictions]):
    """

    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    value: str
    tag: Union[Unset, TokenTag] = UNSET
    name: Union[Unset, str] = UNSET
    restrictions: Union[Unset, "TokenRestrictions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        value = self.value

        tag: Union[Unset, str] = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.value

        name = self.name

        restrictions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "value": value,
            }
        )
        if tag is not UNSET:
            field_dict["tag"] = tag
        if name is not UNSET:
            field_dict["name"] = name
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.token_restrictions import TokenRestrictions

        d = src_dict.copy()
        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        value = d.pop("value")

        _tag = d.pop("tag", UNSET)
        tag: Union[Unset, TokenTag]
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = TokenTag(_tag)

        name = d.pop("name", UNSET)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: Union[Unset, TokenRestrictions]
        if isinstance(_restrictions, Unset):
            restrictions = UNSET
        else:
            restrictions = TokenRestrictions.from_dict(_restrictions)

        token = cls(
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            value=value,
            tag=tag,
            name=name,
            restrictions=restrictions,
        )

        token.additional_properties = d
        return token

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
