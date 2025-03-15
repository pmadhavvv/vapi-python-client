from enum import Enum


class ModelCostType(str, Enum):
    MODEL = "model"

    def __str__(self) -> str:
        return str(self.value)
