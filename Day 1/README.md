# Day 1: The Tyranny of the Rocket Equation
https://adventofcode.com/2019/day/1

## Part 1
https://adventofcode.com/2019/day/1#part1

### Description
Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from **fifty stars**.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given **module** is based on its **mass**. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:
* For a mass of `12`, divide by 3 and round down to get `4`, then subtract 2 to get `2`.
* For a mass of `14`, dividing by 3 and rounding down still yields `4`, so the fuel required is also `2`.
* For a mass of `1969`, the fuel required is `654`.
* For a mass of `100756`, the fuel required is `33583`.

The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

**What is the sum of the fuel requirements** for all of the modules on your spacecraft (input.data)?

### Solution
General formula for this puzzle is **fuel_required=round_down(mass/3)-2**

My input values are in input.data

First I compute individual fuel requirement for each module's mass:
* Fuel requirements for a module with 130541 of mass: 43511.0
* Fuel requirements for a module with 69856 of mass: 23283.0
* Fuel requirements for a module with 104618 of mass: 34870.0
* Fuel requirements for a module with 149406 of mass: 49800.0
* Fuel requirements for a module with 64500 of mass: 21498.0
* Fuel requirements for a module with 128553 of mass: 42849.0
* Fuel requirements for a module with 94958 of mass: 31650.0
* Fuel requirements for a module with 104788 of mass: 34927.0
* Fuel requirements for a module with 87642 of mass: 29212.0
* Fuel requirements for a module with 60597 of mass: 20197.0
* Fuel requirements for a module with 142981 of mass: 47658.0
* Fuel requirements for a module with 132940 of mass: 44311.0
* Fuel requirements for a module with 64860 of mass: 21618.0
* Fuel requirements for a module with 122199 of mass: 40731.0
* Fuel requirements for a module with 131528 of mass: 43840.0
* Fuel requirements for a module with 84879 of mass: 28291.0
* Fuel requirements for a module with 144729 of mass: 48241.0
* Fuel requirements for a module with 139907 of mass: 46633.0
* Fuel requirements for a module with 147856 of mass: 49283.0
* Fuel requirements for a module with 66258 of mass: 22084.0
* Fuel requirements for a module with 95890 of mass: 31961.0
* Fuel requirements for a module with 115399 of mass: 38464.0
* Fuel requirements for a module with 106239 of mass: 35411.0
* Fuel requirements for a module with 126841 of mass: 42278.0
* Fuel requirements for a module with 59689 of mass: 19894.0
* Fuel requirements for a module with 146878 of mass: 48957.0
* Fuel requirements for a module with 105262 of mass: 35085.0
* Fuel requirements for a module with 137079 of mass: 45691.0
* Fuel requirements for a module with 145130 of mass: 48374.0
* Fuel requirements for a module with 114767 of mass: 38253.0
* Fuel requirements for a module with 94900 of mass: 31631.0
* Fuel requirements for a module with 64349 of mass: 21447.0
* Fuel requirements for a module with 105456 of mass: 35150.0
* Fuel requirements for a module with 59491 of mass: 19828.0
* Fuel requirements for a module with 79265 of mass: 26419.0
* Fuel requirements for a module with 89321 of mass: 29771.0
* Fuel requirements for a module with 62254 of mass: 20749.0
* Fuel requirements for a module with 106996 of mass: 35663.0
* Fuel requirements for a module with 107612 of mass: 35868.0
* Fuel requirements for a module with 71451 of mass: 23815.0
* Fuel requirements for a module with 138032 of mass: 46008.0
* Fuel requirements for a module with 137610 of mass: 45868.0
* Fuel requirements for a module with 52157 of mass: 17383.0
* Fuel requirements for a module with 68712 of mass: 22902.0
* Fuel requirements for a module with 134770 of mass: 44921.0
* Fuel requirements for a module with 111493 of mass: 37162.0
* Fuel requirements for a module with 50370 of mass: 16788.0
* Fuel requirements for a module with 91088 of mass: 30360.0
* Fuel requirements for a module with 149756 of mass: 49916.0
* Fuel requirements for a module with 51638 of mass: 17210.0
* Fuel requirements for a module with 110641 of mass: 36878.0
* Fuel requirements for a module with 60113 of mass: 20035.0
* Fuel requirements for a module with 54732 of mass: 18242.0
* Fuel requirements for a module with 86907 of mass: 28967.0
* Fuel requirements for a module with 73037 of mass: 24343.0
* Fuel requirements for a module with 111831 of mass: 37275.0
* Fuel requirements for a module with 116378 of mass: 38790.0
* Fuel requirements for a module with 93493 of mass: 31162.0
* Fuel requirements for a module with 55956 of mass: 18650.0
* Fuel requirements for a module with 111018 of mass: 37004.0
* Fuel requirements for a module with 99771 of mass: 33255.0
* Fuel requirements for a module with 65224 of mass: 21739.0
* Fuel requirements for a module with 149852 of mass: 49948.0
* Fuel requirements for a module with 97464 of mass: 32486.0
* Fuel requirements for a module with 148596 of mass: 49530.0
* Fuel requirements for a module with 140102 of mass: 46698.0
* Fuel requirements for a module with 81222 of mass: 27072.0
* Fuel requirements for a module with 106843 of mass: 35612.0
* Fuel requirements for a module with 61575 of mass: 20523.0
* Fuel requirements for a module with 112180 of mass: 37391.0
* Fuel requirements for a module with 124277 of mass: 41423.0
* Fuel requirements for a module with 59315 of mass: 19769.0
* Fuel requirements for a module with 101347 of mass: 33780.0
* Fuel requirements for a module with 141260 of mass: 47084.0
* Fuel requirements for a module with 90253 of mass: 30082.0
* Fuel requirements for a module with 87946 of mass: 29313.0
* Fuel requirements for a module with 55455 of mass: 18483.0
* Fuel requirements for a module with 115978 of mass: 38657.0
* Fuel requirements for a module with 51255 of mass: 17083.0
* Fuel requirements for a module with 149617 of mass: 49870.0
* Fuel requirements for a module with 77484 of mass: 25826.0
* Fuel requirements for a module with 133499 of mass: 44497.0
* Fuel requirements for a module with 128627 of mass: 42873.0
* Fuel requirements for a module with 75777 of mass: 25257.0
* Fuel requirements for a module with 135748 of mass: 45247.0
* Fuel requirements for a module with 87630 of mass: 29208.0
* Fuel requirements for a module with 86834 of mass: 28942.0
* Fuel requirements for a module with 145664 of mass: 48552.0
* Fuel requirements for a module with 86360 of mass: 28784.0
* Fuel requirements for a module with 139511 of mass: 46501.0
* Fuel requirements for a module with 60064 of mass: 20019.0
* Fuel requirements for a module with 106100 of mass: 35364.0
* Fuel requirements for a module with 123539 of mass: 41177.0
* Fuel requirements for a module with 115732 of mass: 38575.0
* Fuel requirements for a module with 107666 of mass: 35886.0
* Fuel requirements for a module with 89177 of mass: 29723.0
* Fuel requirements for a module with 82419 of mass: 27471.0
* Fuel requirements for a module with 98712 of mass: 32902.0
* Fuel requirements for a module with 148947 of mass: 49647.0
* Fuel requirements for a module with 50931 of mass: 16975.0

Final solution is the sum of all previous values: `3382284`

## Part 2

https://adventofcode.com/2019/day/1#part2

### Description
During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence. Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel **also** requires fuel, and **that** fuel requires fuel, and so on. Any mass that would require **negative fuel** should instead be treated as if it requires **zero fuel**; the remaining mass, if any, is instead handled by **wishing really hard**, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:
* A module of mass `14` requires `2` fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is `0`, which would call for a negative fuel), so the total fuel required is still just `2`.
* At first, a module of mass `1969` requires `654` fuel. Then, this fuel requires `216` more fuel (`654 / 3 - 2`). `216` then requires `70` more fuel, which requires `21` fuel, which requires `5` fuel, which requires no further fuel. So, the total fuel required for a module of mass `1969` is `654 + 216 + 70 + 21 + 5 = 966`.
* The fuel required by a module of mass `100756` and its fuel is: `33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346`.

**What is the sum of the fuel requirements** for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)

### Solution
In this case I use previous formula, but now a while loop is included to repeat formula until the mass is less or equal to zero.

My input values are in input.data

First I compute individual fuel requirement for each module's mass (taking into account the mass of the added fuel):
* Fuel requirements for a module with 130541 of mass: 65236.0
* Fuel requirements for a module with 69856 of mass: 34896.0
* Fuel requirements for a module with 104618 of mass: 52275.0
* Fuel requirements for a module with 149406 of mass: 74669.0
* Fuel requirements for a module with 64500 of mass: 32220.0
* Fuel requirements for a module with 128553 of mass: 64245.0
* Fuel requirements for a module with 94958 of mass: 47447.0
* Fuel requirements for a module with 104788 of mass: 52361.0
* Fuel requirements for a module with 87642 of mass: 43791.0
* Fuel requirements for a module with 60597 of mass: 30269.0
* Fuel requirements for a module with 142981 of mass: 71458.0
* Fuel requirements for a module with 132940 of mass: 66437.0
* Fuel requirements for a module with 64860 of mass: 32398.0
* Fuel requirements for a module with 122199 of mass: 61067.0
* Fuel requirements for a module with 131528 of mass: 65731.0
* Fuel requirements for a module with 84879 of mass: 42407.0
* Fuel requirements for a module with 144729 of mass: 72332.0
* Fuel requirements for a module with 139907 of mass: 69919.0
* Fuel requirements for a module with 147856 of mass: 73894.0
* Fuel requirements for a module with 66258 of mass: 33099.0
* Fuel requirements for a module with 95890 of mass: 47911.0
* Fuel requirements for a module with 115399 of mass: 57666.0
* Fuel requirements for a module with 106239 of mass: 53087.0
* Fuel requirements for a module with 126841 of mass: 63385.0
* Fuel requirements for a module with 59689 of mass: 29813.0
* Fuel requirements for a module with 146878 of mass: 73407.0
* Fuel requirements for a module with 105262 of mass: 52600.0
* Fuel requirements for a module with 137079 of mass: 68507.0
* Fuel requirements for a module with 145130 of mass: 72532.0
* Fuel requirements for a module with 114767 of mass: 57350.0
* Fuel requirements for a module with 94900 of mass: 47417.0
* Fuel requirements for a module with 64349 of mass: 32143.0
* Fuel requirements for a module with 105456 of mass: 52695.0
* Fuel requirements for a module with 59491 of mass: 29715.0
* Fuel requirements for a module with 79265 of mass: 39601.0
* Fuel requirements for a module with 89321 of mass: 44627.0
* Fuel requirements for a module with 62254 of mass: 31096.0
* Fuel requirements for a module with 106996 of mass: 53464.0
* Fuel requirements for a module with 107612 of mass: 53773.0
* Fuel requirements for a module with 71451 of mass: 35695.0
* Fuel requirements for a module with 138032 of mass: 68985.0
* Fuel requirements for a module with 137610 of mass: 68770.0
* Fuel requirements for a module with 52157 of mass: 26046.0
* Fuel requirements for a module with 68712 of mass: 34326.0
* Fuel requirements for a module with 134770 of mass: 67350.0
* Fuel requirements for a module with 111493 of mass: 55712.0
* Fuel requirements for a module with 50370 of mass: 25156.0
* Fuel requirements for a module with 91088 of mass: 45510.0
* Fuel requirements for a module with 149756 of mass: 74843.0
* Fuel requirements for a module with 51638 of mass: 25787.0
* Fuel requirements for a module with 110641 of mass: 55286.0
* Fuel requirements for a module with 60113 of mass: 30026.0
* Fuel requirements for a module with 54732 of mass: 27337.0
* Fuel requirements for a module with 86907 of mass: 43421.0
* Fuel requirements for a module with 73037 of mass: 36487.0
* Fuel requirements for a module with 111831 of mass: 55885.0
* Fuel requirements for a module with 116378 of mass: 58155.0
* Fuel requirements for a module with 93493 of mass: 46714.0
* Fuel requirements for a module with 55956 of mass: 27947.0
* Fuel requirements for a module with 111018 of mass: 55475.0
* Fuel requirements for a module with 99771 of mass: 49854.0
* Fuel requirements for a module with 65224 of mass: 32580.0
* Fuel requirements for a module with 149852 of mass: 74892.0
* Fuel requirements for a module with 97464 of mass: 48699.0
* Fuel requirements for a module with 148596 of mass: 74264.0
* Fuel requirements for a module with 140102 of mass: 70019.0
* Fuel requirements for a module with 81222 of mass: 40581.0
* Fuel requirements for a module with 106843 of mass: 53389.0
* Fuel requirements for a module with 61575 of mass: 30758.0
* Fuel requirements for a module with 112180 of mass: 56056.0
* Fuel requirements for a module with 124277 of mass: 62104.0
* Fuel requirements for a module with 59315 of mass: 29627.0
* Fuel requirements for a module with 101347 of mass: 50643.0
* Fuel requirements for a module with 141260 of mass: 70595.0
* Fuel requirements for a module with 90253 of mass: 45094.0
* Fuel requirements for a module with 87946 of mass: 43941.0
* Fuel requirements for a module with 55455 of mass: 27699.0
* Fuel requirements for a module with 115978 of mass: 57956.0
* Fuel requirements for a module with 51255 of mass: 25597.0
* Fuel requirements for a module with 149617 of mass: 74775.0
* Fuel requirements for a module with 77484 of mass: 38709.0
* Fuel requirements for a module with 133499 of mass: 66717.0
* Fuel requirements for a module with 128627 of mass: 64281.0
* Fuel requirements for a module with 75777 of mass: 37856.0
* Fuel requirements for a module with 135748 of mass: 67840.0
* Fuel requirements for a module with 87630 of mass: 43784.0
* Fuel requirements for a module with 86834 of mass: 43386.0
* Fuel requirements for a module with 145664 of mass: 72799.0
* Fuel requirements for a module with 86360 of mass: 43148.0
* Fuel requirements for a module with 139511 of mass: 69723.0
* Fuel requirements for a module with 60064 of mass: 30002.0
* Fuel requirements for a module with 106100 of mass: 53017.0
* Fuel requirements for a module with 123539 of mass: 61736.0
* Fuel requirements for a module with 115732 of mass: 57832.0
* Fuel requirements for a module with 107666 of mass: 53801.0
* Fuel requirements for a module with 89177 of mass: 44554.0
* Fuel requirements for a module with 82419 of mass: 41179.0
* Fuel requirements for a module with 98712 of mass: 49326.0
* Fuel requirements for a module with 148947 of mass: 74440.0
* Fuel requirements for a module with 50931 of mass: 25435.0

Final solution is the sum of all previous values: `5070541`