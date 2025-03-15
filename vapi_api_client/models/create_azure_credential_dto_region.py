from enum import Enum


class CreateAzureCredentialDTORegion(str, Enum):
    AUSTRALIA = "australia"
    CANADACENTRAL = "canadacentral"
    CANADAEAST = "canadaeast"
    EASTUS = "eastus"
    EASTUS2 = "eastus2"
    FRANCE = "france"
    INDIA = "india"
    JAPANEAST = "japaneast"
    JAPANWEST = "japanwest"
    NORTHCENTRALUS = "northcentralus"
    NORWAY = "norway"
    SOUTHCENTRALUS = "southcentralus"
    SWEDENCENTRAL = "swedencentral"
    SWITZERLAND = "switzerland"
    UAENORTH = "uaenorth"
    UK = "uk"
    WESTUS = "westus"
    WESTUS3 = "westus3"

    def __str__(self) -> str:
        return str(self.value)
