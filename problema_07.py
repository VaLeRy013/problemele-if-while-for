n=int(input("Dati numarul: "))
s=1
s2=1
v=0
for i in range(1,n+1):
    s=s*2+i
print("a)Cand Mihai a implinit",n,"ani, a primit",s,"$")
while s2<=100:
    v+=1
    s2=s2*2+v
print("b)Cadoul lui Mihai a fost mai mare de 100$,cand a implinit",v,"ani")
