n = int(input())
datas, dic, dot, wait, output = [], {}, {}, [], []

for _ in range(n):
    ip = input()
    ls = []
    for text in ip:
        ls.append(text)
        if text not in dic:
            dic[text] = []
            dot[text] = 0
    datas.append(ls)

for time in range(n-1):
    i = 0
    while i < len(datas[time]) and i < len(datas[time+1]):
        x, y = datas[time][i], datas[time+1][i]
        if x != y:
            if y not in dic[x]:
                dic[x].append(y)
                dot[y] += 1
            break
        i += 1

for char in dot:
    if dot[char] == 0:
        wait.append(char)

while len(wait) > 0:
    now = wait.pop(0)
    output.append(now)
    for next in dic[now]:
        dot[next] -= 1
        if dot[next] == 0:
            wait.append(next)

print("".join(output))