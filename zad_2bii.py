def piec_liczb_lista(lista: list) -> list:
    return [element * 2 for element in lista]

liczby = [8, 6, 4, 5, 9]
print(piec_liczb_lista(liczby))
