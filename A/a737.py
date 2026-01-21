n = int(input())

for _ in range(n):
    data = list(map(int, input().split()))
    lengh = data.pop(0)
    data.sort()

    if lengh%2 == 0: 
        mid = (data[lengh//2-1]+data[lengh//2])/2 
    else: 
        mid = data[(lengh)//2]

    total = 0
    for item in data:
        total += abs(item-mid)

    print(int(total))
