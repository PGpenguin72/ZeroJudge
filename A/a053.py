ip = int(input())
if 0 <= ip <= 10:
    print(ip*6)
elif 11 <= ip <= 20:
    print((ip-10)*2+60)
elif 21 <= ip <= 40:
    print((ip-20)*1+80)
else:
    print(100)