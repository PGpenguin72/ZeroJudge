while True:
    try:
        ip, sum, status, i = input(), 0, True, 1
        for text in ip:
            if text.isalpha():
                if status:
                    status = False
                    sum += 1
                i += 1
            else:
                status = True
        print(sum)
            
    except EOFError:
        break