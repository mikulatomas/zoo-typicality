import os

from dataclasses import dataclass

import pandas as pd
from glob import glob

from .enums import Category, Domain, FeatureType
from .constants import *


@dataclass
class FeaturesData:
    feature_matrix: pd.DataFrame
    feature_type: FeatureType
    name: str

    @property
    def exemplars(self):
        return tuple(self.feature_matrix.index)

    @property
    def attributes(self):
        return tuple(self.feature_matrix.columns)


@dataclass
class FeaturesDomainData(FeaturesData):
    domain: Domain

    def __repr__(self):
        return f"{self.__class__.__name__}({self.domain}, {self.feature_type})"


@dataclass
class FeaturesCategoryData(FeaturesData):
    category: Category

    def __repr__(self):
        return f"{self.__class__.__name__}({self.category}, {self.feature_type})"


@dataclass
class ExemplarJudgementsData:
    type: str
    category: Category
    data: pd.DataFrame
    name: str

    def __repr__(self):
        return f"{self.__class__.__name__}({self.type}, {self.category})"


@dataclass
class Features:
    domain: dict
    category: dict
    feature_type: FeatureType

    def __repr__(self):
        return f"{self.__class__.__name__}({self.feature_type})"


@dataclass
class ExemplarJudgements:
    typicality_ratings: dict

    def __repr__(self):
        return f"{self.__class__.__name__}()"


def load_exemplar_judgements(dataset_folder):
    judgments = [
        "typicality_ratings",
    ]

    loaded_judgments = []

    for judgment_name in judgments:
        judgment_folder = os.path.join(
            dataset_folder, EXEMPLAR_JUDGMENTS_FOLDER, judgment_name
        )

        judgment_dict = {}

        for file in glob(os.path.join(judgment_folder, "*.csv")):
            category = Category.from_str(
                os.path.basename(file).replace(f"_{judgment_name}.csv", "")
            )

            df = pd.read_csv(file, index_col=0)

            judgment_name_title = (
                judgment_name.replace("_", " ").title().replace(" ", "")
            )

            judgment_dict[category] = ExemplarJudgementsData(
                type=judgment_name,
                category=category,
                data=df,
                name=f"{DATASET_NAME}{category}{judgment_name_title}",
            )

        loaded_judgments.append(judgment_dict)

    return ExemplarJudgements(*loaded_judgments)


def load_features(dataset_folder, feature_type):
    type_folder = EXEMPLAR_FEATURES_FOLDER

    folder = os.path.join(
        dataset_folder, EXEMPLAR_FEATURES_JUDGEMENTS_FOLDER, type_folder
    )

    domain = load_domain_features(folder, feature_type)
    category = load_category_features(folder, feature_type)

    return Features(domain=domain, category=category, feature_type=feature_type)


def load_domain_features(source_folder, feature_type):
    domains = {}

    for domain_folder in glob(os.path.join(source_folder, "domains", "*")):
        domain = Domain.from_str(os.path.basename(domain_folder))

        feature_matrix = pd.read_csv(
            glob(os.path.join(domain_folder, "*.csv"))[0], index_col=0
        )

        name = f"{DATASET_NAME}{domain}{feature_type.value.title()}"

        domains[domain] = FeaturesDomainData(
            feature_matrix=feature_matrix,
            feature_type=feature_type,
            domain=domain,
            name=name,
        )

    return domains


def load_category_features(source_folder, feature_type):
    categories = {}

    for category_folder in glob(os.path.join(source_folder, "categories", "*")):
        category = Category.from_str(os.path.basename(category_folder))

        feature_matrix = pd.read_csv(
            glob(os.path.join(category_folder, "*.csv"))[0], index_col=0
        )

        name = f"{DATASET_NAME}{category}{feature_type.value.title()}"

        categories[category] = FeaturesCategoryData(
            feature_matrix=feature_matrix,
            feature_type=feature_type,
            category=category,
            name=name,
        )

    return categories
