n = int(input())

for _ in range(n):
    h1, m1, h2, m2, time = map(int, input().split())

    start = h1*60+m1
    bus = h2*60+m2

    if bus-start >= time:
        print("Yes")
    else:
        print("No")