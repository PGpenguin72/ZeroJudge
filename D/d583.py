while True:
    try:
        ip = int(input())
        _ = input()
        for i in range(ip):
            print(i+1, end=" ")
        print()
    except EOFError:
        break