idst = {
    "A": [1, 0],
    "B": [1, 1],
    "C": [1, 2],
    "D": [1, 3],
    "E": [1, 4],
    "F": [1, 5],
    "G": [1, 6],
    "H": [1, 7],
    "I": [3, 4],
    "J": [1, 8],
    "K": [1, 9],
    "L": [2, 0],
    "M": [2, 1],
    "N": [2, 2],
    "O": [3, 5],
    "P": [2, 3],
    "Q": [2, 4],
    "R": [2, 5],
    "S": [2, 6],
    "T": [2, 7],
    "U": [2, 8],
    "V": [2, 9],
    "W": [3, 2],
    "X": [3, 0],
    "Y": [3, 1],
    "Z": [3, 3]
}

ip = input()
ipls = []
for i in ip:
    ipls.append(i)

sum = 0
n = 1

for i in ipls:
    if i in idst:
        lt = idst.get(i)
        for i in lt:
            sum += i*n
            n=9
        n -= 1
    else:
        if n == 0:
            sum += int(i)
        else:
            sum += int(i)*n
            n-= 1

if sum%10 == 0:
    print("real")
else:
    print("fake")