from enum import Enum


class CartesiaExperimentalControlsEmotion(str, Enum):
    ANGERHIGH = "anger:high"
    ANGERHIGHEST = "anger:highest"
    ANGERLOW = "anger:low"
    ANGERLOWEST = "anger:lowest"
    CURIOSITYHIGH = "curiosity:high"
    CURIOSITYHIGHEST = "curiosity:highest"
    CURIOSITYLOW = "curiosity:low"
    CURIOSITYLOWEST = "curiosity:lowest"
    POSITIVITYHIGH = "positivity:high"
    POSITIVITYHIGHEST = "positivity:highest"
    POSITIVITYLOW = "positivity:low"
    POSITIVITYLOWEST = "positivity:lowest"
    SADNESSHIGH = "sadness:high"
    SADNESSHIGHEST = "sadness:highest"
    SADNESSLOW = "sadness:low"
    SADNESSLOWEST = "sadness:lowest"
    SURPRISEHIGH = "surprise:high"
    SURPRISEHIGHEST = "surprise:highest"
    SURPRISELOW = "surprise:low"
    SURPRISELOWEST = "surprise:lowest"

    def __str__(self) -> str:
        return str(self.value)
