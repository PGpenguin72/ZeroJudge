from decimal import Decimal as dc, ROUND_HALF_DOWN as RD

a, b, c, d, e, f = map(int, input().split())
delta, x, y = a*e-b*d, c*e-b*f, a*f-c*d

if delta == 0:
    if x == 0 or y == 0:
        print("Too many")
    else:
        print("No answer")
else:
    print(f"x={dc(x/delta).quantize(dc('0.01'),rounding=RD)}\ny={dc(y/delta).quantize(dc('0.01'),rounding=RD)}")
