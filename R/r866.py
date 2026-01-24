import sys
input = sys.stdin.read
data = input().split()
iterator = iter(data)

try:
    R = int(next(iterator))
    C = int(next(iterator))
except StopIteration:
    sys.exit(0)

ls = [[-1] * (C + 2)]
for _ in range(R):
    row = [-1]
    for _ in range(C):
        row.append(int(next(iterator)))
    row.append(-1)
    ls.append(row)
ls.append([-1] * (C + 2))

ls[R+1][C+1] = 2

i, j = 1, 1
visited = [(1, 1)] 
ls[1][1] = 0

while visited:
    i, j = visited[-1]
    
    if i == R and j == C:
        break
    found_way = False
    
    if ls[i+1][j] == 1:
        ls[i+1][j] = 0
        visited.append((i+1, j))
        found_way = True
        
    elif not found_way and ls[i-1][j] == 1:
        ls[i-1][j] = 0
        visited.append((i-1, j))
        found_way = True
        
    elif not found_way and ls[i][j+1] == 1:
        ls[i][j+1] = 0
        visited.append((i, j+1))
        found_way = True
        
    elif not found_way and ls[i][j-1] == 1:
        ls[i][j-1] = 0
        visited.append((i, j-1))
        found_way = True
    
    if not found_way:
        visited.pop() 
print(len(visited))