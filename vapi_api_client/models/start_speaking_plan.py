from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.start_speaking_plan_smart_endpointing_enabled_type_1 import StartSpeakingPlanSmartEndpointingEnabledType1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_custom_endpointing_rule import AssistantCustomEndpointingRule
    from ..models.both_custom_endpointing_rule import BothCustomEndpointingRule
    from ..models.customer_custom_endpointing_rule import CustomerCustomEndpointingRule
    from ..models.transcription_endpointing_plan import TranscriptionEndpointingPlan


T = TypeVar("T", bound="StartSpeakingPlan")


@_attrs_define
class StartSpeakingPlan:
    """
    Attributes:
        wait_seconds (Union[Unset, float]): This is how long assistant waits before speaking. Defaults to 0.4.

            This is the minimum it will wait but if there is latency is the pipeline, this minimum will be exceeded. This is
            intended as a stopgap in case the pipeline is moving too fast.

            Example:
            - If model generates tokens and voice generates bytes within 100ms, the pipeline still waits 300ms before
            outputting speech.

            Usage:
            - If the customer is taking long pauses, set this to a higher value.
            - If the assistant is accidentally jumping in too much, set this to a higher value.

            @default 0.4 Example: 0.4.
        smart_endpointing_enabled (Union[StartSpeakingPlanSmartEndpointingEnabledType1, Unset, bool]): This determines
            if a customer speech is considered done (endpointing) using a Vapi custom-trained model on customer's speech.
            This is good for middle-of-thought detection. Alternatively, you can use LiveKit's smart endpointing model (it
            only supports English, though)

            Once an endpoint is triggered, the request is sent to `assistant.model`.

            Usage:
            - If your conversations are long-form and you want assistant to wait smartly even if customer pauses for a bit
            to think, you can use this instead.

            This overrides `transcriptionEndpointingPlan`.

            @default false
        custom_endpointing_rules (Union[Unset, list[Union['AssistantCustomEndpointingRule', 'BothCustomEndpointingRule',
            'CustomerCustomEndpointingRule']]]): These are the custom endpointing rules to set an endpointing timeout based
            on a regex on the customer's speech or the assistant's last message.

            Usage:
            - If you have yes/no questions like "are you interested in a loan?", you can set a shorter timeout.
            - If you have questions where the customer may pause to look up information like "what's my account number?",
            you can set a longer timeout.
            - If you want to wait longer while customer is enumerating a list of numbers, you can set a longer timeout.

            These override `transcriptionEndpointingPlan` and `smartEndpointingEnabled` when a rule is matched.

            The rules are evaluated in order and the first one that matches will be used.

            @default []
        transcription_endpointing_plan (Union[Unset, TranscriptionEndpointingPlan]):
    """

    wait_seconds: Union[Unset, float] = UNSET
    smart_endpointing_enabled: Union[StartSpeakingPlanSmartEndpointingEnabledType1, Unset, bool] = UNSET
    custom_endpointing_rules: Union[
        Unset,
        list[Union["AssistantCustomEndpointingRule", "BothCustomEndpointingRule", "CustomerCustomEndpointingRule"]],
    ] = UNSET
    transcription_endpointing_plan: Union[Unset, "TranscriptionEndpointingPlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assistant_custom_endpointing_rule import AssistantCustomEndpointingRule
        from ..models.customer_custom_endpointing_rule import CustomerCustomEndpointingRule

        wait_seconds = self.wait_seconds

        smart_endpointing_enabled: Union[Unset, bool, str]
        if isinstance(self.smart_endpointing_enabled, Unset):
            smart_endpointing_enabled = UNSET
        elif isinstance(self.smart_endpointing_enabled, StartSpeakingPlanSmartEndpointingEnabledType1):
            smart_endpointing_enabled = self.smart_endpointing_enabled.value
        else:
            smart_endpointing_enabled = self.smart_endpointing_enabled

        custom_endpointing_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_endpointing_rules, Unset):
            custom_endpointing_rules = []
            for custom_endpointing_rules_item_data in self.custom_endpointing_rules:
                custom_endpointing_rules_item: dict[str, Any]
                if isinstance(custom_endpointing_rules_item_data, AssistantCustomEndpointingRule):
                    custom_endpointing_rules_item = custom_endpointing_rules_item_data.to_dict()
                elif isinstance(custom_endpointing_rules_item_data, CustomerCustomEndpointingRule):
                    custom_endpointing_rules_item = custom_endpointing_rules_item_data.to_dict()
                else:
                    custom_endpointing_rules_item = custom_endpointing_rules_item_data.to_dict()

                custom_endpointing_rules.append(custom_endpointing_rules_item)

        transcription_endpointing_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.transcription_endpointing_plan, Unset):
            transcription_endpointing_plan = self.transcription_endpointing_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wait_seconds is not UNSET:
            field_dict["waitSeconds"] = wait_seconds
        if smart_endpointing_enabled is not UNSET:
            field_dict["smartEndpointingEnabled"] = smart_endpointing_enabled
        if custom_endpointing_rules is not UNSET:
            field_dict["customEndpointingRules"] = custom_endpointing_rules
        if transcription_endpointing_plan is not UNSET:
            field_dict["transcriptionEndpointingPlan"] = transcription_endpointing_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assistant_custom_endpointing_rule import AssistantCustomEndpointingRule
        from ..models.both_custom_endpointing_rule import BothCustomEndpointingRule
        from ..models.customer_custom_endpointing_rule import CustomerCustomEndpointingRule
        from ..models.transcription_endpointing_plan import TranscriptionEndpointingPlan

        d = dict(src_dict)
        wait_seconds = d.pop("waitSeconds", UNSET)

        def _parse_smart_endpointing_enabled(
            data: object,
        ) -> Union[StartSpeakingPlanSmartEndpointingEnabledType1, Unset, bool]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                smart_endpointing_enabled_type_1 = StartSpeakingPlanSmartEndpointingEnabledType1(data)

                return smart_endpointing_enabled_type_1
            except:  # noqa: E722
                pass
            return cast(Union[StartSpeakingPlanSmartEndpointingEnabledType1, Unset, bool], data)

        smart_endpointing_enabled = _parse_smart_endpointing_enabled(d.pop("smartEndpointingEnabled", UNSET))

        custom_endpointing_rules = []
        _custom_endpointing_rules = d.pop("customEndpointingRules", UNSET)
        for custom_endpointing_rules_item_data in _custom_endpointing_rules or []:

            def _parse_custom_endpointing_rules_item(
                data: object,
            ) -> Union["AssistantCustomEndpointingRule", "BothCustomEndpointingRule", "CustomerCustomEndpointingRule"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    custom_endpointing_rules_item_type_0 = AssistantCustomEndpointingRule.from_dict(data)

                    return custom_endpointing_rules_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    custom_endpointing_rules_item_type_1 = CustomerCustomEndpointingRule.from_dict(data)

                    return custom_endpointing_rules_item_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                custom_endpointing_rules_item_type_2 = BothCustomEndpointingRule.from_dict(data)

                return custom_endpointing_rules_item_type_2

            custom_endpointing_rules_item = _parse_custom_endpointing_rules_item(custom_endpointing_rules_item_data)

            custom_endpointing_rules.append(custom_endpointing_rules_item)

        _transcription_endpointing_plan = d.pop("transcriptionEndpointingPlan", UNSET)
        transcription_endpointing_plan: Union[Unset, TranscriptionEndpointingPlan]
        if isinstance(_transcription_endpointing_plan, Unset):
            transcription_endpointing_plan = UNSET
        else:
            transcription_endpointing_plan = TranscriptionEndpointingPlan.from_dict(_transcription_endpointing_plan)

        start_speaking_plan = cls(
            wait_seconds=wait_seconds,
            smart_endpointing_enabled=smart_endpointing_enabled,
            custom_endpointing_rules=custom_endpointing_rules,
            transcription_endpointing_plan=transcription_endpointing_plan,
        )

        start_speaking_plan.additional_properties = d
        return start_speaking_plan

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
