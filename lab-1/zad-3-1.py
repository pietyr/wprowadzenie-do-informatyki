wynik = 0

while wynik == 0:
    symbol_pierwszego_gracza = int(input('Podaj symbol 1 gracza: 0 (papier), 1(nożyce) lub 2(kamień): '))
    symbol_drugiego_gracza = int(input('Podaj symbol 2 gracza: 0 (papier), 1(nożyce) lub 2(kamień): '))

    wynik = symbol_pierwszego_gracza - symbol_drugiego_gracza
    if wynik == 0:
        print("REMIS")
    elif wynik == 1 or wynik == -2:
        print("Gracz 1 wygrywa")
    else:
        print("Gracz 2 wygrywa")