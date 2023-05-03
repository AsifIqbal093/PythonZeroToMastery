"""
Write a method which takes the following array
arr = [1,2,3,4,2,4,6,8,6,8,4,2,44,2,6,32,2,5,78,32,4,5,7]
and converts the first occurrence of every element which is occurring more than once into string.
Sample Input : [1, 2, 3, 4, 2, 4, 6, 8, 6, 8, 4, 2, 44, 2, 6, 32, 2, 5, 78, 32, 4, 5, 7]
Sample Output : [1, '2', 3, '4', 2, 4, '6', '8', 6, 8, 4, 2, 44, 2, 6, '32', 2, '5', 78, 32, 4, 5, 7]
"""

arr = [1,2,3,4,2,4,6,8,6,8,4,2,44,2,6,32,2,5,78,32,4,5,7]
sample_output = []

for value in arr:
    ind = arr.index(value) 
    if value in arr[ind + 1:]:
        if str(value) in sample_output:
            sample_output.append(value)
        else:
            sample_output.append(str(value))
    else:
        sample_output.append(value)

unique = set(arr)
unique = sorted(unique)
print(unique)
print(sample_output)
print([1, '2', 3, '4', 2, 4, '6', '8', 6, 8, 4, 2, 44, 2, 6, '32', 2, '5', 78, 32, 4, 5, 7])