n = int(input("Podaj ilość liczb: "))
suma = 0

for i in range(n):
    liczba = int(input("Podaj kolejną liczbę z przedziału (10-50): "))
    while liczba < 10 or liczba > 50:
        liczba = int(input("Niepoprawna liczba! Podaj liczbę z przedziału (10-50): "))
    suma += pow(liczba, 2)

print("Suma kwadratów podanych liczb =", suma)