CZ = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"] 

while True:
    try:
        ip = int(input())
        if ip > 0:
            print(CZ[ip%12-1])
        else:
            print(CZ[ip%12])

    except EOFError:
        break