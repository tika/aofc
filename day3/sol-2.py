import math

alpha = "abcdefghijklmnopqrstuvwxyz"

rucksacks = []

def calcPriority(x: str) -> int:
  if x in alpha:
    return alpha.find(x) + 1
  elif x.lower() in alpha:
    x = x.lower()
    return alpha.find(x) + 27

  return -1

total = 0

with open("rucksacks.txt", "r") as rucksacks_file:
  k = rucksacks_file.read()

  k = k.splitlines()

  temp = []

  for i, a in enumerate(k):
    temp.append(a)

    if (i + 1) % 3 == 0:
      rucksacks.append(temp)
      temp = []

for k in rucksacks:
  k = list(map(set, k))

  for i in k[0]:
    if i in k[1] and i in k[2]:
      total += calcPriority(i)
      break

print(total)
