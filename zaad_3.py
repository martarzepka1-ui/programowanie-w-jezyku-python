def spr_czy_parzysta(liczba) -> bool:
    return liczba%2 ==0

wynik = spr_czy_parzysta(2345)

if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")