from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transfer_destination_number_type import TransferDestinationNumberType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_message import CustomMessage
    from ..models.transfer_plan import TransferPlan


T = TypeVar("T", bound="TransferDestinationNumber")


@_attrs_define
class TransferDestinationNumber:
    r"""
    Attributes:
        type_ (TransferDestinationNumberType):
        number (str): This is the phone number to transfer the call to.
        message (Union['CustomMessage', Unset, str]): This is spoken to the customer before connecting them to the
            destination.

            Usage:
            - If this is not provided and transfer tool messages is not provided, default is "Transferring the call now".
            - If set to "", nothing is spoken. This is useful when you want to silently transfer. This is especially useful
            when transferring between assistants in a squad. In this scenario, you likely also want to set
            `assistant.firstMessageMode=assistant-speaks-first-with-model-generated-message` for the destination assistant.

            This accepts a string or a ToolMessageStart class. Latter is useful if you want to specify multiple messages for
            different languages through the `contents` field.
        number_e164_check_enabled (Union[Unset, bool]): This is the flag to toggle the E164 check for the `number`
            field. This is an advanced property which should be used if you know your use case requires it.

            Use cases:
            - `false`: To allow non-E164 numbers like `+001234567890`, `1234`, or `abc`. This is useful for dialing out to
            non-E164 numbers on your SIP trunks.
            - `true` (default): To allow only E164 numbers like `+14155551234`. This is standard for PSTN calls.

            If `false`, the `number` is still required to only contain alphanumeric characters (regex:
            `/^\+?[a-zA-Z0-9]+$/`).

            @default true (E164 check is enabled)
        extension (Union[Unset, str]): This is the extension to dial after transferring the call to the `number`.
        caller_id (Union[Unset, str]): This is the caller ID to use when transferring the call to the `number`.

            Usage:
            - If not provided, the caller ID will be the number the call is coming from. Example, +14151111111 calls in to
            and the assistant transfers out to +16470000000. +16470000000 will see +14151111111 as the caller.
            - To change this behavior, provide a `callerId`.
            - Set to '{{customer.number}}' to always use the customer's number as the caller ID.
            - Set to '{{phoneNumber.number}}' to always use the phone number of the assistant as the caller ID.
            - Set to any E164 number to always use that number as the caller ID. This needs to be a number that is owned or
            verified by your Transport provider like Twilio.

            For Twilio, you can read up more here: https://www.twilio.com/docs/voice/twiml/dial#callerid
        transfer_plan (Union[Unset, TransferPlan]):
        description (Union[Unset, str]): This is the description of the destination, used by the AI to choose when and
            how to transfer the call.
    """

    type_: TransferDestinationNumberType
    number: str
    message: Union["CustomMessage", Unset, str] = UNSET
    number_e164_check_enabled: Union[Unset, bool] = UNSET
    extension: Union[Unset, str] = UNSET
    caller_id: Union[Unset, str] = UNSET
    transfer_plan: Union[Unset, "TransferPlan"] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_message import CustomMessage

        type_ = self.type_.value

        number = self.number

        message: Union[Unset, dict[str, Any], str]
        if isinstance(self.message, Unset):
            message = UNSET
        elif isinstance(self.message, CustomMessage):
            message = self.message.to_dict()
        else:
            message = self.message

        number_e164_check_enabled = self.number_e164_check_enabled

        extension = self.extension

        caller_id = self.caller_id

        transfer_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transfer_plan, Unset):
            transfer_plan = self.transfer_plan.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "number": number,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if number_e164_check_enabled is not UNSET:
            field_dict["numberE164CheckEnabled"] = number_e164_check_enabled
        if extension is not UNSET:
            field_dict["extension"] = extension
        if caller_id is not UNSET:
            field_dict["callerId"] = caller_id
        if transfer_plan is not UNSET:
            field_dict["transferPlan"] = transfer_plan
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.custom_message import CustomMessage
        from ..models.transfer_plan import TransferPlan

        d = src_dict.copy()
        type_ = TransferDestinationNumberType(d.pop("type"))

        number = d.pop("number")

        def _parse_message(data: object) -> Union["CustomMessage", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_1 = CustomMessage.from_dict(data)

                return message_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CustomMessage", Unset, str], data)

        message = _parse_message(d.pop("message", UNSET))

        number_e164_check_enabled = d.pop("numberE164CheckEnabled", UNSET)

        extension = d.pop("extension", UNSET)

        caller_id = d.pop("callerId", UNSET)

        _transfer_plan = d.pop("transferPlan", UNSET)
        transfer_plan: Union[Unset, TransferPlan]
        if isinstance(_transfer_plan, Unset):
            transfer_plan = UNSET
        else:
            transfer_plan = TransferPlan.from_dict(_transfer_plan)

        description = d.pop("description", UNSET)

        transfer_destination_number = cls(
            type_=type_,
            number=number,
            message=message,
            number_e164_check_enabled=number_e164_check_enabled,
            extension=extension,
            caller_id=caller_id,
            transfer_plan=transfer_plan,
            description=description,
        )

        transfer_destination_number.additional_properties = d
        return transfer_destination_number

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
