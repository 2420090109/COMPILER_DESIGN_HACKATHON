import re

code = input("Enter code: ")

patterns = [
    ('KEYWORD', r'\b(int|float|char)\b'),
    ('NUMBER', r'\b\d+\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('OPERATOR', r'[+\-*/=]'),
    ('SEMICOLON', r';')
]

for token_type, pattern in patterns:
    matches = re.finditer(pattern, code)
    for match in matches:
        print(token_type, ":", match.group())