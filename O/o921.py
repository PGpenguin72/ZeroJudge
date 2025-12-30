a, b = map(int, input().split())
c, d = map(int, input().split())
m_d = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

print(((m_d[c-1]+d)-(m_d[a-1]+b)+365)%365)