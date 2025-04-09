from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GcpKey")


@_attrs_define
class GcpKey:
    """
    Attributes:
        type_ (str): This is the type of the key. Most likely, this is "service_account".
        project_id (str): This is the ID of the Google Cloud project associated with this key.
        private_key_id (str): This is the unique identifier for the private key.
        private_key (str): This is the private key in PEM format.

            Note: This is not returned in the API.
        client_email (str): This is the email address associated with the service account.
        client_id (str): This is the unique identifier for the client.
        auth_uri (str): This is the URI for the auth provider's authorization endpoint.
        token_uri (str): This is the URI for the auth provider's token endpoint.
        auth_provider_x509_cert_url (str): This is the URL of the public x509 certificate for the auth provider.
        client_x509_cert_url (str): This is the URL of the public x509 certificate for the client.
        universe_domain (str): This is the domain associated with the universe this service account belongs to.
    """

    type_: str
    project_id: str
    private_key_id: str
    private_key: str
    client_email: str
    client_id: str
    auth_uri: str
    token_uri: str
    auth_provider_x509_cert_url: str
    client_x509_cert_url: str
    universe_domain: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        project_id = self.project_id

        private_key_id = self.private_key_id

        private_key = self.private_key

        client_email = self.client_email

        client_id = self.client_id

        auth_uri = self.auth_uri

        token_uri = self.token_uri

        auth_provider_x509_cert_url = self.auth_provider_x509_cert_url

        client_x509_cert_url = self.client_x509_cert_url

        universe_domain = self.universe_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "projectId": project_id,
                "privateKeyId": private_key_id,
                "privateKey": private_key,
                "clientEmail": client_email,
                "clientId": client_id,
                "authUri": auth_uri,
                "tokenUri": token_uri,
                "authProviderX509CertUrl": auth_provider_x509_cert_url,
                "clientX509CertUrl": client_x509_cert_url,
                "universeDomain": universe_domain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        project_id = d.pop("projectId")

        private_key_id = d.pop("privateKeyId")

        private_key = d.pop("privateKey")

        client_email = d.pop("clientEmail")

        client_id = d.pop("clientId")

        auth_uri = d.pop("authUri")

        token_uri = d.pop("tokenUri")

        auth_provider_x509_cert_url = d.pop("authProviderX509CertUrl")

        client_x509_cert_url = d.pop("clientX509CertUrl")

        universe_domain = d.pop("universeDomain")

        gcp_key = cls(
            type_=type_,
            project_id=project_id,
            private_key_id=private_key_id,
            private_key=private_key,
            client_email=client_email,
            client_id=client_id,
            auth_uri=auth_uri,
            token_uri=token_uri,
            auth_provider_x509_cert_url=auth_provider_x509_cert_url,
            client_x509_cert_url=client_x509_cert_url,
            universe_domain=universe_domain,
        )

        gcp_key.additional_properties = d
        return gcp_key

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
