while True:
    try:
        n = int(input())
        ls = []
        for _ in range(n):
            ls.append(int(input()))
        ls.sort()
        for item in ls:
            print(item)
    except EOFError:
        break