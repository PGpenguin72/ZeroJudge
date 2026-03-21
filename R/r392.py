n = int(input())
data = list(map(int, input().split()))

dic = {}

for value in data:
    if value not in dic:
        dic[value] = 1
    else:
        dic[value] += 1

mx = 0
for idx, val in dic.items():
    while idx+1 < val:
        mx += idx+1
        val -= idx+1
    
    mx += idx+1

print(mx)

