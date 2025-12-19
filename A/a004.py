while True:
    try:
        cin=int(input())
        if (cin % 4 == 0 and cin % 100 != 0) or (cin % 400 == 0):
            print("閏年")
        else:
            print("平年")

    except EOFError:
        break