import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.voice_library_gender import VoiceLibraryGender
from ..models.voice_library_provider import VoiceLibraryProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoiceLibrary")


@_attrs_define
class VoiceLibrary:
    """
    Attributes:
        id (str): The unique identifier for the voice library.
        org_id (str): The unique identifier for the organization that this voice library belongs to.
        is_public (bool): The Public voice is shared accross all the organizations.
        is_deleted (bool): The deletion status of the voice.
        created_at (datetime.datetime): The ISO 8601 date-time string of when the voice library was created.
        updated_at (datetime.datetime): The ISO 8601 date-time string of when the voice library was last updated.
        provider (Union[Unset, VoiceLibraryProvider]): This is the voice provider that will be used.
        provider_id (Union[Unset, str]): The ID of the voice provided by the provider.
        slug (Union[Unset, str]): The unique slug of the voice.
        name (Union[Unset, str]): The name of the voice.
        language (Union[Unset, str]): The language of the voice.
        language_code (Union[Unset, str]): The language code of the voice.
        model (Union[Unset, str]): The model of the voice.
        supported_models (Union[Unset, str]): The supported models of the voice.
        gender (Union[Unset, VoiceLibraryGender]): The gender of the voice.
        accent (Union[Unset, str]): The accent of the voice.
        preview_url (Union[Unset, str]): The preview URL of the voice.
        description (Union[Unset, str]): The description of the voice.
        credential_id (Union[Unset, str]): The credential ID of the voice.
    """

    id: str
    org_id: str
    is_public: bool
    is_deleted: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    provider: Union[Unset, VoiceLibraryProvider] = UNSET
    provider_id: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    language_code: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    supported_models: Union[Unset, str] = UNSET
    gender: Union[Unset, VoiceLibraryGender] = UNSET
    accent: Union[Unset, str] = UNSET
    preview_url: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    credential_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        org_id = self.org_id

        is_public = self.is_public

        is_deleted = self.is_deleted

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        provider_id = self.provider_id

        slug = self.slug

        name = self.name

        language = self.language

        language_code = self.language_code

        model = self.model

        supported_models = self.supported_models

        gender: Union[Unset, str] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        accent = self.accent

        preview_url = self.preview_url

        description = self.description

        credential_id = self.credential_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "orgId": org_id,
                "isPublic": is_public,
                "isDeleted": is_deleted,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if language is not UNSET:
            field_dict["language"] = language
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if model is not UNSET:
            field_dict["model"] = model
        if supported_models is not UNSET:
            field_dict["supportedModels"] = supported_models
        if gender is not UNSET:
            field_dict["gender"] = gender
        if accent is not UNSET:
            field_dict["accent"] = accent
        if preview_url is not UNSET:
            field_dict["previewUrl"] = preview_url
        if description is not UNSET:
            field_dict["description"] = description
        if credential_id is not UNSET:
            field_dict["credentialId"] = credential_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        org_id = d.pop("orgId")

        is_public = d.pop("isPublic")

        is_deleted = d.pop("isDeleted")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, VoiceLibraryProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = VoiceLibraryProvider(_provider)

        provider_id = d.pop("providerId", UNSET)

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        language = d.pop("language", UNSET)

        language_code = d.pop("languageCode", UNSET)

        model = d.pop("model", UNSET)

        supported_models = d.pop("supportedModels", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, VoiceLibraryGender]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = VoiceLibraryGender(_gender)

        accent = d.pop("accent", UNSET)

        preview_url = d.pop("previewUrl", UNSET)

        description = d.pop("description", UNSET)

        credential_id = d.pop("credentialId", UNSET)

        voice_library = cls(
            id=id,
            org_id=org_id,
            is_public=is_public,
            is_deleted=is_deleted,
            created_at=created_at,
            updated_at=updated_at,
            provider=provider,
            provider_id=provider_id,
            slug=slug,
            name=name,
            language=language,
            language_code=language_code,
            model=model,
            supported_models=supported_models,
            gender=gender,
            accent=accent,
            preview_url=preview_url,
            description=description,
            credential_id=credential_id,
        )

        voice_library.additional_properties = d
        return voice_library

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
