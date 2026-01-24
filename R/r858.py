n = int(input())
ls = list(map(int, input().split()))

r = [0, 0, 0, 0, 0, 0]
mx = 0
for item in ls:
    r[item] += 1
    if item:
        mx += 1

p = r[0]-mx
if p >= 0:
    r.append(59*mx + p*50)
else:
    r.append(abs(59*r[0]) + abs(20*p))

print(*r)