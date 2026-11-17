prgram=True
opciones=["1","2","3","4"]

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
            print("Guardando los datos de un brawler")
        case "2":
            print("Registrando")
        case "3":
            print("Resumiendo")
        case "4":
            prgram=False