N, M = map(int, input().split())
table = list(map(int, input().split()))
table_2 = [0 for _ in range(101)]
for item in table:
    table_2[item] += 1

ans = [0 for _ in range(101)]
for _ in range(M):
    datas = list(map(int, input().split()))
    datas.pop(0)
    for data in datas:
        ans[data] += 1

l, m = 0, 0

for j in range(101):
    pan = table_2[j] - ans[j]
    if pan == 0:
        continue
    elif pan <0:
        l += abs(pan)
    else:
        m += pan

print(l, m)