"""CAPITAL PARA EL NEGOCIO"""

from tkinter import N


print("----------------------------------------------------")
print("--Calcular los meses necesarios para poder iniciar--")
print("----------------------------------------------------")

C1 = int(input("Ingrese el capital inicial de Pedro: "))
C2 = int(input("Ingrese el capital inicial de Juan: "))
C3 = int(input("Ingrese el capital que deben tener para inciar el negocio: "))
n = 0

while (C1 + C2) < C3:

    C1 = C1 + (C1*0.03)
    C2 = C2 + (C2*0.04)
    n = n + 1

print("Los meses que necesitan invertir el capital para poder inciar el negocio es de ", str(n)) 



