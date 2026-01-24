def main():
    a, b = map(int, input().split())
    book = list(map(int, input().split()))
    check = list(map(int, input().split()))

    for i in range(a-b):
        if check == book[i:i+b]:
            print(i+1)
            return 0
    
    print("not found")
    return 0

main()