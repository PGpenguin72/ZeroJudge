m, M = map(int, input().split())
status = True

for i in range(m, M+1):
    sum = 0
    n = len(str(i))
    for j in str(i):
        sum += int(j)**n
    if sum == int(i):
        status = False
        print(sum, end=" ")

if status:
    print("none")