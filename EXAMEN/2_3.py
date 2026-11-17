brawlers=[]#nombre/tipo/vida/dañoAT//nombre/tipo/vida/dañoAT
            #0     1     2    3         4    5    6     7
t=""
party=0
for i in range(1,3):
    brawlers.append(input(f"Nombre del brawler {i}: "))
    while t != "T" and t != "N":
        t=input(f"Tipo del brawler {i}, T (Tanque) o N (Normal): ").upper()
    match t:
        case "T":
            t="Tanque"
        case "N":
            t="Normal"
    brawlers.append(t)
    brawlers.append(int(input(f"Vida del brawler {i}: ")))
    brawlers.append(int(input(f"Daño por ataque del brawler {i}: ")))

for i in range(2):
    print(f"Brawler {i+1}: {brawlers[0+i*4]} ({brawlers[1+i*4]}) - Vida: {brawlers[2+i*4]} - Daño: {brawlers[3+i*4]}")

d1=brawlers[3]
d2=brawlers[7]
if brawlers[1]=="Tanque":
    d1=brawlers[3]*80//100
if brawlers[5]=="Tanque":
    d2=brawlers[7]*80//100

a1=0
a2=0
while d1*a1 <=brawlers[6]:
    a1+=1
while d2*a2 <=brawlers[2]:
    a2+=1
print(f"{brawlers[0]} necesita {a1} ataques para derrotar a {brawlers[4]}")
print(f"{brawlers[4]} necesita {a2} ataques para derrotar a {brawlers[0]}")
if a1 == a2:
    print("Duelo igualado")
else:
    if a1<a2:
        fav=0
    else:
        fav=4
    print(f"favorito: {brawlers[fav]}")
v1=brawlers[2]
v2=brawlers[6]
while v1!=0 and v2!=0:
    party+=1
    if party%3==0:
        d1=d1//2
        d2=d2//2
    v2=v2-d2
    if v2<=0:
        v2=0
        print(f"Ronda {party} --> {brawlers[0]}: {v1} | {brawlers[4]}: {v2}")
    else:
        v1=v1-d1
        if v1<=0:
            v1=0
        print(f"Ronda {party} --> {brawlers[0]}: {v1} | {brawlers[4]}: {v2}")
    if party%3==0:
        d1=d1//2
        d2=d2//2
             
if v1>0:
    win=brawlers[0]
    v=v1
    vT=brawlers[2]
else:
    win=brawlers[4]
    v=v2
    vT=brawlers[6]
print(f"Gana {win} en la ronda {party}.")

