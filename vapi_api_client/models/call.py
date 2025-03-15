import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.call_ended_reason import CallEndedReason
from ..models.call_phone_call_provider import CallPhoneCallProvider
from ..models.call_phone_call_transport import CallPhoneCallTransport
from ..models.call_status import CallStatus
from ..models.call_type import CallType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analysis import Analysis
    from ..models.analysis_cost import AnalysisCost
    from ..models.artifact import Artifact
    from ..models.artifact_plan import ArtifactPlan
    from ..models.assistant_overrides import AssistantOverrides
    from ..models.bot_message import BotMessage
    from ..models.cost_breakdown import CostBreakdown
    from ..models.create_assistant_dto import CreateAssistantDTO
    from ..models.create_customer_dto import CreateCustomerDTO
    from ..models.create_squad_dto import CreateSquadDTO
    from ..models.import_twilio_phone_number_dto import ImportTwilioPhoneNumberDTO
    from ..models.model_cost import ModelCost
    from ..models.monitor import Monitor
    from ..models.system_message import SystemMessage
    from ..models.tool_call_message import ToolCallMessage
    from ..models.tool_call_result_message import ToolCallResultMessage
    from ..models.transcriber_cost import TranscriberCost
    from ..models.transfer_destination_number import TransferDestinationNumber
    from ..models.transfer_destination_sip import TransferDestinationSip
    from ..models.transport import Transport
    from ..models.transport_cost import TransportCost
    from ..models.user_message import UserMessage
    from ..models.vapi_cost import VapiCost
    from ..models.voice_cost import VoiceCost
    from ..models.voicemail_detection_cost import VoicemailDetectionCost


T = TypeVar("T", bound="Call")


@_attrs_define
class Call:
    """
    Attributes:
        id (str): This is the unique identifier for the call.
        org_id (str): This is the unique identifier for the org that this call belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the call was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the call was last updated.
        type_ (Union[Unset, CallType]): This is the type of call.
        costs (Union[Unset, list[Union['AnalysisCost', 'ModelCost', 'TranscriberCost', 'TransportCost', 'VapiCost',
            'VoiceCost', 'VoicemailDetectionCost']]]): These are the costs of individual components of the call in USD.
        messages (Union[Unset, list[Union['BotMessage', 'SystemMessage', 'ToolCallMessage', 'ToolCallResultMessage',
            'UserMessage']]]):
        phone_call_provider (Union[Unset, CallPhoneCallProvider]): This is the provider of the call.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
        phone_call_transport (Union[Unset, CallPhoneCallTransport]): This is the transport of the phone call.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
        status (Union[Unset, CallStatus]): This is the status of the call.
        ended_reason (Union[Unset, CallEndedReason]): This is the explanation for how the call ended.
        destination (Union['TransferDestinationNumber', 'TransferDestinationSip', Unset]): This is the destination where
            the call ended up being transferred to. If the call was not transferred, this will be empty.
        started_at (Union[Unset, datetime.datetime]): This is the ISO 8601 date-time string of when the call was
            started.
        ended_at (Union[Unset, datetime.datetime]): This is the ISO 8601 date-time string of when the call was ended.
        cost (Union[Unset, float]): This is the cost of the call in USD.
        cost_breakdown (Union[Unset, CostBreakdown]):
        artifact_plan (Union[Unset, ArtifactPlan]):
        analysis (Union[Unset, Analysis]):
        monitor (Union[Unset, Monitor]):
        artifact (Union[Unset, Artifact]):
        transport (Union[Unset, Transport]):
        phone_call_provider_id (Union[Unset, str]): The ID of the call as provided by the phone number service. callSid
            in Twilio. conversationUuid in Vonage. callControlId in Telnyx.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
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
        name (Union[Unset, str]): This is the name of the call. This is just for your own reference.
    """

    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    type_: Union[Unset, CallType] = UNSET
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
    messages: Union[
        Unset, list[Union["BotMessage", "SystemMessage", "ToolCallMessage", "ToolCallResultMessage", "UserMessage"]]
    ] = UNSET
    phone_call_provider: Union[Unset, CallPhoneCallProvider] = UNSET
    phone_call_transport: Union[Unset, CallPhoneCallTransport] = UNSET
    status: Union[Unset, CallStatus] = UNSET
    ended_reason: Union[Unset, CallEndedReason] = UNSET
    destination: Union["TransferDestinationNumber", "TransferDestinationSip", Unset] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    ended_at: Union[Unset, datetime.datetime] = UNSET
    cost: Union[Unset, float] = UNSET
    cost_breakdown: Union[Unset, "CostBreakdown"] = UNSET
    artifact_plan: Union[Unset, "ArtifactPlan"] = UNSET
    analysis: Union[Unset, "Analysis"] = UNSET
    monitor: Union[Unset, "Monitor"] = UNSET
    artifact: Union[Unset, "Artifact"] = UNSET
    transport: Union[Unset, "Transport"] = UNSET
    phone_call_provider_id: Union[Unset, str] = UNSET
    assistant_id: Union[Unset, str] = UNSET
    assistant: Union[Unset, "CreateAssistantDTO"] = UNSET
    assistant_overrides: Union[Unset, "AssistantOverrides"] = UNSET
    squad_id: Union[Unset, str] = UNSET
    squad: Union[Unset, "CreateSquadDTO"] = UNSET
    phone_number_id: Union[Unset, str] = UNSET
    phone_number: Union[Unset, "ImportTwilioPhoneNumberDTO"] = UNSET
    customer_id: Union[Unset, str] = UNSET
    customer: Union[Unset, "CreateCustomerDTO"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_message import BotMessage
        from ..models.model_cost import ModelCost
        from ..models.system_message import SystemMessage
        from ..models.tool_call_message import ToolCallMessage
        from ..models.transcriber_cost import TranscriberCost
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transport_cost import TransportCost
        from ..models.user_message import UserMessage
        from ..models.vapi_cost import VapiCost
        from ..models.voice_cost import VoiceCost
        from ..models.voicemail_detection_cost import VoicemailDetectionCost

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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

        messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item: dict[str, Any]
                if isinstance(messages_item_data, UserMessage):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, SystemMessage):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, BotMessage):
                    messages_item = messages_item_data.to_dict()
                elif isinstance(messages_item_data, ToolCallMessage):
                    messages_item = messages_item_data.to_dict()
                else:
                    messages_item = messages_item_data.to_dict()

                messages.append(messages_item)

        phone_call_provider: Union[Unset, str] = UNSET
        if not isinstance(self.phone_call_provider, Unset):
            phone_call_provider = self.phone_call_provider.value

        phone_call_transport: Union[Unset, str] = UNSET
        if not isinstance(self.phone_call_transport, Unset):
            phone_call_transport = self.phone_call_transport.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        ended_reason: Union[Unset, str] = UNSET
        if not isinstance(self.ended_reason, Unset):
            ended_reason = self.ended_reason.value

        destination: Union[Unset, dict[str, Any]]
        if isinstance(self.destination, Unset):
            destination = UNSET
        elif isinstance(self.destination, TransferDestinationNumber):
            destination = self.destination.to_dict()
        else:
            destination = self.destination.to_dict()

        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        ended_at: Union[Unset, str] = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat()

        cost = self.cost

        cost_breakdown: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cost_breakdown, Unset):
            cost_breakdown = self.cost_breakdown.to_dict()

        artifact_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artifact_plan, Unset):
            artifact_plan = self.artifact_plan.to_dict()

        analysis: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.analysis, Unset):
            analysis = self.analysis.to_dict()

        monitor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor.to_dict()

        artifact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artifact, Unset):
            artifact = self.artifact.to_dict()

        transport: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transport, Unset):
            transport = self.transport.to_dict()

        phone_call_provider_id = self.phone_call_provider_id

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

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if costs is not UNSET:
            field_dict["costs"] = costs
        if messages is not UNSET:
            field_dict["messages"] = messages
        if phone_call_provider is not UNSET:
            field_dict["phoneCallProvider"] = phone_call_provider
        if phone_call_transport is not UNSET:
            field_dict["phoneCallTransport"] = phone_call_transport
        if status is not UNSET:
            field_dict["status"] = status
        if ended_reason is not UNSET:
            field_dict["endedReason"] = ended_reason
        if destination is not UNSET:
            field_dict["destination"] = destination
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if cost is not UNSET:
            field_dict["cost"] = cost
        if cost_breakdown is not UNSET:
            field_dict["costBreakdown"] = cost_breakdown
        if artifact_plan is not UNSET:
            field_dict["artifactPlan"] = artifact_plan
        if analysis is not UNSET:
            field_dict["analysis"] = analysis
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if artifact is not UNSET:
            field_dict["artifact"] = artifact
        if transport is not UNSET:
            field_dict["transport"] = transport
        if phone_call_provider_id is not UNSET:
            field_dict["phoneCallProviderId"] = phone_call_provider_id
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
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.analysis import Analysis
        from ..models.analysis_cost import AnalysisCost
        from ..models.artifact import Artifact
        from ..models.artifact_plan import ArtifactPlan
        from ..models.assistant_overrides import AssistantOverrides
        from ..models.bot_message import BotMessage
        from ..models.cost_breakdown import CostBreakdown
        from ..models.create_assistant_dto import CreateAssistantDTO
        from ..models.create_customer_dto import CreateCustomerDTO
        from ..models.create_squad_dto import CreateSquadDTO
        from ..models.import_twilio_phone_number_dto import ImportTwilioPhoneNumberDTO
        from ..models.model_cost import ModelCost
        from ..models.monitor import Monitor
        from ..models.system_message import SystemMessage
        from ..models.tool_call_message import ToolCallMessage
        from ..models.tool_call_result_message import ToolCallResultMessage
        from ..models.transcriber_cost import TranscriberCost
        from ..models.transfer_destination_number import TransferDestinationNumber
        from ..models.transfer_destination_sip import TransferDestinationSip
        from ..models.transport import Transport
        from ..models.transport_cost import TransportCost
        from ..models.user_message import UserMessage
        from ..models.vapi_cost import VapiCost
        from ..models.voice_cost import VoiceCost
        from ..models.voicemail_detection_cost import VoicemailDetectionCost

        d = src_dict.copy()
        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CallType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CallType(_type_)

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

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:

            def _parse_messages_item(
                data: object,
            ) -> Union["BotMessage", "SystemMessage", "ToolCallMessage", "ToolCallResultMessage", "UserMessage"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_0 = UserMessage.from_dict(data)

                    return messages_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_1 = SystemMessage.from_dict(data)

                    return messages_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_2 = BotMessage.from_dict(data)

                    return messages_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    messages_item_type_3 = ToolCallMessage.from_dict(data)

                    return messages_item_type_3
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                messages_item_type_4 = ToolCallResultMessage.from_dict(data)

                return messages_item_type_4

            messages_item = _parse_messages_item(messages_item_data)

            messages.append(messages_item)

        _phone_call_provider = d.pop("phoneCallProvider", UNSET)
        phone_call_provider: Union[Unset, CallPhoneCallProvider]
        if isinstance(_phone_call_provider, Unset):
            phone_call_provider = UNSET
        else:
            phone_call_provider = CallPhoneCallProvider(_phone_call_provider)

        _phone_call_transport = d.pop("phoneCallTransport", UNSET)
        phone_call_transport: Union[Unset, CallPhoneCallTransport]
        if isinstance(_phone_call_transport, Unset):
            phone_call_transport = UNSET
        else:
            phone_call_transport = CallPhoneCallTransport(_phone_call_transport)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CallStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CallStatus(_status)

        _ended_reason = d.pop("endedReason", UNSET)
        ended_reason: Union[Unset, CallEndedReason]
        if isinstance(_ended_reason, Unset):
            ended_reason = UNSET
        else:
            ended_reason = CallEndedReason(_ended_reason)

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

        cost = d.pop("cost", UNSET)

        _cost_breakdown = d.pop("costBreakdown", UNSET)
        cost_breakdown: Union[Unset, CostBreakdown]
        if isinstance(_cost_breakdown, Unset):
            cost_breakdown = UNSET
        else:
            cost_breakdown = CostBreakdown.from_dict(_cost_breakdown)

        _artifact_plan = d.pop("artifactPlan", UNSET)
        artifact_plan: Union[Unset, ArtifactPlan]
        if isinstance(_artifact_plan, Unset):
            artifact_plan = UNSET
        else:
            artifact_plan = ArtifactPlan.from_dict(_artifact_plan)

        _analysis = d.pop("analysis", UNSET)
        analysis: Union[Unset, Analysis]
        if isinstance(_analysis, Unset):
            analysis = UNSET
        else:
            analysis = Analysis.from_dict(_analysis)

        _monitor = d.pop("monitor", UNSET)
        monitor: Union[Unset, Monitor]
        if isinstance(_monitor, Unset):
            monitor = UNSET
        else:
            monitor = Monitor.from_dict(_monitor)

        _artifact = d.pop("artifact", UNSET)
        artifact: Union[Unset, Artifact]
        if isinstance(_artifact, Unset):
            artifact = UNSET
        else:
            artifact = Artifact.from_dict(_artifact)

        _transport = d.pop("transport", UNSET)
        transport: Union[Unset, Transport]
        if isinstance(_transport, Unset):
            transport = UNSET
        else:
            transport = Transport.from_dict(_transport)

        phone_call_provider_id = d.pop("phoneCallProviderId", UNSET)

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

        name = d.pop("name", UNSET)

        call = cls(
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            type_=type_,
            costs=costs,
            messages=messages,
            phone_call_provider=phone_call_provider,
            phone_call_transport=phone_call_transport,
            status=status,
            ended_reason=ended_reason,
            destination=destination,
            started_at=started_at,
            ended_at=ended_at,
            cost=cost,
            cost_breakdown=cost_breakdown,
            artifact_plan=artifact_plan,
            analysis=analysis,
            monitor=monitor,
            artifact=artifact,
            transport=transport,
            phone_call_provider_id=phone_call_provider_id,
            assistant_id=assistant_id,
            assistant=assistant,
            assistant_overrides=assistant_overrides,
            squad_id=squad_id,
            squad=squad,
            phone_number_id=phone_number_id,
            phone_number=phone_number,
            customer_id=customer_id,
            customer=customer,
            name=name,
        )

        call.additional_properties = d
        return call

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
