a, c, b = map(str, input().split())
a = int(a)
b = int(b)
if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
else:
    print(int(a//b))