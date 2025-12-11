def change(ls, n):
    temp = ls[n]
    ls[n] = ls[n+1]
    ls[n+1] = temp
    return ls

while True:
    try:
        n = int(input())
        ip = input().split()
        ls = []
        for item in ip:
            ls.append([int(item)//10, int(item)%10])
        for i in range(2):
            for _ in range(n-1):
                for j in range(n-1):
                    if i == 0:
                        if ls[j][1] > ls[j+1][1]:
                            ls = change(ls, j)
                    else:
                        if ls[j][1] == ls[j+1][1]:
                            if ls[j][0] < ls[j+1][0]:
                                ls = change(ls, j)
        for items in ls:
            if items[0] > 0:
                print(f"{items[0]}{items[1]}", end=" ")
            else:
                print(f"{items[1]}", end=" ")
        print()
                
    except EOFError:
        break