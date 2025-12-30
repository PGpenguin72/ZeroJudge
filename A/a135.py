i = 1
while True:
    ip = input()
    if ip != "#":
        dc = {"HELLO": "ENGLISH", "HOLA": "SPANISH", "HALLO": "GERMAN", "BONJOUR": "FRENCH", "CIAO": "ITALIAN", "ZDRAVSTVUJTE": "RUSSIAN"}
        if ip in dc:
            ans = dc.get(ip)
        else:
            ans = "UNKNOWN"
        print(f"Case {i}: {ans}")
        i += 1

    else:
        break


def bool(i):
    return 5

b = bool(i)