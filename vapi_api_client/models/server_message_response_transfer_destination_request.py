from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transfer_destination_assistant import TransferDestinationAssistant
    from ..models.transfer_destination_number import TransferDestinationNumber
    from ..models.transfer_destination_sip import TransferDestinationSip
    from ..models.transfer_destination_step import TransferDestinationStep


T = TypeVar("T", bound="ServerMessageResponseTransferDestinationRequest")


@_attrs_define
class ServerMessageResponseTransferDestinationRequest:
    """
    Attributes:
        destination (Union['TransferDestinationAssistant', 'TransferDestinationNumber', 'TransferDestinationSip',
            'TransferDestinationStep', Unset]): This is the destination you'd like the call to be transferred to.
        error (Union[Unset, str]): This is the error message if the transfer should not be made.
    """

    destination: Union[
        "TransferDestinationAssistant",
        "TransferDestinationNumber",
        "TransferDestinationSip",
        "TransferDestinationStep",
        Unset,
    ] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transfer_destination_assistant import TransferDestinationAssistant
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_step import TransferDestinationStep

        destination: Union[Unset, dict[str, Any]]
        if isinstance(self.destination, Unset):
            destination = UNSET
        elif isinstance(self.destination, TransferDestinationAssistant):
            destination = self.destination.to_dict()
        elif isinstance(self.destination, TransferDestinationStep):
            destination = self.destination.to_dict()
        elif isinstance(self.destination, TransferDestinationNumber):
            destination = self.destination.to_dict()
        else:
            destination = self.destination.to_dict()

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transfer_destination_assistant import TransferDestinationAssistant
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_sip import TransferDestinationSip
        from ..models.transfer_destination_step import TransferDestinationStep

        d = dict(src_dict)

        def _parse_destination(
            data: object,
        ) -> Union[
            "TransferDestinationAssistant",
            "TransferDestinationNumber",
            "TransferDestinationSip",
            "TransferDestinationStep",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                destination_type_0 = TransferDestinationAssistant.from_dict(data)

                return destination_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                destination_type_1 = TransferDestinationStep.from_dict(data)

                return destination_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                destination_type_2 = TransferDestinationNumber.from_dict(data)

                return destination_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            destination_type_3 = TransferDestinationSip.from_dict(data)

            return destination_type_3

        destination = _parse_destination(d.pop("destination", UNSET))

        error = d.pop("error", UNSET)

        server_message_response_transfer_destination_request = cls(
            destination=destination,
            error=error,
        )

        server_message_response_transfer_destination_request.additional_properties = d
        return server_message_response_transfer_destination_request

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
