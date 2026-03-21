while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    string = ""

    for _ in range(a):
        string += input()

    data = list(map(int, input().split()))
    for i in data:
        print(string[i-1], end="")
    print()