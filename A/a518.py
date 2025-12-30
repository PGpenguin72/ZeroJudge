while True:
    try:
        a, b = map(int, input().split())
        if a != -1 or b != -1:
            a1 = ((a-b+100)%100)
            a2 = ((b-a+100)%100)
            if a1 <= a2:
                print(a1)
            else:
                print(a2)
        else:
            break
    except EOFError:
        break