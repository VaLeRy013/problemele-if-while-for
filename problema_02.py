n=int(input("dati valoare lui n: "))
s=0
for i in range(1,n+1):
    x=1
    for n in range(1,i+1):
        x*=n
    s+=x
print("1!+2!+3!+...+n!=",s)