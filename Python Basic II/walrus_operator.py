"""
Walrus Operator i.e., :=
"""


my_list = ['a', 'b', 3, 4 ,11,'abc', True, 5, 'Mango']

if ((n := len(my_list)) > 6):
    print(f'The number of items is {n}')
