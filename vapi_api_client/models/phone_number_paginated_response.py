from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.byo_phone_number import ByoPhoneNumber
    from ..models.pagination_meta import PaginationMeta
    from ..models.telnyx_phone_number import TelnyxPhoneNumber
    from ..models.twilio_phone_number import TwilioPhoneNumber
    from ..models.vapi_phone_number import VapiPhoneNumber
    from ..models.vonage_phone_number import VonagePhoneNumber


T = TypeVar("T", bound="PhoneNumberPaginatedResponse")


@_attrs_define
class PhoneNumberPaginatedResponse:
    """
    Attributes:
        results (list[Union['ByoPhoneNumber', 'TelnyxPhoneNumber', 'TwilioPhoneNumber', 'VapiPhoneNumber',
            'VonagePhoneNumber']]): A list of phone numbers, which can be of any provider type.
        metadata (PaginationMeta):
    """

    results: list[
        Union["ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"]
    ]
    metadata: "PaginationMeta"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.byo_phone_number import ByoPhoneNumber
        from ..models.twilio_phone_number import TwilioPhoneNumber
        from ..models.vapi_phone_number import VapiPhoneNumber
        from ..models.vonage_phone_number import VonagePhoneNumber

        results = []
        for results_item_data in self.results:
            results_item: dict[str, Any]
            if isinstance(results_item_data, ByoPhoneNumber):
                results_item = results_item_data.to_dict()
            elif isinstance(results_item_data, TwilioPhoneNumber):
                results_item = results_item_data.to_dict()
            elif isinstance(results_item_data, VonagePhoneNumber):
                results_item = results_item_data.to_dict()
            elif isinstance(results_item_data, VapiPhoneNumber):
                results_item = results_item_data.to_dict()
            else:
                results_item = results_item_data.to_dict()

            results.append(results_item)

        metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.byo_phone_number import ByoPhoneNumber
        from ..models.pagination_meta import PaginationMeta
        from ..models.telnyx_phone_number import TelnyxPhoneNumber
        from ..models.twilio_phone_number import TwilioPhoneNumber
        from ..models.vapi_phone_number import VapiPhoneNumber
        from ..models.vonage_phone_number import VonagePhoneNumber

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:

            def _parse_results_item(
                data: object,
            ) -> Union[
                "ByoPhoneNumber", "TelnyxPhoneNumber", "TwilioPhoneNumber", "VapiPhoneNumber", "VonagePhoneNumber"
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_0 = ByoPhoneNumber.from_dict(data)

                    return results_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_1 = TwilioPhoneNumber.from_dict(data)

                    return results_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_2 = VonagePhoneNumber.from_dict(data)

                    return results_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_3 = VapiPhoneNumber.from_dict(data)

                    return results_item_type_3
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                results_item_type_4 = TelnyxPhoneNumber.from_dict(data)

                return results_item_type_4

            results_item = _parse_results_item(results_item_data)

            results.append(results_item)

        metadata = PaginationMeta.from_dict(d.pop("metadata"))

        phone_number_paginated_response = cls(
            results=results,
            metadata=metadata,
        )

        phone_number_paginated_response.additional_properties = d
        return phone_number_paginated_response

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
