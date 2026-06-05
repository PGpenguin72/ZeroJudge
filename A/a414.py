while True:
    n, m = str(bin(int(input())))[2:], 0 
    if n=="0": break
    for i in n: m = m+1 if i == "1" else 0
    print(m)