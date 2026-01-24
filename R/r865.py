n, m = map(int, input().split())
dic = {input():0 for _ in range(m)}

for _ in range(n):
    datas = input().split()
    i = 1
    for data in datas:
        if data not in datas[i:3]:
            dic[data] += 1
        i += 1

for a in dic:
    print(a, dic.get(a))