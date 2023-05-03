"""Lambda Exercise."""

#Squaring List
my_list = [5,4,6,8]

print(list(map(lambda sq: sq**2, my_list)))

#List Sorting based on the second value of each tuple
a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)