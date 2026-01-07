R, C, M = map(int, input().split())
ls = []
for _ in range(R):
    ls.append(list(input().split()))

def routate(ls:list):
    new = []
    for i in range(C-1, -1, -1):
        temp = []
        for j in range(R):
            temp.append(ls[j][i])
        new.append(temp)
    return new
            
def flip(ls:list):
    new = []
    for i in range(R-1, -1, -1):
        temp = []
        for j in range(C):
            temp.append(ls[i][j])
        new.append(temp)
    return new

for value in reversed(list(map(int, input().split()))):
    if value == 0:
        ls = routate(ls)
        temp = R
        R = C
        C = temp
    elif value == 1:
        ls = flip(ls)

print(len(ls), len(ls[0]))
for item in ls:
    print(*item)