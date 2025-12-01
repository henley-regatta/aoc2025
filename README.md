# aoc2025

[2025 Advent Of Code](https://adventofcode.com/2025) - My solutions

Work interferes but hopefully I can have a go....

## Python

  * `python/day1part1.py` - Yes, yes, I got the clock arithmetic wrong
  several times, couldn't work out why I should be subtracting from
  `range` instead of `dialmax` but at least I'm in the same hands at the
  Romans with my misunderstanding of the importance of zero.... *
  * `python/day1part2.py` - Some interesting corner-cases there to do with
  large spins and _when_ the dial transitions past zero. I had a couple
  silly sequence errors but mostly just failed on that when the transition
  occurs. Re-running against the test data sorted out the corner-case I
  was missing though.