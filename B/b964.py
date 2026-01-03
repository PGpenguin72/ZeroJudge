n = int(input())
ls = list(map(int, input().split()))

print(*sorted(ls))
mx = 100
mn = 0
best, worth = True, True
for item in ls:
    if 60 > item >= mn:
        mn = item
        best = False
    if mx >= item >= 60:
        mx = item
        worth = False
if best:
    mn = "best case"
if worth:
    mx = "worst case"

print(mn, mx, sep="\n")