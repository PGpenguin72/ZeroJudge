day = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def add(default):
    while True:
        if nag:
            default -= 1
        else:
            default += 1
        sq = default**2
        m, d = (sq%10000)//100, sq%100
        if m in day:
            lim = day[m]
            if lim >= d and d > 0:
                return default
        
while True:
    try:
        ip = int(input())
        nag = False
        if ip < 0:
            nag = True
            ip = abs(ip)
        default = 4499
        for _ in range(ip):
            default = add(default)
        print(default**2)
    except EOFError:
        break