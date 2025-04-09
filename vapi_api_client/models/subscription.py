import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.subscription_status import SubscriptionStatus
from ..models.subscription_type import SubscriptionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_reload_plan import AutoReloadPlan
    from ..models.invoice_plan import InvoicePlan


T = TypeVar("T", bound="Subscription")


@_attrs_define
class Subscription:
    """
    Attributes:
        id (str): This is the unique identifier for the subscription.
        created_at (datetime.datetime): This is the timestamp when the subscription was created.
        updated_at (datetime.datetime): This is the timestamp when the subscription was last updated.
        type_ (SubscriptionType): This is the type / tier of the subscription.
        status (SubscriptionStatus): This is the status of the subscription. Past due subscriptions are subscriptions
            with past due payments.
        credits_ (str): This is the number of credits the subscription currently has.

            Note: This is a string to avoid floating point precision issues.
        concurrency_counter (float): This is the total number of active calls (concurrency) across all orgs under this
            subscription.
        concurrency_limit_included (float): This is the default concurrency limit for the subscription.
        concurrency_limit_purchased (float): This is the purchased add-on concurrency limit for the subscription.
        phone_numbers_counter (Union[Unset, float]): This is the number of free phone numbers the subscription has
        phone_numbers_included (Union[Unset, float]): This is the maximum number of free phone numbers the subscription
            can have
        monthly_charge_schedule_id (Union[Unset, float]): This is the ID of the monthly job that charges for
            subscription add ons and phone numbers.
        monthly_credit_check_schedule_id (Union[Unset, float]): This is the ID of the monthly job that checks whether
            the credit balance of the subscription
            is sufficient for the monthly charge.
        stripe_customer_id (Union[Unset, str]): This is the Stripe customer ID.
        stripe_payment_method_id (Union[Unset, str]): This is the Stripe payment ID.
        slack_support_enabled (Union[Unset, bool]): If this flag is true, then the user has purchased slack support.
        slack_channel_id (Union[Unset, str]): If this subscription has a slack support subscription, the slack channel's
            ID will be stored here.
        hipaa_enabled (Union[Unset, bool]): This is the HIPAA enabled flag for the subscription. It determines whether
            orgs under this
            subscription have the option to enable HIPAA compliance.
        hipaa_common_paper_agreement_id (Union[Unset, str]): This is the ID for the Common Paper agreement outlining the
            HIPAA contract.
        stripe_payment_method_fingerprint (Union[Unset, str]): This is the Stripe fingerprint of the payment method
            (card). It allows us
            to detect users who try to abuse our system through multiple sign-ups.
        stripe_customer_email (Union[Unset, str]): This is the customer's email on Stripe.
        referred_by_email (Union[Unset, str]): This is the email of the referrer for the subscription.
        auto_reload_plan (Union[Unset, AutoReloadPlan]):
        minutes_included (Union[Unset, float]): The number of minutes included in the subscription.
        minutes_used (Union[Unset, float]): The number of minutes used in the subscription.
        minutes_used_next_reset_at (Union[Unset, datetime.datetime]): This is the timestamp at which the number of
            monthly free minutes is scheduled to reset at.
        minutes_overage_cost (Union[Unset, float]): The per minute charge on minutes that exceed the included minutes.
            Enterprise only.
        providers_included (Union[Unset, list[str]]): The list of providers included in the subscription. Enterprise
            only.
        outbound_calls_daily_limit (Union[Unset, float]): The maximum number of outbound calls this subscription may
            make in a day. Resets every night.
        outbound_calls_counter (Union[Unset, float]): The current number of outbound calls the subscription has made in
            the current day.
        outbound_calls_counter_next_reset_at (Union[Unset, datetime.datetime]): This is the timestamp at which the
            outbound calls counter is scheduled to reset at.
        coupon_ids (Union[Unset, list[str]]): This is the IDs of the coupons applicable to this subscription.
        coupon_usage_left (Union[Unset, str]): This is the number of credits left obtained from a coupon.
        invoice_plan (Union[Unset, InvoicePlan]):
    """

    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    type_: SubscriptionType
    status: SubscriptionStatus
    credits_: str
    concurrency_counter: float
    concurrency_limit_included: float
    concurrency_limit_purchased: float
    phone_numbers_counter: Union[Unset, float] = UNSET
    phone_numbers_included: Union[Unset, float] = UNSET
    monthly_charge_schedule_id: Union[Unset, float] = UNSET
    monthly_credit_check_schedule_id: Union[Unset, float] = UNSET
    stripe_customer_id: Union[Unset, str] = UNSET
    stripe_payment_method_id: Union[Unset, str] = UNSET
    slack_support_enabled: Union[Unset, bool] = UNSET
    slack_channel_id: Union[Unset, str] = UNSET
    hipaa_enabled: Union[Unset, bool] = UNSET
    hipaa_common_paper_agreement_id: Union[Unset, str] = UNSET
    stripe_payment_method_fingerprint: Union[Unset, str] = UNSET
    stripe_customer_email: Union[Unset, str] = UNSET
    referred_by_email: Union[Unset, str] = UNSET
    auto_reload_plan: Union[Unset, "AutoReloadPlan"] = UNSET
    minutes_included: Union[Unset, float] = UNSET
    minutes_used: Union[Unset, float] = UNSET
    minutes_used_next_reset_at: Union[Unset, datetime.datetime] = UNSET
    minutes_overage_cost: Union[Unset, float] = UNSET
    providers_included: Union[Unset, list[str]] = UNSET
    outbound_calls_daily_limit: Union[Unset, float] = UNSET
    outbound_calls_counter: Union[Unset, float] = UNSET
    outbound_calls_counter_next_reset_at: Union[Unset, datetime.datetime] = UNSET
    coupon_ids: Union[Unset, list[str]] = UNSET
    coupon_usage_left: Union[Unset, str] = UNSET
    invoice_plan: Union[Unset, "InvoicePlan"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        type_ = self.type_.value

        status = self.status.value

        credits_ = self.credits_

        concurrency_counter = self.concurrency_counter

        concurrency_limit_included = self.concurrency_limit_included

        concurrency_limit_purchased = self.concurrency_limit_purchased

        phone_numbers_counter = self.phone_numbers_counter

        phone_numbers_included = self.phone_numbers_included

        monthly_charge_schedule_id = self.monthly_charge_schedule_id

        monthly_credit_check_schedule_id = self.monthly_credit_check_schedule_id

        stripe_customer_id = self.stripe_customer_id

        stripe_payment_method_id = self.stripe_payment_method_id

        slack_support_enabled = self.slack_support_enabled

        slack_channel_id = self.slack_channel_id

        hipaa_enabled = self.hipaa_enabled

        hipaa_common_paper_agreement_id = self.hipaa_common_paper_agreement_id

        stripe_payment_method_fingerprint = self.stripe_payment_method_fingerprint

        stripe_customer_email = self.stripe_customer_email

        referred_by_email = self.referred_by_email

        auto_reload_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auto_reload_plan, Unset):
            auto_reload_plan = self.auto_reload_plan.to_dict()

        minutes_included = self.minutes_included

        minutes_used = self.minutes_used

        minutes_used_next_reset_at: Union[Unset, str] = UNSET
        if not isinstance(self.minutes_used_next_reset_at, Unset):
            minutes_used_next_reset_at = self.minutes_used_next_reset_at.isoformat()

        minutes_overage_cost = self.minutes_overage_cost

        providers_included: Union[Unset, list[str]] = UNSET
        if not isinstance(self.providers_included, Unset):
            providers_included = self.providers_included

        outbound_calls_daily_limit = self.outbound_calls_daily_limit

        outbound_calls_counter = self.outbound_calls_counter

        outbound_calls_counter_next_reset_at: Union[Unset, str] = UNSET
        if not isinstance(self.outbound_calls_counter_next_reset_at, Unset):
            outbound_calls_counter_next_reset_at = self.outbound_calls_counter_next_reset_at.isoformat()

        coupon_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.coupon_ids, Unset):
            coupon_ids = self.coupon_ids

        coupon_usage_left = self.coupon_usage_left

        invoice_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.invoice_plan, Unset):
            invoice_plan = self.invoice_plan.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "type": type_,
                "status": status,
                "credits": credits_,
                "concurrencyCounter": concurrency_counter,
                "concurrencyLimitIncluded": concurrency_limit_included,
                "concurrencyLimitPurchased": concurrency_limit_purchased,
            }
        )
        if phone_numbers_counter is not UNSET:
            field_dict["phoneNumbersCounter"] = phone_numbers_counter
        if phone_numbers_included is not UNSET:
            field_dict["phoneNumbersIncluded"] = phone_numbers_included
        if monthly_charge_schedule_id is not UNSET:
            field_dict["monthlyChargeScheduleId"] = monthly_charge_schedule_id
        if monthly_credit_check_schedule_id is not UNSET:
            field_dict["monthlyCreditCheckScheduleId"] = monthly_credit_check_schedule_id
        if stripe_customer_id is not UNSET:
            field_dict["stripeCustomerId"] = stripe_customer_id
        if stripe_payment_method_id is not UNSET:
            field_dict["stripePaymentMethodId"] = stripe_payment_method_id
        if slack_support_enabled is not UNSET:
            field_dict["slackSupportEnabled"] = slack_support_enabled
        if slack_channel_id is not UNSET:
            field_dict["slackChannelId"] = slack_channel_id
        if hipaa_enabled is not UNSET:
            field_dict["hipaaEnabled"] = hipaa_enabled
        if hipaa_common_paper_agreement_id is not UNSET:
            field_dict["hipaaCommonPaperAgreementId"] = hipaa_common_paper_agreement_id
        if stripe_payment_method_fingerprint is not UNSET:
            field_dict["stripePaymentMethodFingerprint"] = stripe_payment_method_fingerprint
        if stripe_customer_email is not UNSET:
            field_dict["stripeCustomerEmail"] = stripe_customer_email
        if referred_by_email is not UNSET:
            field_dict["referredByEmail"] = referred_by_email
        if auto_reload_plan is not UNSET:
            field_dict["autoReloadPlan"] = auto_reload_plan
        if minutes_included is not UNSET:
            field_dict["minutesIncluded"] = minutes_included
        if minutes_used is not UNSET:
            field_dict["minutesUsed"] = minutes_used
        if minutes_used_next_reset_at is not UNSET:
            field_dict["minutesUsedNextResetAt"] = minutes_used_next_reset_at
        if minutes_overage_cost is not UNSET:
            field_dict["minutesOverageCost"] = minutes_overage_cost
        if providers_included is not UNSET:
            field_dict["providersIncluded"] = providers_included
        if outbound_calls_daily_limit is not UNSET:
            field_dict["outboundCallsDailyLimit"] = outbound_calls_daily_limit
        if outbound_calls_counter is not UNSET:
            field_dict["outboundCallsCounter"] = outbound_calls_counter
        if outbound_calls_counter_next_reset_at is not UNSET:
            field_dict["outboundCallsCounterNextResetAt"] = outbound_calls_counter_next_reset_at
        if coupon_ids is not UNSET:
            field_dict["couponIds"] = coupon_ids
        if coupon_usage_left is not UNSET:
            field_dict["couponUsageLeft"] = coupon_usage_left
        if invoice_plan is not UNSET:
            field_dict["invoicePlan"] = invoice_plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_reload_plan import AutoReloadPlan
        from ..models.invoice_plan import InvoicePlan

        d = dict(src_dict)
        id = d.pop("id")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        type_ = SubscriptionType(d.pop("type"))

        status = SubscriptionStatus(d.pop("status"))

        credits_ = d.pop("credits")

        concurrency_counter = d.pop("concurrencyCounter")

        concurrency_limit_included = d.pop("concurrencyLimitIncluded")

        concurrency_limit_purchased = d.pop("concurrencyLimitPurchased")

        phone_numbers_counter = d.pop("phoneNumbersCounter", UNSET)

        phone_numbers_included = d.pop("phoneNumbersIncluded", UNSET)

        monthly_charge_schedule_id = d.pop("monthlyChargeScheduleId", UNSET)

        monthly_credit_check_schedule_id = d.pop("monthlyCreditCheckScheduleId", UNSET)

        stripe_customer_id = d.pop("stripeCustomerId", UNSET)

        stripe_payment_method_id = d.pop("stripePaymentMethodId", UNSET)

        slack_support_enabled = d.pop("slackSupportEnabled", UNSET)

        slack_channel_id = d.pop("slackChannelId", UNSET)

        hipaa_enabled = d.pop("hipaaEnabled", UNSET)

        hipaa_common_paper_agreement_id = d.pop("hipaaCommonPaperAgreementId", UNSET)

        stripe_payment_method_fingerprint = d.pop("stripePaymentMethodFingerprint", UNSET)

        stripe_customer_email = d.pop("stripeCustomerEmail", UNSET)

        referred_by_email = d.pop("referredByEmail", UNSET)

        _auto_reload_plan = d.pop("autoReloadPlan", UNSET)
        auto_reload_plan: Union[Unset, AutoReloadPlan]
        if isinstance(_auto_reload_plan, Unset):
            auto_reload_plan = UNSET
        else:
            auto_reload_plan = AutoReloadPlan.from_dict(_auto_reload_plan)

        minutes_included = d.pop("minutesIncluded", UNSET)

        minutes_used = d.pop("minutesUsed", UNSET)

        _minutes_used_next_reset_at = d.pop("minutesUsedNextResetAt", UNSET)
        minutes_used_next_reset_at: Union[Unset, datetime.datetime]
        if isinstance(_minutes_used_next_reset_at, Unset):
            minutes_used_next_reset_at = UNSET
        else:
            minutes_used_next_reset_at = isoparse(_minutes_used_next_reset_at)

        minutes_overage_cost = d.pop("minutesOverageCost", UNSET)

        providers_included = cast(list[str], d.pop("providersIncluded", UNSET))

        outbound_calls_daily_limit = d.pop("outboundCallsDailyLimit", UNSET)

        outbound_calls_counter = d.pop("outboundCallsCounter", UNSET)

        _outbound_calls_counter_next_reset_at = d.pop("outboundCallsCounterNextResetAt", UNSET)
        outbound_calls_counter_next_reset_at: Union[Unset, datetime.datetime]
        if isinstance(_outbound_calls_counter_next_reset_at, Unset):
            outbound_calls_counter_next_reset_at = UNSET
        else:
            outbound_calls_counter_next_reset_at = isoparse(_outbound_calls_counter_next_reset_at)

        coupon_ids = cast(list[str], d.pop("couponIds", UNSET))

        coupon_usage_left = d.pop("couponUsageLeft", UNSET)

        _invoice_plan = d.pop("invoicePlan", UNSET)
        invoice_plan: Union[Unset, InvoicePlan]
        if isinstance(_invoice_plan, Unset):
            invoice_plan = UNSET
        else:
            invoice_plan = InvoicePlan.from_dict(_invoice_plan)

        subscription = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            type_=type_,
            status=status,
            credits_=credits_,
            concurrency_counter=concurrency_counter,
            concurrency_limit_included=concurrency_limit_included,
            concurrency_limit_purchased=concurrency_limit_purchased,
            phone_numbers_counter=phone_numbers_counter,
            phone_numbers_included=phone_numbers_included,
            monthly_charge_schedule_id=monthly_charge_schedule_id,
            monthly_credit_check_schedule_id=monthly_credit_check_schedule_id,
            stripe_customer_id=stripe_customer_id,
            stripe_payment_method_id=stripe_payment_method_id,
            slack_support_enabled=slack_support_enabled,
            slack_channel_id=slack_channel_id,
            hipaa_enabled=hipaa_enabled,
            hipaa_common_paper_agreement_id=hipaa_common_paper_agreement_id,
            stripe_payment_method_fingerprint=stripe_payment_method_fingerprint,
            stripe_customer_email=stripe_customer_email,
            referred_by_email=referred_by_email,
            auto_reload_plan=auto_reload_plan,
            minutes_included=minutes_included,
            minutes_used=minutes_used,
            minutes_used_next_reset_at=minutes_used_next_reset_at,
            minutes_overage_cost=minutes_overage_cost,
            providers_included=providers_included,
            outbound_calls_daily_limit=outbound_calls_daily_limit,
            outbound_calls_counter=outbound_calls_counter,
            outbound_calls_counter_next_reset_at=outbound_calls_counter_next_reset_at,
            coupon_ids=coupon_ids,
            coupon_usage_left=coupon_usage_left,
            invoice_plan=invoice_plan,
        )

        subscription.additional_properties = d
        return subscription

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
