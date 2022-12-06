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
}

states = {
  "X": 0,
  "Y": 3,
  "Z": 6
}

# load in strategy guide
with open("encrypted-strategy-guide.txt", "r") as guide_file:
  k = guide_file.read()

  k = k.splitlines()

  for i in k:
    a, b = i.split(" ")
    strategy += [[shapes[a], b]]

total = 0

for k in strategy:
  total += states[k[1]]

  # figure out what I chose
  if states[k[1]] == 3:
    total += k[0]

  if states[k[1]] == 6:
    # i won
    if k[0] == 1:
      total += 2
    elif k[0] == 2:
      total += 3
    elif k[0] == 3:
      total += 1

  if states[k[1]] == 0:
    # i lost
    if k[0] == 1:
      total += 3
    elif k[0] == 2:
      total += 1
    elif k[0] == 3:
      total += 2

print(total)
