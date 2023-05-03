#Problem 1
my_list = [1,2,3,4,5]

my_dict = {x:x*2 for x in my_list}
print(my_dict)

"""


duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
"""
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set(x for x in some_list if some_list.count(x)>1))

print(some_list)
print(duplicates)