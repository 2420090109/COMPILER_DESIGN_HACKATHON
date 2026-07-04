import re

statement = input("Enter statement: ")

pattern = r'^int\s+[a-zA-Z_]\w*\s*=\s*\d+\s*;$'

if re.match(pattern, statement):
    print("Syntax Valid")
else:
    print("Syntax Error")