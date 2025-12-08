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

  * `python/day3part2.py` - Ahhhh.. OK, *thats* why you should
  functionalise the digit search.... Apart from that, and some off-by-one
  errors in my indexing, this is just a repeat of the first solution with
  a sliding window across the available digits. I'd have been lost on the
  off-by-one's if the sample data hadn't been representative of the actual
  data though...

  * `python/day4part1.py` - OK time to use t'internet's favourite "just
  grow the map border" technique. And, yes, it does make boundary checks
  easy. Of course if you don't remember how `range()` works you still end
  up with off-by-ones everywhere. But having said that, some reasonably
  Pythonic approach to parsing, re-parsing and dumping a nice
  visualisation at the end too. Fun little problem.

* `python/day4part2.py` - Yay, this is just an iterative version of part
1! And I can re-use the visualisation code to make the required map
updates between iterations. Lovely job - I expect today's time differences
between p1 and p2 will be quite low. This was fun but I'd love to do a
proper visualisation animation of the removal process. If time permits...
  * `python/day4part2_visualisation.py` - each step represented as 2 output
  PNGs showing first what to be removed in red, then removing it. Later
  turned into a webm using `ffmpeg` to create an animation

* `python/day5part1.py` - OK so this has the feel of easy-part1,
expensive-part2 so let's get ahead of the curve. Used a common algorithm
to "collapse" the ranges (50% saving on later checks based on my input
data), used a simple range-finder algorithm to minimise effort to
determine which range an ingredient COULD be a part of. Let's see what
that gets me in Part 2....

* `python/day5part2.py` - YESESSS! That was the correct optimisation to
make! Collapsing the ranges to mimimum overlapping makes calculation of
the answer here ("how many IDs count as fresh?") trivial - it's just the
sum of the non-overlapping ranges. Quickest. Ever. Part 2.

* `python/day6part1.py` - Not really a Maths problem, more a sort of
parsing and data organisation issue. Marshalling the data into a parseable
form was the "hard bit"; doing the sums fairly trivial. I mean, really,
it's a matrix manipulation problem and I'm sure recognising that late
isn't going to come back to bite me in the 2nd part, right?

* `python/day6part2.py` - No, not really matrix. More a sort of "your
language's advanced features can't help you here, learn to properly string
index nerd!". Fortunately I spotted that the column delimiters could be
discerned from the position of the operands on the last row which gave me
the "in" I needed to complete the task, but I've never had so many
off-by-one and do-it-forward/do-it-backward indexing issues in my life.
The sample data was _good enough_ to help sort out all these cases so that
running against the actual data didn't throw up any more. If I hadn't
spotted that the actual data could represent a variable number of clauses
per problem (by being variable-width columns thus more/less numbers in the
problem) then I'd have been absolutely stuck.

* `python/day7part1.py` - I had to google why the EXAMPLE answer was the
value given because I could not for the life of me work it out. If you
don't understand the example then how can you proceed? Anyway, once the
core condition - a beam HAS TO HIT a splitter for it to be split - was
understood, on we proceeded with our usual level of off-by-ones and
googling basic functions. Side effect of having to work out wtf was wrong
was an inbuilt visualisation, although it looks like a xmas tree really
(who would have thought, eh?)

* `python/day7part2.py` - OK, wrong thing to be worried about. This was
another avoid-the-combinatorial-trap question. I got that the approach
would be "backtrack from the bottom up" quite quickly but it took a _lot_
longer to work out how to do it. Insight was too note that splitters just
act as sum-of-remaining-paths when tackled in reverse so, with a bit of
phaffing around number propagation __and__ the final insight that "don't
worry about zeroing out the points further on" because the answer is just
the __biggest__ number seen on the final line, boomshanka. The code is
still blazingly quick and it gets the right answer even if it's a pretty
ugly approach.