import re

str1 = input()

def isSSN(str1):
    return re.match(r"^\d{3}-\d{2}-\d{4}$", str1) is not None

print("Valid SSN" if isSSN(str1) else "Invalid SSN")