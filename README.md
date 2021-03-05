# Zoo typicality dataset
Modified version of Zoo dataset contains 73 exemplars and 18 boolean value features.

## Exemplars
Each exemplar is member of one of the class (bird, fish, mammal).

| Class        | Count         | Exemplars  |
| ------------ |:-------------:| ----------:|
| *bird*       | 20            | ```chicken, crow, dove, duck, flamingo, gull, hawk, kiwi, lark, ostrich, parakeet, penguin, pheasant, rhea, skimmer, skua, sparrow, swan, vulture, wren``` |
| *fish*       | 13            | ```bass, carp, catfish, chub, dogfish, haddock, herring, pike, piranha, seahorse, sole, stingray, tuna``` |
| *mammal*     | 40            | ```aardvark, antelope, bear, boar, buffalo, calf, cavy, cheetah, deer, dolphin, elephant, fruitbat, giraffe, goat, gorilla, hamster, hare, leopard, lion, lynx, mink, mole, mongoose, opossum, oryx, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, seal, sealion, squirrel, vampire, vole, wallaby, wolf``` |

## Features

`exemplar` (str), `hair` (bool), `feathers` (bool), `eggs` (bool), `milk` (bool), `airborne` (bool), `aquatic` (bool), `predator` (bool), `toothed` (bool), `backbone` (bool), `breathes` (bool), `venomous` (bool), `fins` (bool), `tail` (bool), `domestic` (bool), `catsize` (bool), `no legs` (bool), `two legs` (bool), `four legs` (bool), `class` (str)

## Original data
https://archive.ics.uci.edu/ml/datasets/zoo
```
Dua, D., Graff, C.: UCI Machine Learning Repository. University of California, Irvine, School of Information and Computer Sciences (2019). http://archive. ics.uci.edu/ml
```

## Modifications to the original data
* Exemplar `girl` was removed.
* Original numeric `legs` feature was converted into multiple bool features (`no legs`, `two legs`, `four legs`).
* Original `type` feature was renamed to `class`.
* Rest of the classes was removed, because typicality was gathered only for `bird`, `fish` and `mammal`.
