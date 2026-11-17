brawlers=[]#nombre/tipo/vida/dañoAT//nombre/tipo/vida/dañoAT
            #0     1     2    3         4    5    6     7
t=""

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
