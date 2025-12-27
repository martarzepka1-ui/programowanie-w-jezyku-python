def parzyste_liczby(liczby):
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)

liczby = list(range(10))
parzyste_liczby(liczby)