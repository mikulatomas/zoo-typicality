import typing
import pkg_resources
import pathlib

from .loaders import load_features, load_exemplar_judgements
from .enums import FeatureType, Language
from .constants import DATASET_NAME


class MiniZooConcepts:
    def __init__(
        self,
        language: Language = Language.ENGLISH,
        dataset_dir: typing.Optional[pathlib.Path] = None,
    ) -> None:
        self.language = language

        if dataset_dir is None:
            self.dataset_dir = pathlib.Path(
                pkg_resources.resource_filename(__name__, "data")
            )
        else:
            self.dataset_dir = dataset_dir
        
        self.name = DATASET_NAME

        self.features = {feature_type: load_features(
            self.dataset_dir / self.language.value, feature_type
        ) for feature_type in FeatureType}

        self.exemplar_judgements = load_exemplar_judgements(
            self.dataset_dir / self.language.value
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.dataset_dir}, {self.language})"
