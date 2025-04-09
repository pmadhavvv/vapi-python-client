from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_message_transfer_update_type import ClientMessageTransferUpdateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_message_transfer_update_from_step_record import ClientMessageTransferUpdateFromStepRecord
    from ..models.client_message_transfer_update_to_step_record import ClientMessageTransferUpdateToStepRecord
    from ..models.create_assistant_dto import CreateAssistantDTO
    from ..models.transfer_destination_assistant import TransferDestinationAssistant
    from ..models.transfer_destination_number import TransferDestinationNumber
    from ..models.transfer_destination_sip import TransferDestinationSip
    from ..models.transfer_destination_step import TransferDestinationStep


T = TypeVar("T", bound="ClientMessageTransferUpdate")


@_attrs_define
class ClientMessageTransferUpdate:
    """
    Attributes:
        type_ (ClientMessageTransferUpdateType): This is the type of the message. "transfer-update" is sent whenever a
            transfer happens.
        destination (Union['TransferDestinationAssistant', 'TransferDestinationNumber', 'TransferDestinationSip',
            'TransferDestinationStep', Unset]): This is the destination of the transfer.
        to_assistant (Union[Unset, CreateAssistantDTO]):
        from_assistant (Union[Unset, CreateAssistantDTO]):
        to_step_record (Union[Unset, ClientMessageTransferUpdateToStepRecord]): This is the step that the conversation
            moved to.
        from_step_record (Union[Unset, ClientMessageTransferUpdateFromStepRecord]): This is the step that the
            conversation moved from. =
    """

    type_: ClientMessageTransferUpdateType
    destination: Union[
        "TransferDestinationAssistant",
        "TransferDestinationNumber",
        "TransferDestinationSip",
        "TransferDestinationStep",
        Unset,
    ] = UNSET
    to_assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    from_assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    to_step_record: Union[Unset, "ClientMessageTransferUpdateToStepRecord"] = UNSET
    from_step_record: Union[Unset, "ClientMessageTransferUpdateFromStepRecord"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transfer_destination_assistant import TransferDestinationAssistant
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_step import TransferDestinationStep

        type_ = self.type_.value

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

        to_assistant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to_assistant, Unset):
            to_assistant = self.to_assistant.to_dict()

        from_assistant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_assistant, Unset):
            from_assistant = self.from_assistant.to_dict()

        to_step_record: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to_step_record, Unset):
            to_step_record = self.to_step_record.to_dict()

        from_step_record: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_step_record, Unset):
            from_step_record = self.from_step_record.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if destination is not UNSET:
            field_dict["destination"] = destination
        if to_assistant is not UNSET:
            field_dict["toAssistant"] = to_assistant
        if from_assistant is not UNSET:
            field_dict["fromAssistant"] = from_assistant
        if to_step_record is not UNSET:
            field_dict["toStepRecord"] = to_step_record
        if from_step_record is not UNSET:
            field_dict["fromStepRecord"] = from_step_record

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_message_transfer_update_from_step_record import ClientMessageTransferUpdateFromStepRecord
        from ..models.client_message_transfer_update_to_step_record import ClientMessageTransferUpdateToStepRecord
        from ..models.create_assistant_dto import CreateAssistantDTO
        from ..models.transfer_destination_assistant import TransferDestinationAssistant
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_sip import TransferDestinationSip
        from ..models.transfer_destination_step import TransferDestinationStep

        d = dict(src_dict)
        type_ = ClientMessageTransferUpdateType(d.pop("type"))

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

        _to_assistant = d.pop("toAssistant", UNSET)
        to_assistant: Union[Unset, CreateAssistantDTO]
        if isinstance(_to_assistant, Unset):
            to_assistant = UNSET
        else:
            to_assistant = CreateAssistantDTO.from_dict(_to_assistant)

        _from_assistant = d.pop("fromAssistant", UNSET)
        from_assistant: Union[Unset, CreateAssistantDTO]
        if isinstance(_from_assistant, Unset):
            from_assistant = UNSET
        else:
            from_assistant = CreateAssistantDTO.from_dict(_from_assistant)

        _to_step_record = d.pop("toStepRecord", UNSET)
        to_step_record: Union[Unset, ClientMessageTransferUpdateToStepRecord]
        if isinstance(_to_step_record, Unset):
            to_step_record = UNSET
        else:
            to_step_record = ClientMessageTransferUpdateToStepRecord.from_dict(_to_step_record)

        _from_step_record = d.pop("fromStepRecord", UNSET)
        from_step_record: Union[Unset, ClientMessageTransferUpdateFromStepRecord]
        if isinstance(_from_step_record, Unset):
            from_step_record = UNSET
        else:
            from_step_record = ClientMessageTransferUpdateFromStepRecord.from_dict(_from_step_record)

        client_message_transfer_update = cls(
            type_=type_,
            destination=destination,
            to_assistant=to_assistant,
            from_assistant=from_assistant,
            to_step_record=to_step_record,
            from_step_record=from_step_record,
        )

        client_message_transfer_update.additional_properties = d
        return client_message_transfer_update

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
