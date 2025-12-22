def prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

while True:
    try:
        x = int(input())
        if prime(x):
            print("質數")
        else:
            print("非質數")
    except EOFError:
        break