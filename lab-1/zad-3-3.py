suma = 0
iloczyn = 1
ilosc = 0
while suma <= 256 and iloczyn <= 50000:
    liczba = int(input("Podaj kolejną liczbę: "))
    suma += liczba
    iloczyn *= liczba
    ilosc += 1

srednia = suma / ilosc
print("Średnia arytmetyczna podanych liczb = ", srednia)
