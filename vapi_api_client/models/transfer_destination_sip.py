from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transfer_destination_sip_type import TransferDestinationSipType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_message import CustomMessage
    from ..models.transfer_destination_sip_sip_headers import TransferDestinationSipSipHeaders
    from ..models.transfer_plan import TransferPlan


T = TypeVar("T", bound="TransferDestinationSip")


@_attrs_define
class TransferDestinationSip:
    """
    Attributes:
        type_ (TransferDestinationSipType):
        sip_uri (str): This is the SIP URI to transfer the call to.
        message (Union['CustomMessage', Unset, str]): This is spoken to the customer before connecting them to the
            destination.

            Usage:
            - If this is not provided and transfer tool messages is not provided, default is "Transferring the call now".
            - If set to "", nothing is spoken. This is useful when you want to silently transfer. This is especially useful
            when transferring between assistants in a squad. In this scenario, you likely also want to set
            `assistant.firstMessageMode=assistant-speaks-first-with-model-generated-message` for the destination assistant.

            This accepts a string or a ToolMessageStart class. Latter is useful if you want to specify multiple messages for
            different languages through the `contents` field.
        transfer_plan (Union[Unset, TransferPlan]):
        sip_headers (Union[Unset, TransferDestinationSipSipHeaders]): These are custom headers to be added to SIP refer
            during transfer call.
        description (Union[Unset, str]): This is the description of the destination, used by the AI to choose when and
            how to transfer the call.
    """

    type_: TransferDestinationSipType
    sip_uri: str
    message: Union["CustomMessage", Unset, str] = UNSET
    transfer_plan: Union[Unset, "TransferPlan"] = UNSET
    sip_headers: Union[Unset, "TransferDestinationSipSipHeaders"] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_message import CustomMessage

        type_ = self.type_.value

        sip_uri = self.sip_uri

        message: Union[Unset, dict[str, Any], str]
        if isinstance(self.message, Unset):
            message = UNSET
        elif isinstance(self.message, CustomMessage):
            message = self.message.to_dict()
        else:
            message = self.message

        transfer_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transfer_plan, Unset):
            transfer_plan = self.transfer_plan.to_dict()

        sip_headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sip_headers, Unset):
            sip_headers = self.sip_headers.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "sipUri": sip_uri,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if transfer_plan is not UNSET:
            field_dict["transferPlan"] = transfer_plan
        if sip_headers is not UNSET:
            field_dict["sipHeaders"] = sip_headers
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.custom_message import CustomMessage
        from ..models.transfer_destination_sip_sip_headers import TransferDestinationSipSipHeaders
        from ..models.transfer_plan import TransferPlan

        d = src_dict.copy()
        type_ = TransferDestinationSipType(d.pop("type"))

        sip_uri = d.pop("sipUri")

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

        _transfer_plan = d.pop("transferPlan", UNSET)
        transfer_plan: Union[Unset, TransferPlan]
        if isinstance(_transfer_plan, Unset):
            transfer_plan = UNSET
        else:
            transfer_plan = TransferPlan.from_dict(_transfer_plan)

        _sip_headers = d.pop("sipHeaders", UNSET)
        sip_headers: Union[Unset, TransferDestinationSipSipHeaders]
        if isinstance(_sip_headers, Unset):
            sip_headers = UNSET
        else:
            sip_headers = TransferDestinationSipSipHeaders.from_dict(_sip_headers)

        description = d.pop("description", UNSET)

        transfer_destination_sip = cls(
            type_=type_,
            sip_uri=sip_uri,
            message=message,
            transfer_plan=transfer_plan,
            sip_headers=sip_headers,
            description=description,
        )

        transfer_destination_sip.additional_properties = d
        return transfer_destination_sip

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
