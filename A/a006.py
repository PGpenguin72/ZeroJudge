ip = input()

a, b, c = ip.split()
a = int(a)
b = int(b)
c = int(c)

try:
    result_a = int((-b + (b**2 - 4*a*c)**0.5) / (2*a))
    result_b = int((-b - (b**2 - 4*a*c)**0.5) / (2*a))
    
    if result_a != result_b:
        print(f"Two different roots x1={result_a} , x2={result_b}")
    else:
        print(f"Two same roots x={result_a}")

except:
    print("No real root")