from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_overrides import AssistantOverrides
    from ..models.create_assistant_dto import CreateAssistantDTO
    from ..models.create_customer_dto import CreateCustomerDTO
    from ..models.create_squad_dto import CreateSquadDTO
    from ..models.import_twilio_phone_number_dto import ImportTwilioPhoneNumberDTO


T = TypeVar("T", bound="CreateCallDTO")


@_attrs_define
class CreateCallDTO:
    """
    Attributes:
        name (Union[Unset, str]): This is the name of the call. This is just for your own reference.
        assistant_id (Union[Unset, str]): This is the assistant that will be used for the call. To use a transient
            assistant, use `assistant` instead.
        assistant (Union[Unset, CreateAssistantDTO]):
        assistant_overrides (Union[Unset, AssistantOverrides]):
        squad_id (Union[Unset, str]): This is the squad that will be used for the call. To use a transient squad, use
            `squad` instead.
        squad (Union[Unset, CreateSquadDTO]):
        phone_number_id (Union[Unset, str]): This is the phone number that will be used for the call. To use a transient
            number, use `phoneNumber` instead.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
        phone_number (Union[Unset, ImportTwilioPhoneNumberDTO]):
        customer_id (Union[Unset, str]): This is the customer that will be called. To call a transient customer , use
            `customer` instead.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
        customer (Union[Unset, CreateCustomerDTO]):
    """

    name: Union[Unset, str] = UNSET
    assistant_id: Union[Unset, str] = UNSET
    assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    assistant_overrides: Union[Unset, "AssistantOverrides"] = UNSET
    squad_id: Union[Unset, str] = UNSET
    squad: Union[Unset, "CreateSquadDTO"] = UNSET
    phone_number_id: Union[Unset, str] = UNSET
    phone_number: Union[Unset, "ImportTwilioPhoneNumberDTO"] = UNSET
    customer_id: Union[Unset, str] = UNSET
    customer: Union[Unset, "CreateCustomerDTO"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        assistant_id = self.assistant_id

        assistant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assistant, Unset):
            assistant = self.assistant.to_dict()

        assistant_overrides: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assistant_overrides, Unset):
            assistant_overrides = self.assistant_overrides.to_dict()

        squad_id = self.squad_id

        squad: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.squad, Unset):
            squad = self.squad.to_dict()

        phone_number_id = self.phone_number_id

        phone_number: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.phone_number, Unset):
            phone_number = self.phone_number.to_dict()

        customer_id = self.customer_id

        customer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if assistant_id is not UNSET:
            field_dict["assistantId"] = assistant_id
        if assistant is not UNSET:
            field_dict["assistant"] = assistant
        if assistant_overrides is not UNSET:
            field_dict["assistantOverrides"] = assistant_overrides
        if squad_id is not UNSET:
            field_dict["squadId"] = squad_id
        if squad is not UNSET:
            field_dict["squad"] = squad
        if phone_number_id is not UNSET:
            field_dict["phoneNumberId"] = phone_number_id
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if customer is not UNSET:
            field_dict["customer"] = customer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.assistant_overrides import AssistantOverrides
        from ..models.create_assistant_dto import CreateAssistantDTO
        from ..models.create_customer_dto import CreateCustomerDTO
        from ..models.create_squad_dto import CreateSquadDTO
        from ..models.import_twilio_phone_number_dto import ImportTwilioPhoneNumberDTO

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        assistant_id = d.pop("assistantId", UNSET)

        _assistant = d.pop("assistant", UNSET)
        assistant: Union[Unset, CreateAssistantDTO]
        if isinstance(_assistant, Unset):
            assistant = UNSET
        else:
            assistant = CreateAssistantDTO.from_dict(_assistant)

        _assistant_overrides = d.pop("assistantOverrides", UNSET)
        assistant_overrides: Union[Unset, AssistantOverrides]
        if isinstance(_assistant_overrides, Unset):
            assistant_overrides = UNSET
        else:
            assistant_overrides = AssistantOverrides.from_dict(_assistant_overrides)

        squad_id = d.pop("squadId", UNSET)

        _squad = d.pop("squad", UNSET)
        squad: Union[Unset, CreateSquadDTO]
        if isinstance(_squad, Unset):
            squad = UNSET
        else:
            squad = CreateSquadDTO.from_dict(_squad)

        phone_number_id = d.pop("phoneNumberId", UNSET)

        _phone_number = d.pop("phoneNumber", UNSET)
        phone_number: Union[Unset, ImportTwilioPhoneNumberDTO]
        if isinstance(_phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = ImportTwilioPhoneNumberDTO.from_dict(_phone_number)

        customer_id = d.pop("customerId", UNSET)

        _customer = d.pop("customer", UNSET)
        customer: Union[Unset, CreateCustomerDTO]
        if isinstance(_customer, Unset):
            customer = UNSET
        else:
            customer = CreateCustomerDTO.from_dict(_customer)

        create_call_dto = cls(
            name=name,
            assistant_id=assistant_id,
            assistant=assistant,
            assistant_overrides=assistant_overrides,
            squad_id=squad_id,
            squad=squad,
            phone_number_id=phone_number_id,
            phone_number=phone_number,
            customer_id=customer_id,
            customer=customer,
        )

        create_call_dto.additional_properties = d
        return create_call_dto

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
