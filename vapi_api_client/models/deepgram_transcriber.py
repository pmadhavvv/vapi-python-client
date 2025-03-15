from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deepgram_transcriber_language import DeepgramTranscriberLanguage
from ..models.deepgram_transcriber_model_type_0 import DeepgramTranscriberModelType0
from ..models.deepgram_transcriber_provider import DeepgramTranscriberProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeepgramTranscriber")


@_attrs_define
class DeepgramTranscriber:
    """
    Attributes:
        provider (DeepgramTranscriberProvider): This is the transcription provider that will be used.
        model (Union[DeepgramTranscriberModelType0, Unset, str]): This is the Deepgram model that will be used. A list
            of models can be found here: https://developers.deepgram.com/docs/models-languages-overview
        language (Union[Unset, DeepgramTranscriberLanguage]): This is the language that will be set for the
            transcription. The list of languages Deepgram supports can be found here:
            https://developers.deepgram.com/docs/models-languages-overview
        smart_format (Union[Unset, bool]): This will be use smart format option provided by Deepgram. It's default
            disabled because it can sometimes format numbers as times but it's getting better.
        code_switching_enabled (Union[Unset, bool]): This automatically switches the transcriber's language when the
            customer's language changes. Defaults to false.

            Usage:
            - If your customers switch languages mid-call, you can set this to true.

            Note:
            - To detect language changes, Vapi uses a custom trained model. Languages supported (X = limited support):
              1. Arabic
              2. Bengali
              3. Cantonese
              4. Chinese
              5. Chinese Simplified (X)
              6. Chinese Traditional (X)
              7. English
              8. Farsi (X)
              9. French
              10. German
              11. Haitian Creole (X)
              12. Hindi
              13. Italian
              14. Japanese
              15. Korean
              16. Portuguese
              17. Russian
              18. Spanish
              19. Thai
              20. Urdu
              21. Vietnamese
            - To receive `language-change-detected` webhook events, add it to `assistant.serverMessages`.

            @default false
        mip_opt_out (Union[Unset, bool]): If set to true, this will add mip_opt_out=true as a query parameter of all API
            requests. See https://developers.deepgram.com/docs/the-deepgram-model-improvement-partnership-program#want-to-
            opt-out

            This will only be used if you are using your own Deepgram API key.

            @default false
        numerals (Union[Unset, bool]): If set to true, this will cause deepgram to convert spoken numbers to literal
            numerals. For example, "my phone number is nine-seven-two..." would become "my phone number is 972..."

            @default false
        keywords (Union[Unset, list[str]]): These keywords are passed to the transcription model to help it pick up use-
            case specific words. Anything that may not be a common word, like your company name, should be added here.
        keyterm (Union[Unset, list[str]]): Keyterm Prompting allows you improve Keyword Recall Rate (KRR) for important
            keyterms or phrases up to 90%.
        endpointing (Union[Unset, float]): This is the timeout after which Deepgram will send transcription on user
            silence. You can read in-depth documentation here: https://developers.deepgram.com/docs/endpointing.

            Here are the most important bits:
            - Defaults to 10. This is recommended for most use cases to optimize for latency.
            - 10 can cause some missing transcriptions since because of the shorter context. This mostly happens for one-
            word utterances. For those uses cases, it's recommended to try 300. It will add a bit of latency but the quality
            and reliability of the experience will be better.
            - If neither 10 nor 300 work, contact support@vapi.ai and we'll find another solution.

            @default 10
    """

    provider: DeepgramTranscriberProvider
    model: Union[DeepgramTranscriberModelType0, Unset, str] = UNSET
    language: Union[Unset, DeepgramTranscriberLanguage] = UNSET
    smart_format: Union[Unset, bool] = UNSET
    code_switching_enabled: Union[Unset, bool] = UNSET
    mip_opt_out: Union[Unset, bool] = UNSET
    numerals: Union[Unset, bool] = UNSET
    keywords: Union[Unset, list[str]] = UNSET
    keyterm: Union[Unset, list[str]] = UNSET
    endpointing: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        model: Union[Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, DeepgramTranscriberModelType0):
            model = self.model.value
        else:
            model = self.model

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        smart_format = self.smart_format

        code_switching_enabled = self.code_switching_enabled

        mip_opt_out = self.mip_opt_out

        numerals = self.numerals

        keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        keyterm: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keyterm, Unset):
            keyterm = self.keyterm

        endpointing = self.endpointing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if language is not UNSET:
            field_dict["language"] = language
        if smart_format is not UNSET:
            field_dict["smartFormat"] = smart_format
        if code_switching_enabled is not UNSET:
            field_dict["codeSwitchingEnabled"] = code_switching_enabled
        if mip_opt_out is not UNSET:
            field_dict["mipOptOut"] = mip_opt_out
        if numerals is not UNSET:
            field_dict["numerals"] = numerals
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if keyterm is not UNSET:
            field_dict["keyterm"] = keyterm
        if endpointing is not UNSET:
            field_dict["endpointing"] = endpointing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = DeepgramTranscriberProvider(d.pop("provider"))

        def _parse_model(data: object) -> Union[DeepgramTranscriberModelType0, Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_type_0 = DeepgramTranscriberModelType0(data)

                return model_type_0
            except:  # noqa: E722
                pass
            return cast(Union[DeepgramTranscriberModelType0, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        _language = d.pop("language", UNSET)
        language: Union[Unset, DeepgramTranscriberLanguage]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = DeepgramTranscriberLanguage(_language)

        smart_format = d.pop("smartFormat", UNSET)

        code_switching_enabled = d.pop("codeSwitchingEnabled", UNSET)

        mip_opt_out = d.pop("mipOptOut", UNSET)

        numerals = d.pop("numerals", UNSET)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        keyterm = cast(list[str], d.pop("keyterm", UNSET))

        endpointing = d.pop("endpointing", UNSET)

        deepgram_transcriber = cls(
            provider=provider,
            model=model,
            language=language,
            smart_format=smart_format,
            code_switching_enabled=code_switching_enabled,
            mip_opt_out=mip_opt_out,
            numerals=numerals,
            keywords=keywords,
            keyterm=keyterm,
            endpointing=endpointing,
        )

        deepgram_transcriber.additional_properties = d
        return deepgram_transcriber

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
