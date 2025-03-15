from enum import Enum


class FormatPlanFormattersEnabled(str, Enum):
    ACRONYM = "acronym"
    ASTERISK = "asterisk"
    COLON = "colon"
    DASH = "dash"
    DATE = "date"
    DISTANCE = "distance"
    DOLLARAMOUNT = "dollarAmount"
    EMAIL = "email"
    MARKDOWN = "markdown"
    NEWLINE = "newline"
    NUMBER = "number"
    PERCENTAGE = "percentage"
    PHONENUMBER = "phoneNumber"
    QUOTE = "quote"
    TIME = "time"
    UNIT = "unit"

    def __str__(self) -> str:
        return str(self.value)
