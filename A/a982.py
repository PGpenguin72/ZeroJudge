MAXN = 105
maze = []
steps = [[0 for _ in range(MAXN)] for _ in range(MAXN)]

n = int(input())

for i in range(n):
    maze.append(input())

start_y, start_x, end_y, end_x = 1, 1, n-2, n-2

steps[start_y][start_x] = 1

dot = []
dot.append((start_y, start_x))

dir_y = [1, -1, 0, 0]
dir_x = [0, 0, 1, -1]

while dot:
    p:tuple = dot.pop(0)
    y = p[0]
    x = p[1]

    if x == end_x and y == end_y:
        break

    for d in range(4):
        now_y = y + dir_y[d]
        now_x = x + dir_x[d]

        if now_y < 0 or now_y >= n or now_x < 0 or now_x >=n:
            continue

        if maze[now_y][now_x] == "#":
            continue

        if steps[now_y][now_x] != 0:
            continue

        steps[now_y][now_x] = steps[y][x] + 1
        dot.append((now_y, now_x))

if steps[end_y][end_x] == 0:
    print("No solution!")
else:
    print(steps[end_y][end_x])