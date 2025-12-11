while True:
    try:
        n = int(input())
        sum = 0
        ls = [1]
        for i in range(1, n+1):
            if i == 1:
                ls.append(1)
            else:
                ls.append(ls[i-1]+ls[i-2])
        
        print(ls[n])

    except EOFError:
        break