usr = list(map(int, input().split()))
prc = list(map(int, input().split()))

ans = 0
spe = False
for item in usr:
    if item in prc[0:-1]:
        ans += 1
    if item == prc[-1]:
        spe = True

ans_ls = ["X", "X", "X", "H", "E", "C", "A"]
spe_ls = ["X", "X", "G", "F", "D", "B"]
if spe:
    print(spe_ls[ans])
else:
    print(ans_ls[ans])