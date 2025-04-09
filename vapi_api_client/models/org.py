import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.org_channel import OrgChannel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_plan import OrgPlan
    from ..models.server import Server
    from ..models.subscription import Subscription


T = TypeVar("T", bound="Org")


@_attrs_define
class Org:
    """
    Attributes:
        id (str): This is the unique identifier for the org.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the org was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the org was last updated.
        hipaa_enabled (Union[Unset, bool]): When this is enabled, no logs, recordings, or transcriptions will be stored.
            At the end of the call, you will still receive an end-of-call-report message to store on your server. Defaults
            to false.
            When HIPAA is enabled, only OpenAI/Custom LLM or Azure Providers will be available for LLM and Voice
            respectively.
            This is due to the compliance requirements of HIPAA. Other providers may not meet these requirements.
        subscription (Union[Unset, Subscription]):
        subscription_id (Union[Unset, str]): This is the ID of the subscription the org belongs to.
        stripe_customer_id (Union[Unset, str]): This is the Stripe customer for the org.
        stripe_subscription_id (Union[Unset, str]): This is the subscription for the org.
        stripe_subscription_item_id (Union[Unset, str]): This is the subscription's subscription item.
        stripe_subscription_current_period_start (Union[Unset, datetime.datetime]): This is the subscription's current
            period start.
        stripe_subscription_status (Union[Unset, str]): This is the subscription's status.
        plan (Union[Unset, OrgPlan]):
        name (Union[Unset, str]): This is the name of the org. This is just for your own reference.
        channel (Union[Unset, OrgChannel]): This is the channel of the org. There is the cluster the API traffic for the
            org will be directed.
        billing_limit (Union[Unset, float]): This is the monthly billing limit for the org. To go beyond $1000/mo,
            please contact us at support@vapi.ai.
        server (Union[Unset, Server]):
        concurrency_limit (Union[Unset, float]): This is the concurrency limit for the org. This is the maximum number
            of calls that can be active at any given time. To go beyond 10, please contact us at support@vapi.ai.
    """

    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    hipaa_enabled: Union[Unset, bool] = UNSET
    subscription: Union[Unset, "Subscription"] = UNSET
    subscription_id: Union[Unset, str] = UNSET
    stripe_customer_id: Union[Unset, str] = UNSET
    stripe_subscription_id: Union[Unset, str] = UNSET
    stripe_subscription_item_id: Union[Unset, str] = UNSET
    stripe_subscription_current_period_start: Union[Unset, datetime.datetime] = UNSET
    stripe_subscription_status: Union[Unset, str] = UNSET
    plan: Union[Unset, "OrgPlan"] = UNSET
    name: Union[Unset, str] = UNSET
    channel: Union[Unset, OrgChannel] = UNSET
    billing_limit: Union[Unset, float] = UNSET
    server: Union[Unset, "Server"] = UNSET
    concurrency_limit: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        hipaa_enabled = self.hipaa_enabled

        subscription: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.subscription, Unset):
            subscription = self.subscription.to_dict()

        subscription_id = self.subscription_id

        stripe_customer_id = self.stripe_customer_id

        stripe_subscription_id = self.stripe_subscription_id

        stripe_subscription_item_id = self.stripe_subscription_item_id

        stripe_subscription_current_period_start: Union[Unset, str] = UNSET
        if not isinstance(self.stripe_subscription_current_period_start, Unset):
            stripe_subscription_current_period_start = self.stripe_subscription_current_period_start.isoformat()

        stripe_subscription_status = self.stripe_subscription_status

        plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.to_dict()

        name = self.name

        channel: Union[Unset, str] = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value

        billing_limit = self.billing_limit

        server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        concurrency_limit = self.concurrency_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if hipaa_enabled is not UNSET:
            field_dict["hipaaEnabled"] = hipaa_enabled
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if stripe_customer_id is not UNSET:
            field_dict["stripeCustomerId"] = stripe_customer_id
        if stripe_subscription_id is not UNSET:
            field_dict["stripeSubscriptionId"] = stripe_subscription_id
        if stripe_subscription_item_id is not UNSET:
            field_dict["stripeSubscriptionItemId"] = stripe_subscription_item_id
        if stripe_subscription_current_period_start is not UNSET:
            field_dict["stripeSubscriptionCurrentPeriodStart"] = stripe_subscription_current_period_start
        if stripe_subscription_status is not UNSET:
            field_dict["stripeSubscriptionStatus"] = stripe_subscription_status
        if plan is not UNSET:
            field_dict["plan"] = plan
        if name is not UNSET:
            field_dict["name"] = name
        if channel is not UNSET:
            field_dict["channel"] = channel
        if billing_limit is not UNSET:
            field_dict["billingLimit"] = billing_limit
        if server is not UNSET:
            field_dict["server"] = server
        if concurrency_limit is not UNSET:
            field_dict["concurrencyLimit"] = concurrency_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_plan import OrgPlan
        from ..models.server import Server
        from ..models.subscription import Subscription

        d = dict(src_dict)
        id = d.pop("id")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        hipaa_enabled = d.pop("hipaaEnabled", UNSET)

        _subscription = d.pop("subscription", UNSET)
        subscription: Union[Unset, Subscription]
        if isinstance(_subscription, Unset):
            subscription = UNSET
        else:
            subscription = Subscription.from_dict(_subscription)

        subscription_id = d.pop("subscriptionId", UNSET)

        stripe_customer_id = d.pop("stripeCustomerId", UNSET)

        stripe_subscription_id = d.pop("stripeSubscriptionId", UNSET)

        stripe_subscription_item_id = d.pop("stripeSubscriptionItemId", UNSET)

        _stripe_subscription_current_period_start = d.pop("stripeSubscriptionCurrentPeriodStart", UNSET)
        stripe_subscription_current_period_start: Union[Unset, datetime.datetime]
        if isinstance(_stripe_subscription_current_period_start, Unset):
            stripe_subscription_current_period_start = UNSET
        else:
            stripe_subscription_current_period_start = isoparse(_stripe_subscription_current_period_start)

        stripe_subscription_status = d.pop("stripeSubscriptionStatus", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: Union[Unset, OrgPlan]
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = OrgPlan.from_dict(_plan)

        name = d.pop("name", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: Union[Unset, OrgChannel]
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = OrgChannel(_channel)

        billing_limit = d.pop("billingLimit", UNSET)

        _server = d.pop("server", UNSET)
        server: Union[Unset, Server]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = Server.from_dict(_server)

        concurrency_limit = d.pop("concurrencyLimit", UNSET)

        org = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            hipaa_enabled=hipaa_enabled,
            subscription=subscription,
            subscription_id=subscription_id,
            stripe_customer_id=stripe_customer_id,
            stripe_subscription_id=stripe_subscription_id,
            stripe_subscription_item_id=stripe_subscription_item_id,
            stripe_subscription_current_period_start=stripe_subscription_current_period_start,
            stripe_subscription_status=stripe_subscription_status,
            plan=plan,
            name=name,
            channel=channel,
            billing_limit=billing_limit,
            server=server,
            concurrency_limit=concurrency_limit,
        )

        org.additional_properties = d
        return org

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
