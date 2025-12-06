ip = int(input())
data = input().split()
sum = 0
n = 0
for j in range(1, ip+1):
    sum += j * int(data[n])
    n += 1
print(sum)