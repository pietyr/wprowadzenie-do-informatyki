from math import sqrt

print("Równanie kwadratowe: Ax^2 + Bx + C = 0")
a = float(input("Podaj wartość współczynnika A: "))
print("Równanie kwadratowe: ", a, "x^2 + Bx + C = 0")
b = float(input("Podaj wartość współczynnika B: "))
print("Równanie kwadratowe: ", a, "x^2 + ", b, "x + C = 0")
c = float(input("Podaj wartość współczynnika C: "))

print("Równanie kwadratowe: ", a, "x^2 + ", b, "x + ", c, " = 0")
delta = pow(b, 2) - 4 * a * c
print("Delta = ", delta)

if delta < 0:
    print("Brak pierwiastków!")
elif delta == 0:
    x0 = (-b) / (2 * a)
    print("Pierwiastek = ", x0)
else:
    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)
    print("Pierwiastki równania: x1 = ", x1, ", x2 = ", x2)