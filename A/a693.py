while True:
    try:
        n, m = map(int, input().split())
        nums = list(map(int, input().split()))
        ls = [0] * (n+1)
        for i in range(1, n+1):
            ls[i] = ls[i-1] + nums[i-1]
        for _ in range(m):
            min, max = map(int, input().split())
            print(ls[max]-ls[min-1])

    except EOFError:
        break
