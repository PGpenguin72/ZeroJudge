n = int(input())
ls = list(map(int, input().split()))
ls.sort()

dict = {}

for item in ls:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1

mx = max(dict.values())

for item in dict:
    if str(dict.get(item)) == str(mx):
        print(str(item), str(mx))