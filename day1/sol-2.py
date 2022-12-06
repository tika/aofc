# task: find elf carrying most calories
inventory_totals = []

with open("calories.txt", "r") as calories_file:
  k = calories_file.read()

  # split by new line
  k = k.split("\n")

  inventories = []
  temp        = []

  for i in k:
    if i == "":
      inventories.append(temp)
      temp = []
      continue

    temp.append(int(i))

  # find the total of each inventory
  for i in inventories:
    inventory_totals += [sum(i)]

inventory_totals = list(reversed(sorted(inventory_totals)))

print(inventory_totals[0] + inventory_totals[1] + inventory_totals[2])
