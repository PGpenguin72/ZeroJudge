while True:
    try:
        a, b, n = map(int, input().split())
        it = a//b
        f = a%b
        ls = []

        for _ in range(n):
            f *= 10 
            ls.append(str(f//b))
            f %= b
        if n == 0:
            print(it)
        else:
            print(f"{it}."+ "".join(ls))
    except EOFError:
        break