"""
Exercise: Checking for Duplicates in a list.
"""

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


#initialising duplicates list 
# duplicates = []

duplicates = list[set(x for x in some_list if some_list.count(x)>1)]



# """First Method"""
# #Iterating over list
# for char in some_list:
#     #getting current index
#     index = some_list.index(char)
#     #checking for duplicates with in remaing values of list
#     if char in some_list[index + 1:] and char not in duplicates:
#         #adding duplicate value to duplicates
#         duplicates.append(char)

# #printing duplicates
# print('First Solution Output')
# print(duplicates)

# """Seconf Method"""

# duplicates_second = []
# #Iterating over list
# for value in some_list:
#     #checking for duplicates in list
#     if some_list.count(value) > 1 and value not in duplicates_second:
#         duplicates_second.append(value)

print("Solution from Second Method")
print(duplicates)