while True:
    try:
        a=int(input())
        print(a*(a-1)+2)
    except EOFError:
        break