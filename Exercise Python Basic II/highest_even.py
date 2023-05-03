"""Function that return highest even number."""
def highest_even(number):
    temp = 0
    for i in number:
        if i % 2 == 0 and i > temp:
            temp = i
    return temp

print(highest_even([1,2,4,6,7,8,9,12,13,16]))

def highest_even_number(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_even_number([10,1,2,3,4,8]))