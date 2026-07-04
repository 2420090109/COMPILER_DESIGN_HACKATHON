expr = input("Enter expression (a=b+c*d): ")

left, right = expr.split("=")

b, rest = right.split("+")
c, d = rest.split("*")

print("Three Address Code")
print("t1 =", c, "*", d)
print("t2 =", b, "+ t1")
print(left, "= t2")