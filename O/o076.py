while True:
    try:
        n = int(input())
        total = 0
        items = input().split()
        for i in range(len(items)):#5
            sum = 0
            for j in range(i, len(items)-1):# 0, 4
                if int(items[j]) > int(items[j+1]):
                    sum += 1
                else:
                    break

            if sum+1 > total:
                total = sum+1

        print(total)
    except EOFError:
        break