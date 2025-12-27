def co_druga_liczba(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])

liczby = list(range(10))
co_druga_liczba(liczby)
