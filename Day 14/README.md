# Day 14: Space Stoichiometry
https://adventofcode.com/2019/day/14

## Part 1
https://adventofcode.com/2019/day/14#part1

### Description
As you approach the rings of Saturn, your ship's **low fuel** indicator turns on. There isn't any fuel here, but the rings have plenty of raw material. Perhaps your ship's Inter-Stellar Refinery Union brand **nanofactory** can turn these raw materials into fuel.

You ask the nanofactory to produce a list of the **reactions** it can perform that are relevant to this process (your puzzle input). Every reaction turns some quantities of specific **input chemicals** into some quantity of an **output chemical**. Almost every **chemical** is produced by exactly one reaction; the only exception, `ORE`, is the raw material input to the entire process and is not produced by a reaction.

You just need to know how much **`ORE`** you'll need to collect before you can produce one unit of **`FUEL`**.

Each reaction gives specific quantities for its inputs and output; reactions cannot be partially run, so only whole integer multiples of these quantities can be used. (It's okay to have leftover chemicals when you're done, though.) For example, the reaction `1 A, 2 B, 3 C => 2 D` means that exactly 2 units of chemical `D` can be produced by consuming exactly 1 `A`, 2 `B` and 3 `C`. You can run the full reaction as many times as necessary; for example, you could produce 10 `D` by consuming 5 `A`, 10 `B`, and 15 `C`.

Suppose your nanofactory produces the following list of reactions:
```
10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL
```

The first two reactions use only `ORE` as inputs; they indicate that you can produce as much of chemical A as you want (in increments of 10 units, each 10 costing 10 `ORE`) and as much of chemical `B` as you want (each costing 1 `ORE`). To produce 1 `FUEL`, a total of **31** `ORE` is required: 1 `ORE` to produce 1 `B`, then 30 more `ORE` to produce the 7 + 7 + 7 + 7 = 28 `A` (with 2 extra `A` wasted) required in the reactions to convert the `B` into `C`, C into `D`, `D` into `E`, and finally `E` into `FUEL`. (30 `A` is produced because its reaction requires that it is created in increments of 10.)

Or, suppose you have the following list of reactions:
```
9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL
```

The above list of reactions requires **165** `ORE` to produce 1 `FUEL`:
* Consume 45 `ORE` to produce 10 `A`.
* Consume 64 `ORE` to produce 24 `B`.
* Consume 56 `ORE` to produce 40 `C`.
* Consume 6 `A`, 8 `B` to produce 2 `AB`.
* Consume 15 `B`, 21 `C` to produce 3 `BC`.
* Consume 16 `C`, 4 `A` to produce 4 `CA`.
* Consume 2 `AB`, 3 `BC`, 4 `CA` to produce 1 `FUEL`.

Here are some larger examples:
* **13312** `ORE` for 1 `FUEL`:
```
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
```
* **180697** `ORE` for 1 `FUEL`:
```
2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF
```
* **2210736** `ORE` for 1 `FUEL`:
```
171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX
```

Given the list of reactions in your puzzle input, **what is the minimum amount of `ORE` required to produce exactly 1 `FUEL`?**

### Solution
To solve this problem, we get needed chemical **from `FUEL` until `ORE`**. I use one dict to store **unused chemicals** and one list that acts as **queue**. The dict starts **empty** (we do not have any unused chemical) and list starts with `[Fuel, 1]` (we calculate from `FUEL` to `ORE`). We use a loop with the following phases:
1) Get next chemical to generate from list and required units.
2) Try to reduce required units with unused chemicals in dict (if there are unused units for current chemical).
3) After the reduction, if required units are `0`, repeat loop from 1. Otherwise, go 4.
4) Get reaction for current chemical (input chemicals and required units for each one, and generated units).
5) Compute how many times it is necessary to apply the rule (`[required units]/[generated units]`). For example, if we need 5 units and the rule generates 3, it is necessary to apply the rule twice.
6) Store unused units in the dict of unused chemicals.
7) For each input chemical needed to generate current chemical, we add to queue each one with its corresponding required units. If input chemical is `ORE`, we add the number of required units to solution instead of add to queue.

To understand this method, let's solve example 3 (step by step):
```
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
```

* Cycle 1:
```
sol = 0
dict = {}
queue = [['FUEL', 1]]
```
  1) Get next chemical and required units: `['FUEL', 1]`
  2) Try to reduce required units: dict is empty, so we cannot reduce it
  3) Required units (1) is not 0, so we continue cycle.
  4) Get reaction for `'FUEL'` (inputs and required units): `[1,[44 'XJWVT', 5 'KHKGT', 1 'QDVJ', 29 'NZVS', 9 'GPVTF', 48 'HKGWZ']]`
  5) Calculate times to apply the rule: `1/1 = 1`
  6) Store unused units: `1-1 = 0` (nothing is stored)
  7) Add input chemicals to queue: None is `'ORE'` and rule is applied once, so we store `['XJWVT',44]`, `['KHKGT',5]`, `['QDVJ',1]`, `['NZVS',29]`, `['GPVTF',9]`, `['HKGWZ',48]`.

* Cycle 2:
```
sol = 0
dict = {}
queue = [['XJWVT',44], ['KHKGT',5], ['QDVJ',1], ['NZVS',29], ['GPVTF',9], ['HKGWZ',48]]
```
  1) Get next chemical and required units: `['XJWVT',44]`
  2) Try to reduce required units: dict is empty, so we cannot reduce it
  3) Required units (44) is not 0, so we continue cycle.
  4) Get reaction for `'XJWVT'` (inputs and required units): `[2,[7 DCFZ, 7 PSHF]]`
  5) Calculate times to apply the rule: `44/2 = 22`
  6) Store unused units: `(22*2)-44 = 0` (nothing is stored)
  7) Add input chemicals to queue: None is `'ORE'` and rule is applied once, so we store `['DCFZ',(7*22=154)]`, `['PSHF',(7*22=154)]`.

* Cycle 3:
```
sol = 0
dict = {}
queue = [['KHKGT',5], ['QDVJ',1], ['NZVS',29], ['GPVTF',9], ['HKGWZ',48], ['DCFZ',154], ['PSHF',154]]
```
  1) Get next chemical and required units: `['KHKGT', 5]`
  2) Try to reduce required units: dict is empty, so we cannot reduce it
  3) Required units (5) is not 0, so we continue cycle.
  4) Get reaction for `'KHKGT'` (inputs and required units): `[8,[3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF]]`
  5) Calculate times to apply the rule: `5/8 = 0.625 => 1`
  6) Store unused units: `8-5 = 3` (`3 'KHKGT'` is stored)
  7) Add input chemicals to queue: None is `'ORE'` and rule is applied once, so we store `['DCFZ',3]`, `['NZVS',7]`, `['HKGWZ',5]`, `['PSHF',10]`.

* Cycle 4:
```
sol = 0
dict = {"KHKGT": 3}
queue = [['QDVJ',1], ['NZVS',29], ['GPVTF',9], ['HKGWZ',48], ['DCFZ',154], ['PSHF',154], ['DCFZ',3], ['NZVS',7], ['HKGWZ',5], ['PSHF',10]]
```
  1) Get next chemical and required units: `['QDVJ',1]`
  2) Try to reduce required units: there are no `'QDVJ'` in dict, so we cannot reduce it
  3) Required units (1) is not 0, so we continue cycle.
  4) Get reaction for `'QDVJ'` (inputs and required units): `[9,[12 HKGWZ, 1 GPVTF, 8 PSHF]]`
  5) Calculate times to apply the rule: `1/9 = 0.1 => 1`
  6) Store unused units: `9-1 = 8` (`8 'QDVJ'` is stored)
  7) Add input chemicals to queue: None is `'ORE'` and rule is applied once, so we store `['HKGWZ',12]`, `['GPVTF',1]`, `['PSHF',8]`.

* Cycle 5:
```
sol = 0
dict = {"KHKGT": 3, "QDVJ": 8}
queue = [['NZVS',29], ['GPVTF',9], ['HKGWZ',48], ['DCFZ',154], ['PSHF',154], ['DCFZ',3], ['NZVS',7], ['HKGWZ',5], ['PSHF',10], ['HKGWZ',12], ['GPVTF',1], ['PSHF',8]]
```
  1) Get next chemical and required units: `['NZVS',29]`
  2) Try to reduce required units: there are no `'NZVS'` in dict, so we cannot reduce it
  3) Required units (29) is not 0, so we continue cycle.
  4) Get reaction for `'NZVS'` (inputs and required units): `[5,[157 ORE]]`
  5) Calculate times to apply the rule: `29/5 = 5.8 => 6`
  6) Store unused units: `(5*6)-29 = 1` (`1 'NZVS'` is stored)
  7) Add input chemicals to queue: Input is `'ORE'`, so we add `157*6 = 942` to sol.

* Cycle 6:
```
sol = 942
dict = {"KHKGT": 3, "QDVJ": 8, "NZVS": 1}
queue = [['GPVTF',9], ['HKGWZ',48], ['DCFZ',154], ['PSHF',154], ['DCFZ',3], ['NZVS',7], ['HKGWZ',5], ['PSHF',10], ['HKGWZ',12], ['GPVTF',1], ['PSHF',8]]
```
  1) Get next chemical and required units: `['GPVTF',9]`
  2) Try to reduce required units: there are no `'GPVTF'` in dict, so we cannot reduce it
  3) Required units (9) is not 0, so we continue cycle.
  4) Get reaction for `'GPVTF'` (inputs and required units): `[2,[165 ORE]]`
  5) Calculate times to apply the rule: `9/2 = 4.5 => 5`
  6) Store unused units: `(2*5)-9 = 1` (`1 'GPVTF'` is stored)
  7) Add input chemicals to queue: Input is `'ORE'`, so we add `165*5 = 825` to sol.

* Cycle 7:
```
sol = 1767
dict = {"KHKGT": 3, "QDVJ": 8, "NZVS": 1, "GPVTF": 1}
queue = [['HKGWZ',48], ['DCFZ',154], ['PSHF',154], ['DCFZ',3], ['NZVS',7], ['HKGWZ',5], ['PSHF',10], ['HKGWZ',12], ['GPVTF',1], ['PSHF',8]]
```
  1) Get next chemical and required units: `['HKGWZ',48]`
  2) Try to reduce required units: there are no `'HKGWZ'` in dict, so we cannot reduce it
  3) Required units (48) is not 0, so we continue cycle.
  4) Get reaction for `'HKGWZ'` (inputs and required units): `[5,[177 ORE]]`
  5) Calculate times to apply the rule: `48/5 = 9.6 => 10`
  6) Store unused units: `(5*10)-48 = 2` (`2 'HKGWZ'` is stored)
  7) Add input chemicals to queue: Input is `'ORE'`, so we add `177*10 = 1770` to sol.

* Cycle 8:
```
sol = 3537
dict = {"KHKGT": 3, "QDVJ": 8, "NZVS": 1, "GPVTF": 1, "HKGWZ": 2}
queue = [['DCFZ',154], ['PSHF',154], ['DCFZ',3], ['NZVS',7], ['HKGWZ',5], ['PSHF',10], ['HKGWZ',12], ['GPVTF',1], ['PSHF',8]]
```
  1) Get next chemical and required units: `['DCFZ',154]`
  2) Try to reduce required units: there are no `'DCFZ'` in dict, so we cannot reduce it
  3) Required units (154) is not 0, so we continue cycle.
  4) Get reaction for `'DCFZ'` (inputs and required units): `[6,[165 ORE]]`
  5) Calculate times to apply the rule: `154/6 = 25.6 => 26`
  6) Store unused units: `(6*26)-154 = 2` (`2 'DCFZ'` is stored)
  7) Add input chemicals to queue: Input is `'ORE'`, so we add `165*26 = 4290` to sol.

* Cycle 9:
```
sol = 7827
dict = {"KHKGT": 3, "QDVJ": 8, "NZVS": 1, "GPVTF": 1, "HKGWZ": 2, "DCFZ": 2}
queue = [['PSHF',154], ['DCFZ',3], ['NZVS',7], ['HKGWZ',5], ['PSHF',10], ['HKGWZ',12], ['GPVTF',1], ['PSHF',8]]
```
  1) Get next chemical and required units: `['PSHF',154]`
  2) Try to reduce required units: there are no `'PSHF'` in dict, so we cannot reduce it
  3) Required units (154) is not 0, so we continue cycle.
  4) Get reaction for `'PSHF'` (inputs and required units): `[7,[179 ORE]]`
  5) Calculate times to apply the rule: `154/7 = 22`
  6) Store unused units: `(7*22)-154 = 0` (nothing is stored)
  7) Add input chemicals to queue: Input is `'ORE'`, so we add `179*22 = 3938` to sol.

* Cycle 10:
```
sol = 11765
dict = {"KHKGT": 3, "QDVJ": 8, "NZVS": 1, "GPVTF": 1, "HKGWZ": 2, "DCFZ": 2}
queue = [['DCFZ',3], ['NZVS',7], ['HKGWZ',5], ['PSHF',10], ['HKGWZ',12], ['GPVTF',1], ['PSHF',8]]
```
  1) Get next chemical and required units: `['DCFZ',3]`
  2) Try to reduce required units: there are `'DCFZ'` in dict, so we reduce it to 3-2 = 1
  3) Required units (1) is not 0, so we continue cycle.
  4) Get reaction for `'DCFZ'` (inputs and required units): `[6,[165 ORE]]`
  5) Calculate times to apply the rule: `1/6 = 0.16 => 1`
  6) Store unused units: `(6*1)-1 = 5` (`5 'DCFZ'` is stored)
  7) Add input chemicals to queue: Input is `'ORE'`, so we add `165*1 = 165` to sol.

* Cycle 11:
```
sol = 11930
dict = {"KHKGT": 3, "QDVJ": 8, "NZVS": 1, "GPVTF": 1, "HKGWZ": 2, "DCFZ": 5}
queue = [['NZVS',7], ['HKGWZ',5], ['PSHF',10], ['HKGWZ',12], ['GPVTF',1], ['PSHF',8]]
```
  1) Get next chemical and required units: `['NZVS',7]`
  2) Try to reduce required units: there are `'NZVS'` in dict, so we reduce it to 7-1 = 6
  3) Required units (6) is not 0, so we continue cycle.
  4) Get reaction for `'NZVS'` (inputs and required units): `[5,[157 ORE]]`
  5) Calculate times to apply the rule: `6/5 = 1.2 => 2`
  6) Store unused units: `(5*2)-6 = 4` (`4 'NZVS'` is stored)
  7) Add input chemicals to queue: Input is `'ORE'`, so we add `157*2 = 314` to sol.

* Cycle 12:
```
sol = 12244
dict = {"KHKGT": 3, "QDVJ": 8, "NZVS": 4, "GPVTF": 1, "HKGWZ": 2, "DCFZ": 5}
queue = [['HKGWZ',5], ['PSHF',10], ['HKGWZ',12], ['GPVTF',1], ['PSHF',8]]
```
  1) Get next chemical and required units: `['HKGWZ',5]`
  2) Try to reduce required units: there are `'HKGWZ'` in dict, so we reduce it to 5-2 = 3
  3) Required units (3) is not 0, so we continue cycle.
  4) Get reaction for `'HKGWZ'` (inputs and required units): `[5,[177 ORE]]`
  5) Calculate times to apply the rule: `3/5 = 0.6 => 1`
  6) Store unused units: `(5*1)-3 = 2` (`2 'HKGWZ'` is stored)
  7) Add input chemicals to queue: Input is `'ORE'`, so we add `177*1 = 177` to sol.

* Cycle 13:
```
sol = 12421
dict = {"KHKGT": 3, "QDVJ": 8, "NZVS": 4, "GPVTF": 1, "HKGWZ": 2, "DCFZ": 5}
queue = [['PSHF',10], ['HKGWZ',12], ['GPVTF',1], ['PSHF',8]]
```
  1) Get next chemical and required units: `['PSHF',10]`
  2) Try to reduce required units: there are no `'PSHF'` in dict, so we cannot reduce it
  3) Required units (10) is not 0, so we continue cycle.
  4) Get reaction for `'PSHF'` (inputs and required units): `[7,[179 ORE]]`
  5) Calculate times to apply the rule: `10/7 = 1.43 => 2`
  6) Store unused units: `(7*2)-10 = 4` (`4 'PSHF'` is stored)
  7) Add input chemicals to queue: Input is `'ORE'`, so we add `179*2 = 358` to sol.

* Cycle 14:
```
sol = 12779
dict = {"KHKGT": 3, "QDVJ": 8, "NZVS": 4, "GPVTF": 1, "HKGWZ": 2, "DCFZ": 5, "PSHF": 4}
queue = [['HKGWZ',12], ['GPVTF',1], ['PSHF',8]]
```
  1) Get next chemical and required units: `['HKGWZ',12]`
  2) Try to reduce required units: there are `'HKGWZ'` in dict, so we reduce it to 12-2 = 10
  3) Required units (10) is not 0, so we continue cycle.
  4) Get reaction for `'HKGWZ'` (inputs and required units): `[5,[177 ORE]]`
  5) Calculate times to apply the rule: `10/5 = 2`
  6) Store unused units: `(5*2)-10 = 0` (nothing is stored)
  7) Add input chemicals to queue: Input is `'ORE'`, so we add `177*2 = 354` to sol.

* Cycle 15:
```
sol = 13133
dict = {"KHKGT": 3, "QDVJ": 8, "NZVS": 4, "GPVTF": 1, "DCFZ": 5, "PSHF": 4}
queue = [['GPVTF',1], ['PSHF',8]]
```
  1) Get next chemical and required units: `['GPVTF',1]`
  2) Try to reduce required units: there are `'GPVTF'` in dict, so we reduce it to 1-1 = 0
  3) Required units (0) is 0, so stop this cycle cycle.

* Cycle 16:
```
sol = 13133
dict = {"KHKGT": 3, "QDVJ": 8, "NZVS": 4, "DCFZ": 5, "PSHF": 4}
queue = [['PSHF',8]]
```
  1) Get next chemical and required units: `['PSHF',8]`
  2) Try to reduce required units: there are `'PSHF'` in dict, so we reduce it to 8-4 = 4
  3) Required units (4) is not 0, so we continue cycle.
  4) Get reaction for `'PSHF'` (inputs and required units): `[7,[179 ORE]]`
  5) Calculate times to apply the rule: `4/7 = 0.57 => 1`
  6) Store unused units: `(7*1)-4 = 0` (`3 'PSHF'` is stored)
  7) Add input chemicals to queue: Input is `'ORE'`, so we add `179*1 = 179` to sol.

* Final state:
```
sol = 13312
dict = {"KHKGT": 3, "QDVJ": 8, "NZVS": 4, "DCFZ": 5, "PSHF": 3}
queue = []
```

Result for my input data is: `483766`


## Part 2
https://adventofcode.com/2019/day/14#part2

### Description
After collecting `ORE` for a while, you check your cargo hold: **1 trillion** (**1000000000000**) units of `ORE`.

**With that much ore**, given the examples above:
* The 13312 `ORE`-per-`FUEL` example could produce **82892753** `FUEL`.
* The 180697 `ORE`-per-`FUEL` example could produce **5586022** `FUEL`.
* The 2210736 `ORE`-per-`FUEL` example could produce **460664** `FUEL`.

Given 1 trillion `ORE`, **what is the maximum amount of `FUEL` you can produce?**

### Solution
In part 1 we calculated required `ORE` to generate 1 `FUEL`. In part 2 we have to **calculate how many `FUEL`s can be generated with 1 trillion of `ORE`**.

To solve this part, we can use previous code. We can do a loop to generate `FUEL` one by one, but this is **too computationally expensive**. For this reason we need another strategy. In my case, I generate **blocks of `FUEL` of a specific size** (in my case `1000`). We generate `FUEL`s in blocks of `1000` units and, **when a block cost more `ORE` than we have, block size is reduced** to `1`.

**You must have in account that unused chemicals from one block are used in the next execution.**

Result for my input data is: `3061522`