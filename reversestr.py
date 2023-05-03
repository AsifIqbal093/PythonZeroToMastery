def reverse(s):
    mystr = "" 
    for i in s: 
        mystr = i + mystr
    return mystr

print(reverse("Hello"))