prgram=True
opciones=["1","2","3","4"]
brawlers=[]#nombre/rareza/trof/part
partidas=[]#modo/resultado o posicion
rarezas=["C","R","E","L"]
modos=["G", "B", "N","S"]

while prgram:
    print("""===== BREAWL STARTS REGISTRO =====
1. Guardar datos del brawler
2. Registrar partida
3. Mostrar resumen
4. Terminar programa
Selecciona una opción""")
    opcion=input()

    while opcion not in opciones:
        print("Opción no válida")
        print("""===== BREAWL STARTS REGISTRO =====
    1. Guardar datos del brawler
    2. Registrar partida
    3. Mostrar resumen
    4. Terminar programa
    Selecciona una opción""")
        opcion=input()

    match opcion:
        case "1":
            r=""
            print("Guardando los datos de un brawler")
            nom=input("Nombre: ")
            brawlers.append(nom[0].upper()+nom[1:])
            while r not in rarezas:
                r=input("Rareza: ").upper()
            brawlers.append(r)
            brawlers.append(int(input("Número de trofeos iniciales: ")))
            brawlers.append(0)
            print(f"Registrado el brawler {nom}")
        case "2":
            p=""
            print("Registrando")
            while p not in modos:
                p=input("Modo de juego juego G (Atrapagemas), B (Balón Brawl), N (Noqueo) o S (Supervivencia): ").upper()
            partidas.append(p)
            if p != "S":
                f=input("Resultado de la partida V (victoria), D (Derrota) o E (Empate): ").upper()
                partidas.append(f)
            else:
                partidas.append(int(input("Posición final: ")))
            if partidas[0] != "S":
                match f:
                    case "V":
                        t=+ 10
                    case "D":
                        t=- 10
            else:
                t=(12-2*p)
            brawlers[2]=brawlers[2]+t
            print(f"El brawler {brawlers[0]} ha conseguido: {t} trofeos en esta partida, quedando su total de trofeos a {brawlers[2]}")
            brawlers[3]+=1
        case "3":
            print("Resumiendo")
            print(f"Brawler: {brawlers[0]} ({brawlers[1]})")
            print(f"Partidas registradas: {brawlers[3]}")
            print(f"Trofeos alcanzados: {brawlers[2]}")
        case "4":
            prgram=False