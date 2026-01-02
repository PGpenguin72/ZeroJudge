A1, B1, C1 = map(int, input().split())
A2, B2, C2 = map(int, input().split())

n, max, first = int(input()), 0, True

for i in range(n+1):
    X1, X2 = i, n-i
    sum = (A1*X1**2 + B1*X1 + C1) + (A2*X2**2 + B2*X2 + C2)
    if first:
        max = sum
        first = False
    if sum > max:
        max = sum
    
print(max)