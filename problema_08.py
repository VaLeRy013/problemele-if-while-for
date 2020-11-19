a, b, c = eval(input("Dati 3 numere: "))

if ((a<c+b)and(b<c+a)and(c<a+b)): 

    if ((a==b)and(a+b>c)):
         print("tringhiul e isoscel")

    if ((a==b)and(a==c)and(b==c)):
         print("triunghiul e echilateral")

    else:
         print("triungiul e scalen")
else :
    print("nu exista asa triunghi!!")        

