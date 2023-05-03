from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
for ind in range(len(my_pets)):
    my_pets[ind] = my_pets[ind].capitalize()

print(my_pets)  

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(tuple(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def passing_scores(num):
    return num > 50

print(list(filter(passing_scores, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumulator(acc, num):
    return acc + num

print(reduce(accumulator, list(my_numbers + scores), 0))