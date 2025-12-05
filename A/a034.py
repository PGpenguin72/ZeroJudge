while True:
    try: 
        print(bin(int(input()))[2:])
    except EOFError:
        break