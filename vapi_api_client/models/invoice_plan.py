from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoicePlan")


@_attrs_define
class InvoicePlan:
    """
    Attributes:
        company_name (Union[Unset, str]): This is the name of the company.
        company_address (Union[Unset, str]): This is the address of the company.
        company_tax_id (Union[Unset, str]): This is the tax ID of the company.
        company_email (Union[Unset, str]): This is the preferred invoicing email of the company. If not specified,
            defaults to the subscription's email.
    """

    company_name: Union[Unset, str] = UNSET
    company_address: Union[Unset, str] = UNSET
    company_tax_id: Union[Unset, str] = UNSET
    company_email: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name = self.company_name

        company_address = self.company_address

        company_tax_id = self.company_tax_id

        company_email = self.company_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if company_address is not UNSET:
            field_dict["companyAddress"] = company_address
        if company_tax_id is not UNSET:
            field_dict["companyTaxId"] = company_tax_id
        if company_email is not UNSET:
            field_dict["companyEmail"] = company_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_name = d.pop("companyName", UNSET)

        company_address = d.pop("companyAddress", UNSET)

        company_tax_id = d.pop("companyTaxId", UNSET)

        company_email = d.pop("companyEmail", UNSET)

        invoice_plan = cls(
            company_name=company_name,
            company_address=company_address,
            company_tax_id=company_tax_id,
            company_email=company_email,
        )

        invoice_plan.additional_properties = d
        return invoice_plan

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
