import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.custom_llm_credential_provider import CustomLLMCredentialProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_2_authentication_plan import OAuth2AuthenticationPlan
    from ..models.oauth_2_authentication_session import Oauth2AuthenticationSession


T = TypeVar("T", bound="CustomLLMCredential")


@_attrs_define
class CustomLLMCredential:
    """
    Attributes:
        provider (CustomLLMCredentialProvider):
        api_key (str): This is not returned in the API.
        id (str): This is the unique identifier for the credential.
        org_id (str): This is the unique identifier for the org that this credential belongs to.
        created_at (datetime.datetime): This is the ISO 8601 date-time string of when the credential was created.
        updated_at (datetime.datetime): This is the ISO 8601 date-time string of when the assistant was last updated.
        authentication_plan (Union[Unset, OAuth2AuthenticationPlan]):
        authentication_session (Union[Unset, Oauth2AuthenticationSession]):
        name (Union[Unset, str]): This is the name of credential. This is just for your reference.
    """

    provider: CustomLLMCredentialProvider
    api_key: str
    id: str
    org_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    authentication_plan: Union[Unset, "OAuth2AuthenticationPlan"] = UNSET
    authentication_session: Union[Unset, "Oauth2AuthenticationSession"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        api_key = self.api_key

        id = self.id

        org_id = self.org_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        authentication_plan: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.authentication_plan, Unset):
            authentication_plan = self.authentication_plan.to_dict()

        authentication_session: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.authentication_session, Unset):
            authentication_session = self.authentication_session.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "apiKey": api_key,
                "id": id,
                "orgId": org_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if authentication_plan is not UNSET:
            field_dict["authenticationPlan"] = authentication_plan
        if authentication_session is not UNSET:
            field_dict["authenticationSession"] = authentication_session
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_2_authentication_plan import OAuth2AuthenticationPlan
        from ..models.oauth_2_authentication_session import Oauth2AuthenticationSession

        d = dict(src_dict)
        provider = CustomLLMCredentialProvider(d.pop("provider"))

        api_key = d.pop("apiKey")

        id = d.pop("id")

        org_id = d.pop("orgId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _authentication_plan = d.pop("authenticationPlan", UNSET)
        authentication_plan: Union[Unset, OAuth2AuthenticationPlan]
        if isinstance(_authentication_plan, Unset):
            authentication_plan = UNSET
        else:
            authentication_plan = OAuth2AuthenticationPlan.from_dict(_authentication_plan)

        _authentication_session = d.pop("authenticationSession", UNSET)
        authentication_session: Union[Unset, Oauth2AuthenticationSession]
        if isinstance(_authentication_session, Unset):
            authentication_session = UNSET
        else:
            authentication_session = Oauth2AuthenticationSession.from_dict(_authentication_session)

        name = d.pop("name", UNSET)

        custom_llm_credential = cls(
            provider=provider,
            api_key=api_key,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            authentication_plan=authentication_plan,
            authentication_session=authentication_session,
            name=name,
        )

        custom_llm_credential.additional_properties = d
        return custom_llm_credential

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
