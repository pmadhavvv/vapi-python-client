from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_message_speech_update_role import ServerMessageSpeechUpdateRole
from ..models.server_message_speech_update_status import ServerMessageSpeechUpdateStatus
from ..models.server_message_speech_update_type import ServerMessageSpeechUpdateType
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


T = TypeVar("T", bound="ServerMessageSpeechUpdate")


@_attrs_define
class ServerMessageSpeechUpdate:
    """
    Attributes:
        type_ (ServerMessageSpeechUpdateType): This is the type of the message. "speech-update" is sent whenever
            assistant or user start or stop speaking.
        status (ServerMessageSpeechUpdateStatus): This is the status of the speech update.
        role (ServerMessageSpeechUpdateRole): This is the role which the speech update is for.
        phone_number (Union['CreateByoPhoneNumberDTO', 'CreateTwilioPhoneNumberDTO', 'CreateVapiPhoneNumberDTO',
            'CreateVonagePhoneNumberDTO', Unset]): This is the phone number associated with the call.

            This matches one of the following:
            - `call.phoneNumber`,
            - `call.phoneNumberId`.
        timestamp (Union[Unset, str]): This is the ISO-8601 formatted timestamp of when the message was sent.
        artifact (Union[Unset, Artifact]):
        assistant (Union[Unset, CreateAssistantDTO]):
        customer (Union[Unset, CreateCustomerDTO]):
        call (Union[Unset, Call]):
    """

    type_: ServerMessageSpeechUpdateType
    status: ServerMessageSpeechUpdateStatus
    role: ServerMessageSpeechUpdateRole
    phone_number: Union[
        "CreateByoPhoneNumberDTO",
        "CreateTwilioPhoneNumberDTO",
        "CreateVapiPhoneNumberDTO",
        "CreateVonagePhoneNumberDTO",
        Unset,
    ] = UNSET
    timestamp: Union[Unset, str] = UNSET
    artifact: Union[Unset, "Artifact"] = UNSET
    assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    customer: Union[Unset, "CreateCustomerDTO"] = UNSET
    call: Union[Unset, "Call"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
        from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
        from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO

        type_ = self.type_.value

        status = self.status.value

        role = self.role.value

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "status": status,
                "role": role,
            }
        )
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.artifact import Artifact
        from ..models.call import Call
        from ..models.create_assistant_dto import CreateAssistantDTO
        from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
        from ..models.create_customer_dto import CreateCustomerDTO
        from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
        from ..models.create_vapi_phone_number_dto import CreateVapiPhoneNumberDTO
        from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO

        d = src_dict.copy()
        type_ = ServerMessageSpeechUpdateType(d.pop("type"))

        status = ServerMessageSpeechUpdateStatus(d.pop("status"))

        role = ServerMessageSpeechUpdateRole(d.pop("role"))

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

        server_message_speech_update = cls(
            type_=type_,
            status=status,
            role=role,
            phone_number=phone_number,
            timestamp=timestamp,
            artifact=artifact,
            assistant=assistant,
            customer=customer,
            call=call,
        )

        server_message_speech_update.additional_properties = d
        return server_message_speech_update

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
