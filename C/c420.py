a = int(input())
t = int(2*a-1)
c = (a-1)

for i in range(1, a+1):
    if i == 0:
        continue
    print("_"*c, end="")
    print("*"*(i*2-1), end="")
    print("_"*c)
    c -= 1