from enum import Enum


class CartesiaExperimentalControlsSpeed(str, Enum):
    FAST = "fast"
    FASTEST = "fastest"
    NORMAL = "normal"
    SLOW = "slow"
    SLOWEST = "slowest"

    def __str__(self) -> str:
        return str(self.value)
