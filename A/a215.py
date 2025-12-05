while True:
    try:
        a,b = map(int,input().split())
        i = 1 
        sum = a
        while b >= sum:
            sum = sum + a + i
            i += 1
        print(i)

    except EOFError:
        break