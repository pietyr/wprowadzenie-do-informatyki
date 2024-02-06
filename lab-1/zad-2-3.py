liczba = int(input("Podaj liczbę z zakresu 0 - 999: "))
while liczba < 0 or liczba > 999:
    print("Niepoprawna liczba")
    liczba = int(input("Podaj liczbę z zakresu 0 - 999: "))
jednosci = liczba % 10
dziesiatki = (liczba % 100 - jednosci) // 10
setki = (liczba % 1000 - jednosci - dziesiatki) // 100
print("Suma cyfr = ", jednosci + dziesiatki + setki)
print("Liczba setek: ", setki)
print("Liczba dziesiątek: ", dziesiatki)
print("Liczba jedności: ", jednosci)