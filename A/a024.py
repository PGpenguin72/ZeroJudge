a, b = map(int, input().split())

while a != 0 and b != 0:
    b = b%a
    if b == 0:
        break
    a = a%b


if a == 0:
    print(b)
elif b == 0:
    print(a) 
    
