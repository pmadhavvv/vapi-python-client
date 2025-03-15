from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.o_auth_2_authentication_plan_type import OAuth2AuthenticationPlanType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2AuthenticationPlan")


@_attrs_define
class OAuth2AuthenticationPlan:
    """
    Attributes:
        type_ (OAuth2AuthenticationPlanType):
        url (str): This is the OAuth2 URL.
        client_id (str): This is the OAuth2 client ID.
        client_secret (str): This is the OAuth2 client secret.
        scope (Union[Unset, str]): This is the scope of the OAuth2 token.
    """

    type_: OAuth2AuthenticationPlanType
    url: str
    client_id: str
    client_secret: str
    scope: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        url = self.url

        client_id = self.client_id

        client_secret = self.client_secret

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "url": url,
                "clientId": client_id,
                "clientSecret": client_secret,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = OAuth2AuthenticationPlanType(d.pop("type"))

        url = d.pop("url")

        client_id = d.pop("clientId")

        client_secret = d.pop("clientSecret")

        scope = d.pop("scope", UNSET)

        o_auth_2_authentication_plan = cls(
            type_=type_,
            url=url,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
        )

        o_auth_2_authentication_plan.additional_properties = d
        return o_auth_2_authentication_plan

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
