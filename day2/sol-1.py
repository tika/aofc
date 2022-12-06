# Rock paper scissors

# A = rock
# B = paper
# C = scissors

# The first column is what the opponent is going to play

# X = rock
# Y = paper
# Z = scissors

# Scoring:
# Shape
# 1 - Rock
# 2 - Paper
# 3 - Scissors
# + Outcome
# 0 - Lose
# 3 - Draw
# 6 - Win

strategy = []

# pts for each shape
shapes = {
  "A": 1,
  "B": 2,
  "C": 3,
  "X": 1,
  "Y": 2,
  "Z": 3
}

# load in strategy guide
with open("encrypted-strategy-guide.txt", "r") as guide_file:
  k = guide_file.read()

  k = k.splitlines()

  for i in k:
    a, b = i.split(" ")
    strategy += [[shapes[a], shapes[b]]]

def findWinner(a: int, b: int) -> int:
  if a == 1 and b == 2:
    return b

  if a == 2 and b == 3:
    return b

  if a == 3 and b == 1:
    return b

  return a

total = 0

for k in strategy:
  # draw
  if k[0] == k[1]:
    total += 3 + k[0]
  else:
    # aka I am the loser (k[0] is the winner)
    if findWinner(k[0], k[1]) == k[0]:
      total += k[1]
    else:
      total += k[1] + 6

print(total)
