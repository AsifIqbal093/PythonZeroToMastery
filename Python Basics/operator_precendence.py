"""Operators Precedence."""


#print(20 - 3 * 4 / 2)

"""Following is the order of precedence"""
# () Bracket
# ** Power/Exponents
# * Multiplication
# / Division
# + Addition
# - Subtraction


"""Exercise."""
# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

#Question 1:
print((5 + 4) * 10 / 2)
#solution
print(45.0)

#question 2:
print(((5 + 4) * 10) / 2)
#solution
print(45.0)

#question 3:
print((5 + 4) * (10 / 2))
#Solution
print(45.0)

#Question 4:
print(5 + (4 * 10) / 2)
#Solution
print(25.0)

#Question 5:
print(5 + 4 * 10 // 2)
#Solution
print(25)