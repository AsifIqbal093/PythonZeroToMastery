"""
Password Checker Program.
"""

username = input('Enter your username.\n')
password = input('Enter your password.\n')

hidden_pass = '*' * len(password)
print(f'Hello {username}! \n Your Password {hidden_pass} is {len(password)} characters long.')