import math

alpha = "abcdefghijklmnopqrstuvwxyz"

rucksacks = []

with open("rucksacks.txt", "r") as rucksacks_file:
  k = rucksacks_file.read()

  k = k.splitlines()

  rucksacks = k

total = 0

def calcPriority(x: str) -> int:
  if x in alpha:
    return alpha.find(x) + 1
  elif x.lower() in alpha:
    x = x.lower()
    return alpha.find(x) + 27

  return -1

for rucksack in rucksacks:
  half = math.floor(len(rucksack) / 2)

  first = rucksack[:half]
  second = rucksack[half:]

  # find letters common in both
  x = first
  y = second

  x_count = dict()
  y_count = dict()

  # go through first compartment
  for k in x:
    if k in x_count:
      x_count[k] += 1
    else:
      x_count[k] = 1

  # go through second compartment
  for k in y:
    if k in y_count:
      y_count[k] += 1
    else:
      y_count[k] = 1

  lowest_common = dict()

  # go through each key
  for x_key in x_count:
    val_x = x_count[x_key]

    if x_key in y_count:
      val_y = y_count[x_key]

      lowest_common[x_key] = min(val_x, val_y)

  # add to sum
  for key in lowest_common:
    total += calcPriority(key)
    # print(calcPriority(key), key)

print(total)
