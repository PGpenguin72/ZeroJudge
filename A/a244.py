ip = int(input())
for i in range(ip):
    data = input().split()
    num = int(data[0])
    if num == 1:
        print(int(data[1]) + int(data[2]))
    elif num == 2:
        print(int(data[1]) - int(data[2]))
    elif num == 3:
        print(int(data[1]) * int(data[2]))
    else:
        print(int(int(data[1]) / int(data[2])))