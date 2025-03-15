from enum import Enum


class DeepgramTranscriberModelType0(str, Enum):
    BASE = "base"
    BASE_CONVERSATIONALAI = "base-conversationalai"
    BASE_FINANCE = "base-finance"
    BASE_GENERAL = "base-general"
    BASE_MEETING = "base-meeting"
    BASE_PHONECALL = "base-phonecall"
    BASE_VIDEO = "base-video"
    BASE_VOICEMAIL = "base-voicemail"
    ENHANCED = "enhanced"
    ENHANCED_FINANCE = "enhanced-finance"
    ENHANCED_GENERAL = "enhanced-general"
    ENHANCED_MEETING = "enhanced-meeting"
    ENHANCED_PHONECALL = "enhanced-phonecall"
    NOVA = "nova"
    NOVA_2 = "nova-2"
    NOVA_2_AUTOMOTIVE = "nova-2-automotive"
    NOVA_2_CONVERSATIONALAI = "nova-2-conversationalai"
    NOVA_2_DRIVETHRU = "nova-2-drivethru"
    NOVA_2_FINANCE = "nova-2-finance"
    NOVA_2_GENERAL = "nova-2-general"
    NOVA_2_MEDICAL = "nova-2-medical"
    NOVA_2_MEETING = "nova-2-meeting"
    NOVA_2_PHONECALL = "nova-2-phonecall"
    NOVA_2_VIDEO = "nova-2-video"
    NOVA_2_VOICEMAIL = "nova-2-voicemail"
    NOVA_3 = "nova-3"
    NOVA_3_GENERAL = "nova-3-general"
    NOVA_GENERAL = "nova-general"
    NOVA_MEDICAL = "nova-medical"
    NOVA_PHONECALL = "nova-phonecall"

    def __str__(self) -> str:
        return str(self.value)
