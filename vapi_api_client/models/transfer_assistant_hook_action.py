from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transfer_assistant_hook_action_type import TransferAssistantHookActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transfer_destination_number import TransferDestinationNumber
    from ..models.transfer_destination_sip import TransferDestinationSip


T = TypeVar("T", bound="TransferAssistantHookAction")


@_attrs_define
class TransferAssistantHookAction:
    """
    Attributes:
        type_ (TransferAssistantHookActionType): This is the type of action - must be "transfer"
        destination (Union['TransferDestinationNumber', 'TransferDestinationSip', Unset]): This is the destination
            details for the transfer - can be a phone number or SIP URI
    """

    type_: TransferAssistantHookActionType
    destination: Union["TransferDestinationNumber", "TransferDestinationSip", Unset] = UNSET
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if destination is not UNSET:
            field_dict["destination"] = destination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_sip import TransferDestinationSip

        d = dict(src_dict)
        type_ = TransferAssistantHookActionType(d.pop("type"))

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

        transfer_assistant_hook_action = cls(
            type_=type_,
            destination=destination,
        )

        transfer_assistant_hook_action.additional_properties = d
        return transfer_assistant_hook_action

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
