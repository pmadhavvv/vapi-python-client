from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompliancePlan")


@_attrs_define
class CompliancePlan:
    """
    Attributes:
        hipaa_enabled (Union[Unset, bool]): When this is enabled, no logs, recordings, or transcriptions will be stored.
            At the end of the call, you will still receive an end-of-call-report message to store on your server. Defaults
            to false. Example: {'hipaaEnabled': False}.
        pci_enabled (Union[Unset, bool]): When this is enabled, the user will be restricted to use PCI-compliant
            providers, and no logs or transcripts are stored. At the end of the call, you will receive an end-of-call-report
            message to store on your server. Defaults to false. Example: {'pciEnabled': False}.
    """

    hipaa_enabled: Union[Unset, bool] = UNSET
    pci_enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hipaa_enabled = self.hipaa_enabled

        pci_enabled = self.pci_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hipaa_enabled is not UNSET:
            field_dict["hipaaEnabled"] = hipaa_enabled
        if pci_enabled is not UNSET:
            field_dict["pciEnabled"] = pci_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        hipaa_enabled = d.pop("hipaaEnabled", UNSET)

        pci_enabled = d.pop("pciEnabled", UNSET)

        compliance_plan = cls(
            hipaa_enabled=hipaa_enabled,
            pci_enabled=pci_enabled,
        )

        compliance_plan.additional_properties = d
        return compliance_plan

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
