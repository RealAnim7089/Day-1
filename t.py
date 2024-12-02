left = []
right = []

with open("day1_exercise.txt") as file:
  for line in file:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

def total_distance(array1, array2):   # Part 1
  l1 = sorted(array1)
  l2 = sorted(array2)

  new_list = sorted(list(zip(l1,l2)))
  empty_l = list()

  for num1, num2 in new_list:
    empty_l.append(abs(num1 - num2))

  return sum(empty_l)

def part2(array1, array2):              # Part 2
  empty_l = []
  new_list = list(zip(array1, array2))

  for num1, num2 in new_list:
    empty_l.append(num1 * array2.count(num1))
  return sum(empty_l)

print(part2(left,right))
print(total_distance(left, right))
