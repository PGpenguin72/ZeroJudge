from datetime import datetime as dt

while True:
    try:
        Y1, M1, D1 = map(int, input().split())
        Y2, M2, D2 = map(int, input().split())
        print(abs((dt(Y2, M2, D2) - dt(Y1, M1, D1)).days))

    except EOFError:
        break