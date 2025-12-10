while True:
    try:
        n = int(input())
        print(int((n*(n+1))/2), int((n*(n+1)*(n+2))/6))
    except EOFError:
        break