while True:
    try:
        ip = list(input().split())
        conj = ip.pop(0)
        if len(ip) != 1:
            n = int(len(ip)/2) + 1
        else:
            n = 0

        for item in ip:
            print(item, end=" ")
            if n != 0:
                print(conj, end=" ")
                n -= 1

        print()

    except EOFError:
        break