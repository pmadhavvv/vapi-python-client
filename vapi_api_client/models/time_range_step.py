from enum import Enum


class TimeRangeStep(str, Enum):
    CENTURY = "century"
    DAY = "day"
    DECADE = "decade"
    HOUR = "hour"
    MILLENNIUM = "millennium"
    MINUTE = "minute"
    MONTH = "month"
    QUARTER = "quarter"
    SECOND = "second"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
