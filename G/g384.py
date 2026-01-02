ip = list(input())
sum = 0
for item in ip:
    sum += ord(item)-64
    
print(sum)