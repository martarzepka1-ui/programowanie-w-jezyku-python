def zad(lista1: list, lista2: list) -> list:
    polaczone = lista1 + lista2
    bez_duplikatow = list(set(polaczone))
    wynik = [element ** 3 for element in bez_duplikatow]
    return wynik

lista1 = [1,0,6,7]
lista2 = [7,8,5,4]

print(zad(lista1, lista2))
