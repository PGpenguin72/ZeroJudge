a, b = map(int, input().split())
distance = ["E", "S", "W", "N"]
lost = []

def move(x, y, d):
    mv_list = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
    status = check(mv_list[d][0], mv_list[d][1])
    if status:
        if (x, y) not in lost:
            lost.append((x, y))
            return x, y, -1
        else:
            return x, y, d
    else:
        return mv_list[d][0], mv_list[d][1], d

def check(x, y):
    if (x > a or x < 0) or (y > b or y < 0):
        return 1
    else:
        return 0

while True:
    try:
        x, y, d = map(str, input().split())
        x, y = int(x), int(y)
        d = distance.index(d)
        cmds = list(input())
        d_t = 1
        for cmd in cmds:
            if cmd == "R":
                d = (d+1)%4
            elif cmd == "L":
                d = (d-1)%4
            elif cmd == "F":
                x_t, y_t, d_t = move(x, y, d)
                if d_t == -1:
                    print(x, y, distance[d], "LOST")
                    break
                else:
                    x, y, d = x_t, y_t, d_t
        if d_t != -1:
            print(x, y, distance[d])
        
    except EOFError:
        break