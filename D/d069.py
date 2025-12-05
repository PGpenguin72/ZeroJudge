count = int(input())
for i in range(count):
    ip = int(input())
    if ip % 400 == 0:
        print("a leap year")
    elif ip % 100 == 0:
        print("a normal year")
    elif ip % 4 == 0:
        print("a leap year")
    else:
        print("a normal year")