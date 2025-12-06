while True:
    try:
        num = int(input())
        data = input().split()
        ls = []
        for i in data:
            ls.append(int(i))
        ls.sort()
        for i in ls:
            print(i, end=" ")
        print()
    except EOFError:
        break