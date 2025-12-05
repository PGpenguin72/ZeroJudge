count = int(input())
for i in range(count):
    a, b, c, d = map(int, input().split())
    if d-c == c-b:
        e = 2*d-c
    else:
        e = d*(d/c)
    print(a, b, c, d, int(e))