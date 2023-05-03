def transform(a = 2):
    if a == 1:
        return a + 2
    return a

total = 1

for x in [3,5,1]:
    total = total + transform(x)
print(total)

x = "11"
print(int(x, 2))

# print(None * 4)
# print(chr("a"))
# print(2*True - 3*False)

x = -100
from math import sqrt
x > 0 and sqrt(x)