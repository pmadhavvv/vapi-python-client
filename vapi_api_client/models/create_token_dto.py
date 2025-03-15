from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_token_dto_tag import CreateTokenDTOTag
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.token_restrictions import TokenRestrictions


T = TypeVar("T", bound="CreateTokenDTO")


@_attrs_define
class CreateTokenDTO:
    """
    Attributes:
        tag (Union[Unset, CreateTokenDTOTag]): This is the tag for the token. It represents its scope.
        name (Union[Unset, str]): This is the name of the token. This is just for your own reference.
        restrictions (Union[Unset, TokenRestrictions]):
    """

    tag: Union[Unset, CreateTokenDTOTag] = UNSET
    name: Union[Unset, str] = UNSET
    restrictions: Union[Unset, "TokenRestrictions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag: Union[Unset, str] = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.value

        name = self.name

        restrictions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        _tag = d.pop("tag", UNSET)
        tag: Union[Unset, CreateTokenDTOTag]
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = CreateTokenDTOTag(_tag)

        name = d.pop("name", UNSET)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: Union[Unset, TokenRestrictions]
        if isinstance(_restrictions, Unset):
            restrictions = UNSET
        else:
            restrictions = TokenRestrictions.from_dict(_restrictions)

        create_token_dto = cls(
            tag=tag,
            name=name,
            restrictions=restrictions,
        )

        create_token_dto.additional_properties = d
        return create_token_dto

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
