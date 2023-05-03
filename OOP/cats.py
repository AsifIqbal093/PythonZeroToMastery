#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Silly', 8)
cat2 = Cat('Mano', 10)
cat3 = Cat('Lucky', 5)


# 2 Create a function that finds the oldest cat
def oldest(age1, age2, age3):
    old = max(age1,age2, age3)
    return(f'The oldest cat is {old} years old')
    


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(oldest(cat1.age, cat2.age, cat3.age))