# Zoo typicality dataset
Modified version of Zoo dataset which contains 73 exemplars (animals) with up to 18 boolean features. Dataset was extended by human typicality ratings for each exemplar in given category.

## Exemplars
Each exemplar is member of one of the class (bird, fish, mammal).

| Category        | Count         | Exemplars  |
|:------------:|:-------------:|:---------- |
| *bird*       | 20            | ```chicken, crow, dove, duck, flamingo, gull, hawk, kiwi, lark, ostrich, parakeet, penguin, pheasant, rhea, skimmer, skua, sparrow, swan, vulture, wren``` |
| *fish*       | 13            | ```bass, carp, catfish, chub, dogfish, haddock, herring, pike, piranha, seahorse, sole, stingray, tuna``` |
| *mammal*     | 40            | ```aardvark, antelope, bear, boar, buffalo, calf, cavy, cheetah, deer, dolphin, elephant, fruitbat, giraffe, goat, gorilla, hamster, hare, leopard, lion, lynx, mink, mole, mongoose, opossum, oryx, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, seal, sealion, squirrel, vampire, vole, wallaby, wolf``` |

## Features
Each exemplar is defined by set of boolean features, category and it's name.

| Type         | Features    |
|:------------:|:----------- |
| bool         | ```hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, tail, domestic, catsize, no legs, two legs, four legs``` |
| str          | ```exemplar, category``` |

## Typicality
For each exemplar (in given category) typicality rating was obtained. Each exemplar was assessed by up to 242 respondents (136 were women, 106 were men). Typicality ratings calcualted as mean value of given responses are avaliable in `data/typicality ratings/` folder. The `original_responses.csv` file includes unprocessed responses from participants.

## Original data
https://archive.ics.uci.edu/ml/datasets/zoo

```
Dua, D., Graff, C.: UCI Machine Learning Repository. University of California, Irvine, School of Information and Computer Sciences (2019). http://archive. ics.uci.edu/ml
```

## Modifications to the original data
* Exemplar `girl` was removed.
* Original numeric `legs` feature was converted into multiple bool features (`no legs`, `two legs`, `four legs`).
* Original `type` feature was renamed to `category`.
* Because typicality ratings were gathered only for `bird`, `fish` and `mammal` category, other categories were removed.
