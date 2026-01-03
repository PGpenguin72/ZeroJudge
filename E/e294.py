while True:
    try:
        ip = list(map(int, input()))

        def check(num_list):
            for item in num_list:
                if item % 2 == 0:
                    return False
            return True

        def next(num_list:list):
            i, status = 0, True
            for item in num_list:
                if status:
                    if item % 2 == 0:
                        num_list[i] += 1
                        status = False
                else:
                    num_list[i] = 1
                i += 1
            return num_list

        def down(num_list:list):
            i, status = 0, True
            for item in num_list:
                if status:
                    if item % 2 == 0:
                        if item == 0:
                            i_temp = i
                            num_list[i_temp] = 9
                            while True:
                                if i_temp > -1:
                                    i_temp -= 1
                                    if num_list[i_temp] > 1:
                                        if num_list[i_temp] % 2 == 0:
                                            num_list[i_temp] -= 1
                                        else:
                                            num_list[i_temp] -= 2
                                        break
                                    else:
                                        num_list[i_temp] = 9
                                else:
                                    num_list.pop(0)
                                    i = 0
                                    break
                        else:
                            num_list[i] -= 1

                        status = False
                            
                else:
                    num_list[i] = 9
                i += 1
            return num_list

        if check(ip):
            print(0)
            continue
        
        nx_l = next(ip.copy())
        nx = 0
        for item1 in nx_l:
            nx = nx*10 + item1
        dw_l = down(ip.copy())
        dw = 0
        for item2 in dw_l:
            dw = dw*10 + item2
        now = 0
        for item3 in ip:
            now = now*10 + item3

        if abs(nx - now) <= abs(dw - now):
            print(abs(nx-now))
        else:
            print(abs(dw-now))

    except EOFError:
        break