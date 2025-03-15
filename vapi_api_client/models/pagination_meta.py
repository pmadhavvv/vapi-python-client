from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PaginationMeta")


@_attrs_define
class PaginationMeta:
    """
    Attributes:
        items_per_page (float):
        total_items (float):
        current_page (float):
    """

    items_per_page: float
    total_items: float
    current_page: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items_per_page = self.items_per_page

        total_items = self.total_items

        current_page = self.current_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemsPerPage": items_per_page,
                "totalItems": total_items,
                "currentPage": current_page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        items_per_page = d.pop("itemsPerPage")

        total_items = d.pop("totalItems")

        current_page = d.pop("currentPage")

        pagination_meta = cls(
            items_per_page=items_per_page,
            total_items=total_items,
            current_page=current_page,
        )

        pagination_meta.additional_properties = d
        return pagination_meta

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
