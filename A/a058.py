ip = int(input())
a, b, c = 0, 0, 0
for i in range(ip):
    n = int(input())%3
    if n == 0:
        a += 1
    elif n == 1:
        b += 1
    else:
        c += 1
print(a, b, c)