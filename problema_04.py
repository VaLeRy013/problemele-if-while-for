from fractions import Fraction
n1 = int(input("Dati numărătorul: "))
num1 = int(input("Dati numitorul: "))
n2 = int(input("Dati numărătorul: "))
num2 = int(input("Dati numitorul: "))
adunarea = (Fraction(n1,num1)+Fraction(n2,num2))
inmultirea = (Fraction(n1,num1)*Fraction(n2,num2))
print("adunarea =",adunarea)
print("înmulțirea =",inmultirea)