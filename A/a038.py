ip = input()
n = len(ip)+1
op = ""

for i in range(n+1):
    op += ip[n:n+1]
    n -= 1

print(int(op))