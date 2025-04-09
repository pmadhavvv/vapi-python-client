from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_inbound_message_transfer_type import ClientInboundMessageTransferType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transfer_destination_number import TransferDestinationNumber
    from ..models.transfer_destination_sip import TransferDestinationSip


T = TypeVar("T", bound="ClientInboundMessageTransfer")


@_attrs_define
class ClientInboundMessageTransfer:
    """
    Attributes:
        type_ (ClientInboundMessageTransferType): This is the type of the message. Send "transfer" message to transfer
            the call to a destination.
        destination (Union['TransferDestinationNumber', 'TransferDestinationSip', Unset]): This is the destination to
            transfer the call to.
        content (Union[Unset, str]): This is the content to say.
    """

    type_: ClientInboundMessageTransferType
    destination: Union["TransferDestinationNumber", "TransferDestinationSip", Unset] = UNSET
    content: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transfer_destination_number import TransferDestinationNumber

        type_ = self.type_.value

        destination: Union[Unset, dict[str, Any]]
        if isinstance(self.destination, Unset):
            destination = UNSET
        elif isinstance(self.destination, TransferDestinationNumber):
            destination = self.destination.to_dict()
        else:
            destination = self.destination.to_dict()

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if destination is not UNSET:
            field_dict["destination"] = destination
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_sip import TransferDestinationSip

        d = dict(src_dict)
        type_ = ClientInboundMessageTransferType(d.pop("type"))

        def _parse_destination(data: object) -> Union["TransferDestinationNumber", "TransferDestinationSip", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                destination_type_0 = TransferDestinationNumber.from_dict(data)

                return destination_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            destination_type_1 = TransferDestinationSip.from_dict(data)

            return destination_type_1

        destination = _parse_destination(d.pop("destination", UNSET))

        content = d.pop("content", UNSET)

        client_inbound_message_transfer = cls(
            type_=type_,
            destination=destination,
            content=content,
        )

        client_inbound_message_transfer.additional_properties = d
        return client_inbound_message_transfer

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
