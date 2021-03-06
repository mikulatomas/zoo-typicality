# Zoo typicality dataset
Modified version of Zoo dataset which contains 73 exemplars (animals) with up to 18 boolean features. Dataset was extended by human typicality ratings for each exemplar in given category.

This dataset was used in:

> Belohlavek, R., Mikula, T.: Typicality: a formal concept analysis account (2021 - preprint).

## Exemplars
Each exemplar is member of one of the category (bird, fish and mammal).

| Category        | Count         | Exemplars  |
|:------------:|:-------------:|:---------- |
| *bird*       | 20            | ```chicken, crow, dove, duck, flamingo, gull, hawk, kiwi, lark, ostrich, parakeet, penguin, pheasant, rhea, skimmer, skua, sparrow, swan, vulture, wren``` |
| *fish*       | 13            | ```bass, carp, catfish, chub, dogfish, haddock, herring, pike, piranha, seahorse, sole, stingray, tuna``` |
| *mammal*     | 40            | ```aardvark, antelope, bear, boar, buffalo, calf, cavy, cheetah, deer, dolphin, elephant, fruitbat, giraffe, goat, gorilla, hamster, hare, leopard, lion, lynx, mink, mole, mongoose, opossum, oryx, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, seal, sealion, squirrel, vampire, vole, wallaby, wolf``` |

## Features
Each exemplar is defined by set of boolean features, category and it's name. Exemplar by feature matrix is avaliable in `data/features.csv` file.

| Type         | Features    |
|:------------:|:----------- |
| bool         | ```hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, tail, domestic, catsize, no legs, two legs, four legs``` |
| str          | ```exemplar, category``` |

## Typicality
Each exemplar was assessed on scale 1 (least typical) to 5 (most typical) by 242 respondents (136 were women, 106 were men). Mean typicality ratings are avaliable in `data/typicality ratings/` folder. The `original_responses.csv` file includes unprocessed responses from participants.

## Reference
Original dataset: https://archive.ics.uci.edu/ml/datasets/zoo

> Dua, D., Graff, C.: UCI Machine Learning Repository. University of California, Irvine, School of Information and Computer Sciences (2019). http://archive. ics.uci.edu/ml

### Modifications to the original data
* Exemplar `girl` was removed.
* Original numeric `legs` feature was converted to multiple boolean features (`no legs`, `two legs`, `four legs`).
* Original `type` feature was renamed as `category`.
* Because typicality ratings were gathered only for `bird`, `fish` and `mammal` category, other categories were removed.
