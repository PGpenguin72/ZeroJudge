ans = str(round(((int(input())-32)*5/9), 3))
num = 3
for text in ans[-3:]:
    if text == ".":
        ans = ans + "0"*num
        break
    num -= 1

print(ans)