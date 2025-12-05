ip = input()
ls = []
n = 0
for i in ip:
    ls.append(i)
    n += 1 

status = True    
for j in range(n):
    if ls[j] != ls[n-1]:
        status = False
    n -= 1

if status:
    print("yes")
else:
    print("no")