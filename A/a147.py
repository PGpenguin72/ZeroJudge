while True:
    ip = int(input())
    if ip == 0:
        break
    for i in range(ip):
        if i%7 == 0:
            continue
        print(i, end=" ")
    print()