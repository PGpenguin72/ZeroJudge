while True:
    try:
        datas = input().split()
        sym, opt = [""], []
        
        for item in datas:
            if item.isalpha():
                opt.append(item)
            
            elif item == ")":
                while sym[-1] != "(":
                    opt.append(sym.pop(-1))
                sym.pop(-1)

            else:
                if item == "(":
                    sym.append(item)
                    continue 

                while item in ["+", "-"] and sym[-1] not in ["", "("]:
                    opt.append(sym.pop(-1))
                    
                while sym != [""] and (sym[-1] in ["*", "/"] and item in ["*", "/"]):
                    opt.append(sym.pop(-1))
                
                sym.append(item)
            
        while sym:
            opt.append(sym.pop(-1))
        
        print(" ".join(opt))

    except EOFError:
        break