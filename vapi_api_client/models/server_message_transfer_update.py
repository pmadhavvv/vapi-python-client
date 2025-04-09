from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_message_transfer_update_type import ServerMessageTransferUpdateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artifact import Artifact
    from ..models.call import Call
    from ..models.create_assistant_dto import CreateAssistantDTO
    from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
    from ..models.create_customer_dto import CreateCustomerDTO
    from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
    from ..models.create_vapi_phone_number_dto import CreateVapiPhoneNumberDTO
    from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
    from ..models.server_message_transfer_update_from_step_record import ServerMessageTransferUpdateFromStepRecord
    from ..models.server_message_transfer_update_to_step_record import ServerMessageTransferUpdateToStepRecord
    from ..models.transfer_destination_assistant import TransferDestinationAssistant
    from ..models.transfer_destination_number import TransferDestinationNumber
    from ..models.transfer_destination_sip import TransferDestinationSip
    from ..models.transfer_destination_step import TransferDestinationStep


T = TypeVar("T", bound="ServerMessageTransferUpdate")


@_attrs_define
class ServerMessageTransferUpdate:
    """
    Attributes:
        type_ (ServerMessageTransferUpdateType): This is the type of the message. "transfer-update" is sent whenever a
            transfer happens.
        phone_number (Union['CreateByoPhoneNumberDTO', 'CreateTwilioPhoneNumberDTO', 'CreateVapiPhoneNumberDTO',
            'CreateVonagePhoneNumberDTO', Unset]): This is the phone number associated with the call.

            This matches one of the following:
            - `call.phoneNumber`,
            - `call.phoneNumberId`.
        destination (Union['TransferDestinationAssistant', 'TransferDestinationNumber', 'TransferDestinationSip',
            'TransferDestinationStep', Unset]): This is the destination of the transfer.
        timestamp (Union[Unset, str]): This is the ISO-8601 formatted timestamp of when the message was sent.
        artifact (Union[Unset, Artifact]):
        assistant (Union[Unset, CreateAssistantDTO]):
        customer (Union[Unset, CreateCustomerDTO]):
        call (Union[Unset, Call]):
        to_assistant (Union[Unset, CreateAssistantDTO]):
        from_assistant (Union[Unset, CreateAssistantDTO]):
        to_step_record (Union[Unset, ServerMessageTransferUpdateToStepRecord]): This is the step that the conversation
            moved to.
        from_step_record (Union[Unset, ServerMessageTransferUpdateFromStepRecord]): This is the step that the
            conversation moved from. =
    """

    type_: ServerMessageTransferUpdateType
    phone_number: Union[
        "CreateByoPhoneNumberDTO",
        "CreateTwilioPhoneNumberDTO",
        "CreateVapiPhoneNumberDTO",
        "CreateVonagePhoneNumberDTO",
        Unset,
    ] = UNSET
    destination: Union[
        "TransferDestinationAssistant",
        "TransferDestinationNumber",
        "TransferDestinationSip",
        "TransferDestinationStep",
        Unset,
    ] = UNSET
    timestamp: Union[Unset, str] = UNSET
    artifact: Union[Unset, "Artifact"] = UNSET
    assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    customer: Union[Unset, "CreateCustomerDTO"] = UNSET
    call: Union[Unset, "Call"] = UNSET
    to_assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    from_assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    to_step_record: Union[Unset, "ServerMessageTransferUpdateToStepRecord"] = UNSET
    from_step_record: Union[Unset, "ServerMessageTransferUpdateFromStepRecord"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
        from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
        from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
        from ..models.transfer_destination_assistant import TransferDestinationAssistant
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_step import TransferDestinationStep

        type_ = self.type_.value

        phone_number: Union[Unset, dict[str, Any]]
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        elif isinstance(self.phone_number, CreateByoPhoneNumberDTO):
            phone_number = self.phone_number.to_dict()
        elif isinstance(self.phone_number, CreateTwilioPhoneNumberDTO):
            phone_number = self.phone_number.to_dict()
        elif isinstance(self.phone_number, CreateVonagePhoneNumberDTO):
            phone_number = self.phone_number.to_dict()
        else:
            phone_number = self.phone_number.to_dict()

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

        timestamp = self.timestamp

        artifact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artifact, Unset):
            artifact = self.artifact.to_dict()

        assistant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assistant, Unset):
            assistant = self.assistant.to_dict()

        customer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        call: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.call, Unset):
            call = self.call.to_dict()

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
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if destination is not UNSET:
            field_dict["destination"] = destination
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if artifact is not UNSET:
            field_dict["artifact"] = artifact
        if assistant is not UNSET:
            field_dict["assistant"] = assistant
        if customer is not UNSET:
            field_dict["customer"] = customer
        if call is not UNSET:
            field_dict["call"] = call
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
        from ..models.artifact import Artifact
        from ..models.call import Call
        from ..models.create_assistant_dto import CreateAssistantDTO
        from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
        from ..models.create_customer_dto import CreateCustomerDTO
        from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
        from ..models.create_vapi_phone_number_dto import CreateVapiPhoneNumberDTO
        from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
        from ..models.server_message_transfer_update_from_step_record import ServerMessageTransferUpdateFromStepRecord
        from ..models.server_message_transfer_update_to_step_record import ServerMessageTransferUpdateToStepRecord
        from ..models.transfer_destination_assistant import TransferDestinationAssistant
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_sip import TransferDestinationSip
        from ..models.transfer_destination_step import TransferDestinationStep

        d = dict(src_dict)
        type_ = ServerMessageTransferUpdateType(d.pop("type"))

        def _parse_phone_number(
            data: object,
        ) -> Union[
            "CreateByoPhoneNumberDTO",
            "CreateTwilioPhoneNumberDTO",
            "CreateVapiPhoneNumberDTO",
            "CreateVonagePhoneNumberDTO",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                phone_number_type_0 = CreateByoPhoneNumberDTO.from_dict(data)

                return phone_number_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                phone_number_type_1 = CreateTwilioPhoneNumberDTO.from_dict(data)

                return phone_number_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                phone_number_type_2 = CreateVonagePhoneNumberDTO.from_dict(data)

                return phone_number_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            phone_number_type_3 = CreateVapiPhoneNumberDTO.from_dict(data)

            return phone_number_type_3

        phone_number = _parse_phone_number(d.pop("phoneNumber", UNSET))

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

        timestamp = d.pop("timestamp", UNSET)

        _artifact = d.pop("artifact", UNSET)
        artifact: Union[Unset, Artifact]
        if isinstance(_artifact, Unset):
            artifact = UNSET
        else:
            artifact = Artifact.from_dict(_artifact)

        _assistant = d.pop("assistant", UNSET)
        assistant: Union[Unset, CreateAssistantDTO]
        if isinstance(_assistant, Unset):
            assistant = UNSET
        else:
            assistant = CreateAssistantDTO.from_dict(_assistant)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, CreateCustomerDTO]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CreateCustomerDTO.from_dict(_customer)

        _call = d.pop("call", UNSET)
        call: Union[Unset, Call]
        if isinstance(_call, Unset):
            call = UNSET
        else:
            call = Call.from_dict(_call)

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
        to_step_record: Union[Unset, ServerMessageTransferUpdateToStepRecord]
        if isinstance(_to_step_record, Unset):
            to_step_record = UNSET
        else:
            to_step_record = ServerMessageTransferUpdateToStepRecord.from_dict(_to_step_record)

        _from_step_record = d.pop("fromStepRecord", UNSET)
        from_step_record: Union[Unset, ServerMessageTransferUpdateFromStepRecord]
        if isinstance(_from_step_record, Unset):
            from_step_record = UNSET
        else:
            from_step_record = ServerMessageTransferUpdateFromStepRecord.from_dict(_from_step_record)

        server_message_transfer_update = cls(
            type_=type_,
            phone_number=phone_number,
            destination=destination,
            timestamp=timestamp,
            artifact=artifact,
            assistant=assistant,
            customer=customer,
            call=call,
            to_assistant=to_assistant,
            from_assistant=from_assistant,
            to_step_record=to_step_record,
            from_step_record=from_step_record,
        )

        server_message_transfer_update.additional_properties = d
        return server_message_transfer_update

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
