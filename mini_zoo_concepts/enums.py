from enum import Enum

__all__ = ["Category", "Domain", "Language", "FeatureType"]


class Language(Enum):
    ENGLISH = "en"

    def __str__(self):
        return self.name.title()


class FeatureType(Enum):
    EXEMPLAR = "exemplar"

    def __str__(self):
        return self.name.title()


class StringMixin:
    @classmethod
    def from_str(cls, label):
        label = label.lower()
        label = label.rstrip("s")
        label = label.replace("_", " ")

        return cls(label)

    def to_filename(self):
        return self.value.replace(" ", "_")

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"

    def __str__(self):
        return self.value.title().replace(" ", "")


class Category(StringMixin, Enum):
    BIRD = "bird"
    FISH = "fish"
    MAMMAL = "mammal"


class Domain(StringMixin, Enum):
    ANIMAL = "animal"

    @property
    def members(self):
        if self == Domain.ANIMAL:
            return (Category.BIRD, Category.FISH, Category.MAMMAL)
