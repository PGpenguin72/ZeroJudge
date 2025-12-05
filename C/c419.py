a = int(input())

for i in range(1, a+1):
    if i == 0:
        continue
    print("_"*(a-i), end="")
    print("*"*i)