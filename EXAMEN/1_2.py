prgram=True
opciones=["1","2","3","4"]
brawlers=[]#nombre/rareza/trofInic/part
rarezas=["C","R","E","L"]

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
            print("Registrando")
        case "3":
            print("Resumiendo")
        case "4":
            prgram=False