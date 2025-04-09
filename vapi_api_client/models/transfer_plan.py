from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transfer_plan_mode import TransferPlanMode
from ..models.transfer_plan_sip_verb import TransferPlanSipVerb
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_message import CustomMessage
    from ..models.summary_plan import SummaryPlan


T = TypeVar("T", bound="TransferPlan")


@_attrs_define
class TransferPlan:
    """
    Attributes:
        mode (TransferPlanMode): This configures how transfer is executed and the experience of the destination party
            receiving the call.

            Usage:
            - `blind-transfer`: The assistant forwards the call to the destination without any message or summary.
            - `blind-transfer-add-summary-to-sip-header`: The assistant forwards the call to the destination and adds a SIP
            header X-Transfer-Summary to the call to include the summary.
            - `warm-transfer-say-message`: The assistant dials the destination, delivers the `message` to the destination
            party, connects the customer, and leaves the call.
            - `warm-transfer-say-summary`: The assistant dials the destination, provides a summary of the call to the
            destination party, connects the customer, and leaves the call.
            - `warm-transfer-wait-for-operator-to-speak-first-and-then-say-message`: The assistant dials the destination,
            waits for the operator to speak, delivers the `message` to the destination party, and then connects the
            customer.
            - `warm-transfer-wait-for-operator-to-speak-first-and-then-say-summary`: The assistant dials the destination,
            waits for the operator to speak, provides a summary of the call to the destination party, and then connects the
            customer.
            - `warm-transfer-twiml`: The assistant dials the destination, executes the twiml instructions on the destination
            call leg, connects the customer, and leaves the call.

            @default 'blind-transfer'
        message (Union['CustomMessage', Unset, str]): This is the message the assistant will deliver to the destination
            party before connecting the customer.

            Usage:
            - Used only when `mode` is `blind-transfer-add-summary-to-sip-header`, `warm-transfer-say-message` or `warm-
            transfer-wait-for-operator-to-speak-first-and-then-say-message`.
        sip_verb (Union[Unset, TransferPlanSipVerb]): This specifies the SIP verb to use while transferring the call.
            - 'refer': Uses SIP REFER to transfer the call (default)
            - 'bye': Ends current call with SIP BYE
            - 'dial': Uses SIP DIAL to transfer the call
        twiml (Union[Unset, str]): This is the TwiML instructions to execute on the destination call leg before
            connecting the customer.

            Usage:
            - Used only when `mode` is `warm-transfer-twiml`.
            - Supports only `Play`, `Say`, `Gather`, `Hangup` and `Pause` verbs.
            - Maximum length is 4096 characters.

            Example:
            ```
            <Say voice="alice" language="en-US">Hello, transferring a customer to you.</Say>
            <Pause length="2"/>
            <Say>They called about billing questions.</Say>
            ```
        summary_plan (Union[Unset, SummaryPlan]):
    """

    mode: TransferPlanMode
    message: Union["CustomMessage", Unset, str] = UNSET
    sip_verb: Union[Unset, TransferPlanSipVerb] = UNSET
    twiml: Union[Unset, str] = UNSET
    summary_plan: Union[Unset, "SummaryPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_message import CustomMessage

        mode = self.mode.value

        message: Union[Unset, dict[str, Any], str]
        if isinstance(self.message, Unset):
            message = UNSET
        elif isinstance(self.message, CustomMessage):
            message = self.message.to_dict()
        else:
            message = self.message

        sip_verb: Union[Unset, str] = UNSET
        if not isinstance(self.sip_verb, Unset):
            sip_verb = self.sip_verb.value

        twiml = self.twiml

        summary_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summary_plan, Unset):
            summary_plan = self.summary_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if sip_verb is not UNSET:
            field_dict["sipVerb"] = sip_verb
        if twiml is not UNSET:
            field_dict["twiml"] = twiml
        if summary_plan is not UNSET:
            field_dict["summaryPlan"] = summary_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_message import CustomMessage
        from ..models.summary_plan import SummaryPlan

        d = dict(src_dict)
        mode = TransferPlanMode(d.pop("mode"))

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

        _sip_verb = d.pop("sipVerb", UNSET)
        sip_verb: Union[Unset, TransferPlanSipVerb]
        if isinstance(_sip_verb, Unset):
            sip_verb = UNSET
        else:
            sip_verb = TransferPlanSipVerb(_sip_verb)

        twiml = d.pop("twiml", UNSET)

        _summary_plan = d.pop("summaryPlan", UNSET)
        summary_plan: Union[Unset, SummaryPlan]
        if isinstance(_summary_plan, Unset):
            summary_plan = UNSET
        else:
            summary_plan = SummaryPlan.from_dict(_summary_plan)

        transfer_plan = cls(
            mode=mode,
            message=message,
            sip_verb=sip_verb,
            twiml=twiml,
            summary_plan=summary_plan,
        )

        transfer_plan.additional_properties = d
        return transfer_plan

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
