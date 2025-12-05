dic = {"M":1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
math = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rome = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

def change_to_int(text):
    count = 0
    start = "S"
    for text in text:
        if start+text in dic:
            count -= dic.get(start)
            count += dic.get(start+text)
            start = text
        else:
            count += dic.get(text)
            start = text
    return count

def cals(a, b):
    rt = abs(a - b)
    if rt == 0:
        print("ZERO", end="")
        return
    for i in range(13):
        n = (rt // math[i])
        print(rome[i]*n, end="")
        rt -= math[i]*n
    return
        
while True:
    try:
        a, b = input().split()
        a_int = change_to_int(a)
        b_int = change_to_int(b)
        cals(a_int, b_int)
        print("\n", end="")
    except:
        break