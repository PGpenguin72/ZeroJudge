ip = input()
text = []
n = int(input())
for i in ip:
    text.append(i)

for n in range(n):
    ls = []
    num = int(input())
    if num == 0:
        for i in range(0, len(text), 2):
            ls.append(text[i+1])
            ls.append(text[i])
    elif num == 1:
        for i in range(0, len(text), 2):
            temp = []
            temp.append(text[i+1])
            temp.append(text[i])
            temp.sort()
            for j in temp:
                ls.append(j)
    elif num == 2:
        for i in range(0, int(len(text)/2)):
            ls.append(text[i])
            ls.append(text[(int((len(text))/2))+i])
    text = ls

for t in text:
    print(t, end="")