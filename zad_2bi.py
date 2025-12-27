def piec_liczb_funkcja(lista: list) -> list:
    wynik = []
    for liczba in lista:
        wynik.append(liczba*2)
    return wynik

liczby = [2, 9, 7, -6, 4]
print(piec_liczb_funkcja(liczby))
