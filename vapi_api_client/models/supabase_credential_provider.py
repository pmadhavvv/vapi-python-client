from enum import Enum


class SupabaseCredentialProvider(str, Enum):
    SUPABASE = "supabase"

    def __str__(self) -> str:
        return str(self.value)
