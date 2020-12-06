# Day 4: Secure Container
https://adventofcode.com/2019/day/4

## Part 1
https://adventofcode.com/2019/day/4#part1

### Description
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:
* It is a six-digit number.
* The value is within the range given in your puzzle input.
* Two adjacent digits are the same (like `22` in 1**22**345).
* Going from left to right, the digits **never decrease**; they only ever increase or stay the same (like `111123` or `135679`).

Other than the range rule, the following are true:
* `111111` meets these criteria (double `11`, never decreases).
* `223450` does not meet these criteria (decreasing pair of digits `50`).
* `123789` does not meet these criteria (no double).

**How many different passwords** within the range given in your puzzle input meet these criteria?

Your puzzle input is `134792-675810`.

### Solution
To solve this problem I am going to implement a **validation function** that evaluates a password and **returns if it is valid or not**. This function evaluates each digit of the password from the **position 0** until the **last position**, one by one. At each position, **I compare the current digit with the previous one**. All digits must satisfy the following conditions:
* **Always increase**: If any current digit is less than previous, it satisfies the never decrease condition.
* **Two adjacent digit are the same**: If any current digit is equal to the previous, it satisfies this condition.

When all digits have been evaluated, it is a **valid password** if the two conditions are satisfied. In otherwise, the password is not valid.

In this case, I **generate all possible password** inside the range with a loop and **evaluate each one**. The result is the **number of valid passwords** from generated passwords.

Result for my input data is: `2220`


## Part 2
https://adventofcode.com/2019/day/4#part2

### Description
An Elf just remembered one more important detail: the two adjacent matching digits **are not part of a larger group of matching digits**.

Given this additional criterion, but still ignoring the range rule, the following are now true:
* `112233` meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
* `123444` no longer meets the criteria (the repeated `44` is part of a larger group of `444`).
* `111122` meets the criteria (even though `1` is repeated more than twice, it still contains a double `22`).

**How many different passwords** within the range given in your puzzle input meet all of the criteria?

Your puzzle input is still `134792-675810`.

### Solution
In this part the **second criteria is modified**. Now a password satisfy this condition only if it has a digit that is repeated **exactly twice**. For example:
* `11123` not satisfies the condition because there is not a digit that is repeated twice.
* `11122` satisfies the condition, because the digit 2 is repeated exactly twice.

To solve this part I change the validation function. Now when a digit appear repeated, **I store the number of occurrences for each digit**. At the end, if any digit has appeared twice, this condition is satisfied.

Result for my input data is: `1515`