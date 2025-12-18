data = ["BNZ", "AMW", "KLY", "JVX", "HU", "GT", "FS", "ER", "DOQ", "CIP"]
ip = list(input())
sum = 0

for i in range(8, 0, -1):
    sum += int(ip[8-i])*i

print(data[-(int(ip[8])-10+(sum%10))%10])