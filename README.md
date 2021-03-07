# Human typicality ratings for the Zoo dataset
This repository provides human typicality ratings for each exemplar from three categories (bird, fish, mammal) based on the original Zoo dataset (see below).

<img src="https://github.com/mikulatomas/zoo-typicality/raw/pre-publish/logo.png" width=500>

Human typicality ratings were used in:

> Belohlavek, R., Mikula, T.: Typicality: a formal concept analysis account (2021 - preprint).

## Zoo dataset
Original Zoo dataset [1] consists of 101 animals and 17 features. Each animal is member of one of the 7 categories (types).

Dataset can be downloaded here: https://archive.ics.uci.edu/ml/datasets/zoo.

## Selected categories
Bird, fish, mammal (type 1, 2, 4 in Zoo dataset) categories were selected for assessing typicality ratings. All exemplars for each category are listed in following table. Note that `girl` exemplar was omitted.

| Category        | Count         | Exemplars  |
|:------------:|:-------------:|:---------- |
| bird       | 20            | ```chicken, crow, dove, duck, flamingo, gull, hawk, kiwi, lark, ostrich, parakeet, penguin, pheasant, rhea, skimmer, skua, sparrow, swan, vulture, wren``` |
| fish       | 13            | ```bass, carp, catfish, chub, dogfish, haddock, herring, pike, piranha, seahorse, sole, stingray, tuna``` |
| mammal     | 40            | ```aardvark, antelope, bear, boar, buffalo, calf, cavy, cheetah, deer, dolphin, elephant, fruitbat, giraffe, goat, gorilla, hamster, hare, leopard, lion, lynx, mink, mole, mongoose, opossum, oryx, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, seal, sealion, squirrel, vampire, vole, wallaby, wolf``` |

## Typicality ratings
Each exemplar from selected categories was assessed on scale 1 (least typical) to 5 (most typical) by up to 242 respondents (136 were women, 106 were men). Respondents were allowed to skip unknown exemplars, so not all of the exemplars were assessed by all 242 respondents.

Mean typicality ratings for each exemplar are available in `data/typicality ratings/` folder. Alongside mean value, sample standard deviation (std) and number of non-missing human assessment (nonmissing) was calculated. The `original_responses.csv` file includes unprocessed responses from participants.

## Features
For convenient experiments, subset of original Zoo dataset is available as attachment to this dataset in `data/features/mini_zoo.csv`.

| Type         | Features    |
|:------------:|:----------- |
| bool         | ```hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, tail, domestic, catsize, no legs, two legs, four legs``` |
| str          | ```exemplar, category``` |

List of modifications to the original Zoo dataset:
* Original numeric `legs` feature was converted to multiple boolean features (`no legs`, `two legs`, `four legs`).
* As mentioned, girl exemplar was removed.
* Original `animal name` feature was renamed as `exemplar`.
* Original `type` feature was renamed as `category` and original numeric values (1, 2, 4) are transformed to strings (bird, fish, mammal).
* Exemplars from other categories are removed.

## References
> [1] Dua, D., Graff, C.: UCI Machine Learning Repository. University of California, Irvine, School of Information and Computer Sciences (2019). http://archive. ics.uci.edu/ml
