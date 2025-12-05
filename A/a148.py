while True:
    try:
        ip = input().split()
        x = 0
        sum = 0
        n = int(ip[x])
        for i in range(1, n+1):
            sum += int(ip[i])
        if (sum/n) <= 59:
            print("yes")
        else:
            print("no")
    except EOFError:
        break