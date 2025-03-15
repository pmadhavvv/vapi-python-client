from enum import Enum


class PlayHTVoiceEmotion(str, Enum):
    FEMALE_ANGRY = "female_angry"
    FEMALE_DISGUST = "female_disgust"
    FEMALE_FEARFUL = "female_fearful"
    FEMALE_HAPPY = "female_happy"
    FEMALE_SAD = "female_sad"
    FEMALE_SURPRISED = "female_surprised"
    MALE_ANGRY = "male_angry"
    MALE_DISGUST = "male_disgust"
    MALE_FEARFUL = "male_fearful"
    MALE_HAPPY = "male_happy"
    MALE_SAD = "male_sad"
    MALE_SURPRISED = "male_surprised"

    def __str__(self) -> str:
        return str(self.value)
