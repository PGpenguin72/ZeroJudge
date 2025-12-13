ip = int(input())

sum = 0
for i in range(1, ip+1):
    time = 0
    for j in range(i+1):
        sum += j
        time += 1
    sum += i * time

print(sum)