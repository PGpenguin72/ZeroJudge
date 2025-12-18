while True:
    try:
        n, m = map(int, input().split())
        ls = [[0]*(n+1)for _ in range(n+1)]
        for i in range(n):
            ip = list(map(int, input().split()))
            for j in range(n):
                ls[i+1][j+1] = ls[i][j+1] + ls[i+1][j] + ip[j] - ls[i][j]

        for _ in range(m):
            x1, y1, x2, y2 = map(int, input().split())
            print(ls[x2][y2]-ls[x1-1][y2]-ls[x2][y1-1]+ls[x1-1][y1-1])

    except EOFError:
        break