ip = int(input())
result = {}

last = 1
num = 0

for i in range(2, int(ip**0.5)+1):
    prime = True
    for j in range(1 ,int(i**0.5)):
        if i%(j+1) == 0:
            prime = False
    if prime:
        count = 0
        temp = ip
        while temp%i == 0 :
            count += 1
            temp /= i
        if count != 0:
            result[f"{i}"] = str(count)
            num += 1
            last = i

if num == 1:
    count = 0
    while ip%last == 0:
        count += 1
        ip /= last
    if count != 0:
        if int(ip) != 1:
            result[f"{int(ip)}"] = str(count)
            num += 1
            last = int(ip)
elif num == 0:
    result[f"{int(ip)}"] = str(1)
    last = ip
    
for k in result:
    if str(last) != str(k):
        if str(result.get(k)) != str(1):
            print(f"{k}^{result.get(k)} * ",end="")
        else:
            print(f"{k} * ",end="")
    else:
        if str(result.get(k)) != str(1):
            print(f"{k}^{result.get(k)}",end="")
        else:
            print(f"{k}",end="")