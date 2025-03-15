from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_user_role_dto_role import UpdateUserRoleDTORole

T = TypeVar("T", bound="UpdateUserRoleDTO")


@_attrs_define
class UpdateUserRoleDTO:
    """
    Attributes:
        user_id (str):
        role (UpdateUserRoleDTORole):
    """

    user_id: str
    role: UpdateUserRoleDTORole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        role = UpdateUserRoleDTORole(d.pop("role"))

        update_user_role_dto = cls(
            user_id=user_id,
            role=role,
        )

        update_user_role_dto.additional_properties = d
        return update_user_role_dto

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
