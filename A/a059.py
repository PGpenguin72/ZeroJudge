count = int(input())
data = []
for i in range(count):
    total = 0
    a = int(input())
    b = int(input())
    for j in range(1, 32):
        if j**2 >= a and j**2 <= b:
            total += j**2
    data.append(total)

for k in range(count):
    print(f"Case {k+1}: {data[k]}")