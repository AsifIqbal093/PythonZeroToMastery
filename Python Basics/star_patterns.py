"""
*
**
***
****
*****
"""
num_rows = 5
k = 1
for i in range(0, num_rows):
    for j in range(0, k):
        print("* ", end="")
    k = k + 1
    print()


"""
*****
****
***
**
*
"""

num = 5
k = 5
for i in range(0,num):
    for j in range(0,k):
        print('* ', end='')
    k = k-1
    print()