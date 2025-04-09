from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCustomerDTO")


@_attrs_define
class CreateCustomerDTO:
    r"""
    Attributes:
        number_e164_check_enabled (Union[Unset, bool]): This is the flag to toggle the E164 check for the `number`
            field. This is an advanced property which should be used if you know your use case requires it.

            Use cases:
            - `false`: To allow non-E164 numbers like `+001234567890`, `1234`, or `abc`. This is useful for dialing out to
            non-E164 numbers on your SIP trunks.
            - `true` (default): To allow only E164 numbers like `+14155551234`. This is standard for PSTN calls.

            If `false`, the `number` is still required to only contain alphanumeric characters (regex:
            `/^\+?[a-zA-Z0-9]+$/`).

            @default true (E164 check is enabled)
        extension (Union[Unset, str]): This is the extension that will be dialed after the call is answered.
        number (Union[Unset, str]): This is the number of the customer.
        sip_uri (Union[Unset, str]): This is the SIP URI of the customer.
        name (Union[Unset, str]): This is the name of the customer. This is just for your own reference.

            For SIP inbound calls, this is extracted from the `From` SIP header with format `"Display Name"
            <sip:username@domain>`.
    """

    number_e164_check_enabled: Union[Unset, bool] = UNSET
    extension: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    sip_uri: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number_e164_check_enabled = self.number_e164_check_enabled

        extension = self.extension

        number = self.number

        sip_uri = self.sip_uri

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number_e164_check_enabled is not UNSET:
            field_dict["numberE164CheckEnabled"] = number_e164_check_enabled
        if extension is not UNSET:
            field_dict["extension"] = extension
        if number is not UNSET:
            field_dict["number"] = number
        if sip_uri is not UNSET:
            field_dict["sipUri"] = sip_uri
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number_e164_check_enabled = d.pop("numberE164CheckEnabled", UNSET)

        extension = d.pop("extension", UNSET)

        number = d.pop("number", UNSET)

        sip_uri = d.pop("sipUri", UNSET)

        name = d.pop("name", UNSET)

        create_customer_dto = cls(
            number_e164_check_enabled=number_e164_check_enabled,
            extension=extension,
            number=number,
            sip_uri=sip_uri,
            name=name,
        )

        create_customer_dto.additional_properties = d
        return create_customer_dto

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
