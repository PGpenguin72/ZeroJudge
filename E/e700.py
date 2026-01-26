ZS_ls = ["水瓶座","雙魚座","牡羊座","金牛座","雙子座","巨蟹座","獅子座","處女座","天秤座","天蠍座","射手座","摩羯座"]
day = [0, 21, 20, 21, 21, 22, 22, 23, 22, 24, 24, 23, 23]

while True:
    try:
        m, d = map(int, input().split("/"))
        if day[m] > d:
            print(ZS_ls[m-2])
        else:
            print(ZS_ls[m-1])
    except EOFError:
        break