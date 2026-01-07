while True:
    try:
        a = int(input())
        print(int(((a**3)+(5*a)+6)/6))
    except EOFError:
        break