while True:
    try:
        r, i = map(int, input().split())
        ls = []
        for j in range(r):
            ls.append(input().split())

        for k in range(i):
            for l in range(r):
                if l == r-1:
                    print(ls[l][k])
                else:
                    print(ls[l][k], end=" ")
    except:
        break