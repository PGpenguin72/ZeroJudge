a , b = map(int, input().split())
n = int(input())
item = list(map(int, input().split()))
sum = 0

for i in item:
    m = i%(a+b)
    if m >= a:
        sum += (a+b)-m

print(sum)