import re
import pathlib

import pandas as pd

from translation import en_cs_exemplars, en_cs_categories


values_translation = {
    "Muž": "man",
    "Žena": "woman",
    "Čeština": "CS",
    "Slovenština": "SK",
    "5 (nejvíce typické)": "5",
    "1 (nejméně typické)": "1",
}

dfs = [pd.read_csv(f_csv) for f_csv in pathlib.Path("raw").glob("*.csv")]
df = pd.concat(dfs).reset_index(drop=True)

df = df.replace(values_translation)

translation_animals_en_cs = en_cs_exemplars
translation_animals_cs_en = dict((v, k) for k, v in translation_animals_en_cs.items())

cs_en_categories = dict((v, k) for k, v in en_cs_categories.items())

column_translation = {
    "Časová značka": "timestamp",
    "Pohlaví": "sex",
    "Věk": "age",
    "Mateřský jazyk": "first language",
}

columns_types = {
    "timestamp": str,
    "sex": str,
    "first language": str,
    "age": int,
}

df_cs = df.rename(columns=column_translation)
df_cs = df_cs.astype(columns_types)

df_cs.to_csv(pathlib.Path("processed") / "typicality_cs.csv")

for column_name in df.columns:
    column_name_lower = column_name.lower()
    try:
        concept = re.search("(.*) \[(.*)\]", column_name_lower).group(1)
        animal = re.search("(.*) \[(.*)\]", column_name_lower).group(2)
    except:
        continue

    animal_en = translation_animals_cs_en.get(animal)
    concept_en = cs_en_categories.get(concept)
    column_translation[column_name] = f"{concept_en} [{animal_en}]"
    columns_types[f"{concept_en} [{animal_en}]"] = float

df_en = df.rename(columns=column_translation)
df_en = df_en.astype(columns_types)

df_en.to_csv(pathlib.Path("processed") / "typicality.csv")

df = pd.read_csv(pathlib.Path("processed") / "typicality.csv", index_col=0)

concepts = list(en_cs_categories.keys())

for concept in concepts:
    concept_df = df.filter(regex=f"^{concept} ", axis=1)

    concept_df.columns = [
        re.search(r"(.*)\[(.*)\]", name).group(2) for name in concept_df.columns
    ]

    typicality_df = concept_df.T
    typicality_df.columns = [f"respondent {col}" for col in typicality_df.columns]
    nonmissing = typicality_df.count(axis=1)
    typicality_df["std"] = concept_df.std()
    typicality_df["mean"] = concept_df.mean()
    typicality_df["nonmissing"] = nonmissing

    typicality_df.to_csv(
        pathlib.Path("processed") / f"{concept}_typicality_ratings.csv"
    )
