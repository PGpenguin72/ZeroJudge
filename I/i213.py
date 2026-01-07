n, ls = int(input()), []

for _ in range(n):
    ip = list(map(int,input().split()))
    
    if ip[0] == 1: 
        ls.append(ip[1])
    elif ip[0] == 2: 
        print(ls[-1]) if ls else print(-1)
    elif ip[0] == 3:
        ls.pop() if ls else print("")