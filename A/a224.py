while True:
    try:
        ip = input()
        odd = 0
        ls, dc = [chr(c) for c in range(ord('a'), ord('z')+1)], {chr(c):0 for c in range(ord('a'), ord('z')+1)}
        for i in ip:
            if i.lower() in ls:
                dc[i.lower()] = dc.get(i.lower()) + 1
        for j in list(dc.values()):
            if j%2 !=0:
                odd += 1
        if odd <= 1:
            print("yes !")
        else:
            print("no...")

    except EOFError:
        break