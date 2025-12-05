it = int(input())
for i in range(it):
    ls = []
    ip = input()
    for i in ip:
        ls.append(int(i))
    sum = ls[0]
    for i in range(len(ip)-1):
        sum *= ls[i+1]
    print(sum)
