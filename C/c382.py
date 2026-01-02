ip = list(input())
status = True
a, b = [], []
for i in ip:
    if i in ["+", "-", "*", "/"]:
        cal = i
        status = False
    elif status:
        a.append(i)
    else:
        b.append(i)

a_sum = 0
l = len(a)
for a_item in a:
    a_sum += int(a_item)*10**(l-1)
    l -= 1

b_sum = 0
l = len(b)
for b_item in b:
    b_sum += int(b_item)*10**(l-1)
    l -= 1

if cal == "+":
    print(a_sum+b_sum)
elif cal == "-":
    print(a_sum-b_sum)
elif cal == "*":
    print(a_sum*b_sum)
else:
    print(int(a_sum/b_sum))

# eval 解：
# e = eval
# print(int(e(input())))