ip = list(input())

for i in range(len(ip)-1):
    print(abs(ord(ip[i+1])-ord(ip[i])),end="")