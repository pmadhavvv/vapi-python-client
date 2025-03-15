from enum import Enum


class AzureSpeechTranscriberLanguage(str, Enum):
    AF_ZA = "af-ZA"
    AM_ET = "am-ET"
    AR_AE = "ar-AE"
    AR_BH = "ar-BH"
    AR_DZ = "ar-DZ"
    AR_EG = "ar-EG"
    AR_IL = "ar-IL"
    AR_IQ = "ar-IQ"
    AR_JO = "ar-JO"
    AR_KW = "ar-KW"
    AR_LB = "ar-LB"
    AR_LY = "ar-LY"
    AR_MA = "ar-MA"
    AR_OM = "ar-OM"
    AR_PS = "ar-PS"
    AR_QA = "ar-QA"
    AR_SA = "ar-SA"
    AR_SY = "ar-SY"
    AR_TN = "ar-TN"
    AR_YE = "ar-YE"
    AZ_AZ = "az-AZ"
    BG_BG = "bg-BG"
    BN_IN = "bn-IN"
    BS_BA = "bs-BA"
    CA_ES = "ca-ES"
    CS_CZ = "cs-CZ"
    CY_GB = "cy-GB"
    DA_DK = "da-DK"
    DE_AT = "de-AT"
    DE_CH = "de-CH"
    DE_DE = "de-DE"
    EL_GR = "el-GR"
    EN_AU = "en-AU"
    EN_CA = "en-CA"
    EN_GB = "en-GB"
    EN_GH = "en-GH"
    EN_HK = "en-HK"
    EN_IE = "en-IE"
    EN_IN = "en-IN"
    EN_KE = "en-KE"
    EN_NG = "en-NG"
    EN_NZ = "en-NZ"
    EN_PH = "en-PH"
    EN_SG = "en-SG"
    EN_TZ = "en-TZ"
    EN_US = "en-US"
    EN_ZA = "en-ZA"
    ES_AR = "es-AR"
    ES_BO = "es-BO"
    ES_CL = "es-CL"
    ES_CO = "es-CO"
    ES_CR = "es-CR"
    ES_CU = "es-CU"
    ES_DO = "es-DO"
    ES_EC = "es-EC"
    ES_ES = "es-ES"
    ES_GQ = "es-GQ"
    ES_GT = "es-GT"
    ES_HN = "es-HN"
    ES_MX = "es-MX"
    ES_NI = "es-NI"
    ES_PA = "es-PA"
    ES_PE = "es-PE"
    ES_PR = "es-PR"
    ES_PY = "es-PY"
    ES_SV = "es-SV"
    ES_US = "es-US"
    ES_UY = "es-UY"
    ES_VE = "es-VE"
    ET_EE = "et-EE"
    EU_ES = "eu-ES"
    FA_IR = "fa-IR"
    FIL_PH = "fil-PH"
    FI_FI = "fi-FI"
    FR_BE = "fr-BE"
    FR_CA = "fr-CA"
    FR_CH = "fr-CH"
    FR_FR = "fr-FR"
    GA_IE = "ga-IE"
    GL_ES = "gl-ES"
    GU_IN = "gu-IN"
    HE_IL = "he-IL"
    HI_IN = "hi-IN"
    HR_HR = "hr-HR"
    HU_HU = "hu-HU"
    HY_AM = "hy-AM"
    ID_ID = "id-ID"
    IS_IS = "is-IS"
    IT_CH = "it-CH"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    JV_ID = "jv-ID"
    KA_GE = "ka-GE"
    KK_KZ = "kk-KZ"
    KM_KH = "km-KH"
    KN_IN = "kn-IN"
    KO_KR = "ko-KR"
    LO_LA = "lo-LA"
    LT_LT = "lt-LT"
    LV_LV = "lv-LV"
    MK_MK = "mk-MK"
    ML_IN = "ml-IN"
    MN_MN = "mn-MN"
    MR_IN = "mr-IN"
    MS_MY = "ms-MY"
    MT_MT = "mt-MT"
    MY_MM = "my-MM"
    NB_NO = "nb-NO"
    NE_NP = "ne-NP"
    NL_BE = "nl-BE"
    NL_NL = "nl-NL"
    PA_IN = "pa-IN"
    PL_PL = "pl-PL"
    PS_AF = "ps-AF"
    PT_BR = "pt-BR"
    PT_PT = "pt-PT"
    RO_RO = "ro-RO"
    RU_RU = "ru-RU"
    SI_LK = "si-LK"
    SK_SK = "sk-SK"
    SL_SI = "sl-SI"
    SO_SO = "so-SO"
    SQ_AL = "sq-AL"
    SR_RS = "sr-RS"
    SV_SE = "sv-SE"
    SW_KE = "sw-KE"
    SW_TZ = "sw-TZ"
    TA_IN = "ta-IN"
    TE_IN = "te-IN"
    TH_TH = "th-TH"
    TR_TR = "tr-TR"
    UK_UA = "uk-UA"
    UR_IN = "ur-IN"
    UZ_UZ = "uz-UZ"
    VI_VN = "vi-VN"
    WUU_CN = "wuu-CN"
    YUE_CN = "yue-CN"
    ZH_CN = "zh-CN"
    ZH_CN_SHANDONG = "zh-CN-shandong"
    ZH_CN_SICHUAN = "zh-CN-sichuan"
    ZH_HK = "zh-HK"
    ZH_TW = "zh-TW"
    ZU_ZA = "zu-ZA"

    def __str__(self) -> str:
        return str(self.value)
