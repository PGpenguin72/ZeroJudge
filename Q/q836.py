k = int(input())
a, b = map(int, input().split())
c, d = map(int, input().split())
p = 0

while k>0:
  p += k
  if (p%a) == 0:
    k -= b
  if (p%c) == 0:
    k -= d
print(p)