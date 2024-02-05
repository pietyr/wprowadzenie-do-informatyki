max = -1
for i in range(3):
    prompt = "Podaj " + str(i + 1) + " dodatnią liczbę: "
    liczba = int(input(prompt))
    while liczba <= 0:
        liczba = int(input(prompt))
    if liczba > max:
        max = liczba
print("Największa liczba = ", max)