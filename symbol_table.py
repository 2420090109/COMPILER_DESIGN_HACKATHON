symbol_table = {}

n = int(input("Number of variables: "))

for i in range(n):
    name = input("Variable Name: ")
    dtype = input("Data Type: ")
    value = input("Value: ")

    symbol_table[name] = [dtype, value]

print("\nSymbol Table")

for k, v in symbol_table.items():
    print(k, v)