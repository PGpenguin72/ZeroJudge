a = int(input())

def check_dead(weight):
    if weight <= 0:
        return True
    else:
        return False
    
for _ in range(a):
    x, y, z, w, n, m = map(int, input().split())
    data = input().split()
    if data == []:
        print(f"{m}g")
    else:
        ls = []
        for item in data:
            ls.append(int(item))
        poison = False
        time = 0
        for i in ls:
            if poison:
                m -= (n * time)
                if check_dead(m):
                    break
            if i == 0:
                continue
            elif i == 1:
                m += x
            elif i == 2:
                m += y
            elif i == 3:
                m -= z
                if check_dead(m):
                    break
            elif i == 4:
                poison = True
                m -= w
                time += 1
                if check_dead(m):
                    break

        if check_dead(m):
            print("bye~Rabbit")
        else:
            print(f"{m}g")
        
