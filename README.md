# aoc2025

[2025 Advent Of Code](https://adventofcode.com/2025) - My solutions

Work interferes but hopefully I can have a go....

## Python

  * `python/day1part1.py` - Yes, yes, I got the clock arithmetic wrong
  several times, couldn't work out why I should be subtracting from
  `range` instead of `dialmax` but at least I'm in the same hands at the
  Romans with my misunderstanding of the importance of zero....

  * `python/day1part2.py` - Some interesting corner-cases there to do with
  large spins and _when_ the dial transitions past zero. I had a couple
  silly sequence errors but mostly just failed on that when the transition
  occurs. Re-running against the test data sorted out the corner-case I
  was missing though.

  * `python/day2part1.py` - A good question today, with the world's
  stupidest answer provided. Yes, I too like to treat mathematical
  problems as string comparison exercises. I'm absolutely sure this will
  in no way come back to bite me in Part 2....

  * `python/day2part2.py` - I think I'm ashamed of this solution. I mean
  it _works_ but I really can't help but feel a bit dirty for just
  treating this as a string comparision problem. And taking the most
  brute-force approach to generating the strings and fragments. I'm really
  not a pythonista, am I?

  * `python/day3part1.py` - Actually I'm quite satisfied with this. Got
  the algorithm right first time, found the corner case and correctly
  worked around it, solution's fairly simplistic (you could functionalise
  the digit search to avoid repetition but why bother?). Let's see what
  part 2 has to bring to the table...