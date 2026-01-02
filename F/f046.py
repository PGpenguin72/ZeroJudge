wide = int(input())
word = list(input())
time = int(input())
ls = []
for _ in range(wide):
    ls.append(" ")

for item in word:
    if time == 0:
        break
    else:
        ls.pop(0)
        ls.append(item)
    time -= 1

while time != 0:
    ls.pop(0)
    ls.append(" ")
    time -= 1

print(*ls, sep="")