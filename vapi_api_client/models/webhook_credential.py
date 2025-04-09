import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.webhook_credential_provider import WebhookCredentialProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_2_authentication_plan import OAuth2AuthenticationPlan
    from ..models.oauth_2_authentication_session import Oauth2AuthenticationSession


T = TypeVar("T", bound="WebhookCredential")


@_attrs_define
class WebhookCredential:
    """
    Attributes:
        provider (WebhookCredentialProvider):
        authentication_plan (OAuth2AuthenticationPlan):
        id (str): This is the unique identifier for the credential.
        org_id (str): This is the unique identifier for the org that this credential belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the credential was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the assistant was last updated.
        authentication_session (Oauth2AuthenticationSession):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: WebhookCredentialProvider
    authentication_plan: "OAuth2AuthenticationPlan"
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    authentication_session: "Oauth2AuthenticationSession"
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        authentication_plan = self.authentication_plan.to_dict()

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        authentication_session = self.authentication_session.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "authenticationPlan": authentication_plan,
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "authenticationSession": authentication_session,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_2_authentication_plan import OAuth2AuthenticationPlan
        from ..models.oauth_2_authentication_session import Oauth2AuthenticationSession

        d = dict(src_dict)
        provider = WebhookCredentialProvider(d.pop("provider"))

        authentication_plan = OAuth2AuthenticationPlan.from_dict(d.pop("authenticationPlan"))

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        authentication_session = Oauth2AuthenticationSession.from_dict(d.pop("authenticationSession"))

        name = d.pop("name", UNSET)

        webhook_credential = cls(
            provider=provider,
            authentication_plan=authentication_plan,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            authentication_session=authentication_session,
            name=name,
        )

        webhook_credential.additional_properties = d
        return webhook_credential

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
