"""
Get Birth year from user and calculate age of the user, display it.
"""

import datetime

birth_year = int(input('Enter your birth year.\n'))
current_data = datetime.date.today()
age =  current_data.year - birth_year

print(f'You are {age} years old')