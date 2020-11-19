import math
m=int(input("Dati valoare lui m : "))
n=int(input("Dati valoare lui n: "))
if ((m>n)or(m==n)):
    print("nu corespunde cerintelor")
else:
    l=round(math.log(n,m))
    if (m**l==n):
        print(n,"este o putere a lui",m)
    else:
        print(n,"nu este o putere a lui",m)
