import re

pattern = re.compile(r"(^[A-Z])([a-zA-Z0-9*@#!%&]){8,}[0-9]")

password= 'P@kistan6545'

check = pattern.fullmatch(password)
print(check)