ip = input()
text = list(ip)
n = int(input())

for _ in range(n):
    ls = []
    num = int(input())
    if num == 0:
        for i in range(0, len(text), 2):
            ls.append(text[i+1])
            ls.append(text[i])
    elif num == 1:
        pair = sorted([text[i],text[i+1]])
        ls.extend(pair)
    elif num == 2:
        for i in range(0, int(len(text)/2)):
            ls.append(text[i])
            ls.append(text[(int((len(text))/2))+i])
    text = ls

print("".join(text))