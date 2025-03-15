import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.server_message_end_of_call_report_ended_reason import ServerMessageEndOfCallReportEndedReason
from ..models.server_message_end_of_call_report_type import ServerMessageEndOfCallReportType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis import Analysis
    from ..models.analysis_cost import AnalysisCost
    from ..models.artifact import Artifact
    from ..models.call import Call
    from ..models.create_assistant_dto import CreateAssistantDTO
    from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
    from ..models.create_customer_dto import CreateCustomerDTO
    from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
    from ..models.create_vapi_phone_number_dto import CreateVapiPhoneNumberDTO
    from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
    from ..models.model_cost import ModelCost
    from ..models.transcriber_cost import TranscriberCost
    from ..models.transport_cost import TransportCost
    from ..models.vapi_cost import VapiCost
    from ..models.voice_cost import VoiceCost
    from ..models.voicemail_detection_cost import VoicemailDetectionCost


T = TypeVar("T", bound="ServerMessageEndOfCallReport")


@_attrs_define
class ServerMessageEndOfCallReport:
    """
    Attributes:
        type_ (ServerMessageEndOfCallReportType): This is the type of the message. "end-of-call-report" is sent when the
            call ends and post-processing is complete.
        ended_reason (ServerMessageEndOfCallReportEndedReason): This is the reason the call ended. This can also be
            found at `call.endedReason` on GET /call/:id.
        artifact (Artifact):
        analysis (Analysis):
        phone_number (Union['CreateByoPhoneNumberDTO', 'CreateTwilioPhoneNumberDTO', 'CreateVapiPhoneNumberDTO',
            'CreateVonagePhoneNumberDTO', Unset]): This is the phone number associated with the call.

            This matches one of the following:
            - `call.phoneNumber`,
            - `call.phoneNumberId`.
        cost (Union[Unset, float]): This is the cost of the call in USD. This can also be found at `call.cost` on GET
            /call/:id.
        costs (Union[Unset, list[Union['AnalysisCost', 'ModelCost', 'TranscriberCost', 'TransportCost', 'VapiCost',
            'VoiceCost', 'VoicemailDetectionCost']]]): These are the costs of individual components of the call in USD. This
            can also be found at `call.costs` on GET /call/:id.
        timestamp (Union[Unset, str]): This is the ISO-8601 formatted timestamp of when the message was sent.
        assistant (Union[Unset, CreateAssistantDTO]):
        customer (Union[Unset, CreateCustomerDTO]):
        call (Union[Unset, Call]):
        started_at (Union[Unset, datetime.datetime]): This is the ISO 8601 date-time string of when the call started.
            This can also be found at `call.startedAt` on GET /call/:id.
        ended_at (Union[Unset, datetime.datetime]): This is the ISO 8601 date-time string of when the call ended. This
            can also be found at `call.endedAt` on GET /call/:id.
    """

    type_: ServerMessageEndOfCallReportType
    ended_reason: ServerMessageEndOfCallReportEndedReason
    artifact: "Artifact"
    analysis: "Analysis"
    phone_number: Union[
        "CreateByoPhoneNumberDTO",
        "CreateTwilioPhoneNumberDTO",
        "CreateVapiPhoneNumberDTO",
        "CreateVonagePhoneNumberDTO",
        Unset,
    ] = UNSET
    cost: Union[Unset, float] = UNSET
    costs: Union[
        Unset,
        list[
            Union[
                "AnalysisCost",
                "ModelCost",
                "TranscriberCost",
                "TransportCost",
                "VapiCost",
                "VoiceCost",
                "VoicemailDetectionCost",
            ]
        ],
    ] = UNSET
    timestamp: Union[Unset, str] = UNSET
    assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    customer: Union[Unset, "CreateCustomerDTO"] = UNSET
    call: Union[Unset, "Call"] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    ended_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
        from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
        from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
        from ..models.model_cost import ModelCost
        from ..models.transcriber_cost import TranscriberCost
        from ..models.transport_cost import TransportCost
        from ..models.vapi_cost import VapiCost
        from ..models.voice_cost import VoiceCost
        from ..models.voicemail_detection_cost import VoicemailDetectionCost

        type_ = self.type_.value

        ended_reason = self.ended_reason.value

        artifact = self.artifact.to_dict()

        analysis = self.analysis.to_dict()

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

        cost = self.cost

        costs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.costs, Unset):
            costs = []
            for costs_item_data in self.costs:
                costs_item: dict[str, Any]
                if isinstance(costs_item_data, TransportCost):
                    costs_item = costs_item_data.to_dict()
                elif isinstance(costs_item_data, TranscriberCost):
                    costs_item = costs_item_data.to_dict()
                elif isinstance(costs_item_data, ModelCost):
                    costs_item = costs_item_data.to_dict()
                elif isinstance(costs_item_data, VoiceCost):
                    costs_item = costs_item_data.to_dict()
                elif isinstance(costs_item_data, VapiCost):
                    costs_item = costs_item_data.to_dict()
                elif isinstance(costs_item_data, VoicemailDetectionCost):
                    costs_item = costs_item_data.to_dict()
                else:
                    costs_item = costs_item_data.to_dict()

                costs.append(costs_item)

        timestamp = self.timestamp

        assistant: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assistant, Unset):
            assistant = self.assistant.to_dict()

        customer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customer, Unset):
            customer = self.customer.to_dict()

        call: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.call, Unset):
            call = self.call.to_dict()

        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        ended_at: Union[Unset, str] = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "endedReason": ended_reason,
                "artifact": artifact,
                "analysis": analysis,
            }
        )
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if cost is not UNSET:
            field_dict["cost"] = cost
        if costs is not UNSET:
            field_dict["costs"] = costs
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if assistant is not UNSET:
            field_dict["assistant"] = assistant
        if customer is not UNSET:
            field_dict["customer"] = customer
        if call is not UNSET:
            field_dict["call"] = call
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.analysis import Analysis
        from ..models.analysis_cost import AnalysisCost
        from ..models.artifact import Artifact
        from ..models.call import Call
        from ..models.create_assistant_dto import CreateAssistantDTO
        from ..models.create_byo_phone_number_dto import CreateByoPhoneNumberDTO
        from ..models.create_customer_dto import CreateCustomerDTO
        from ..models.create_twilio_phone_number_dto import CreateTwilioPhoneNumberDTO
        from ..models.create_vapi_phone_number_dto import CreateVapiPhoneNumberDTO
        from ..models.create_vonage_phone_number_dto import CreateVonagePhoneNumberDTO
        from ..models.model_cost import ModelCost
        from ..models.transcriber_cost import TranscriberCost
        from ..models.transport_cost import TransportCost
        from ..models.vapi_cost import VapiCost
        from ..models.voice_cost import VoiceCost
        from ..models.voicemail_detection_cost import VoicemailDetectionCost

        d = src_dict.copy()
        type_ = ServerMessageEndOfCallReportType(d.pop("type"))

        ended_reason = ServerMessageEndOfCallReportEndedReason(d.pop("endedReason"))

        artifact = Artifact.from_dict(d.pop("artifact"))

        analysis = Analysis.from_dict(d.pop("analysis"))

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

        cost = d.pop("cost", UNSET)

        costs = []
        _costs = d.pop("costs", UNSET)
        for costs_item_data in _costs or []:

            def _parse_costs_item(
                data: object,
            ) -> Union[
                "AnalysisCost",
                "ModelCost",
                "TranscriberCost",
                "TransportCost",
                "VapiCost",
                "VoiceCost",
                "VoicemailDetectionCost",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    costs_item_type_0 = TransportCost.from_dict(data)

                    return costs_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    costs_item_type_1 = TranscriberCost.from_dict(data)

                    return costs_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    costs_item_type_2 = ModelCost.from_dict(data)

                    return costs_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    costs_item_type_3 = VoiceCost.from_dict(data)

                    return costs_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    costs_item_type_4 = VapiCost.from_dict(data)

                    return costs_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    costs_item_type_5 = VoicemailDetectionCost.from_dict(data)

                    return costs_item_type_5
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                costs_item_type_6 = AnalysisCost.from_dict(data)

                return costs_item_type_6

            costs_item = _parse_costs_item(costs_item_data)

            costs.append(costs_item)

        timestamp = d.pop("timestamp", UNSET)

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

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _ended_at = d.pop("endedAt", UNSET)
        ended_at: Union[Unset, datetime.datetime]
        if isinstance(_ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = isoparse(_ended_at)

        server_message_end_of_call_report = cls(
            type_=type_,
            ended_reason=ended_reason,
            artifact=artifact,
            analysis=analysis,
            phone_number=phone_number,
            cost=cost,
            costs=costs,
            timestamp=timestamp,
            assistant=assistant,
            customer=customer,
            call=call,
            started_at=started_at,
            ended_at=ended_at,
        )

        server_message_end_of_call_report.additional_properties = d
        return server_message_end_of_call_report

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
