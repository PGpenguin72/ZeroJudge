while True:
    try:
        data = input().split()
        dic = {"+": lambda num_1, num_2: num_1 + num_2,
               "-": lambda num_1, num_2: num_1 - num_2,
               "*": lambda num_1, num_2: num_1 * num_2,
               "/": lambda num_1, num_2: num_1 // num_2}
        sym, tmp = [], []
        for i in range(len(data)):
            if data[i] in dic:
                sym.append(i)

        while len(data) != 1:
            now = sym.pop(0)
            op = data.pop(now)
            l, r = int(data.pop(now-2)), int(data.pop(now-2))
            data.insert(now-2, str(dic.get(op)(l, r)))
            sym = [idx-2 for idx in sym]

        print(int(*data))
    
    except EOFError:
        break