print("¡Bienvenido al sistema de gestión de espacios del Almacén Industrial!")
espacios = 60
espaciosLiberar = 0
espaciosOcupar = 0
historial = 0
while True:
    
    print("=== MENÚ PRINCIPAL ===")
    print("1. Espacios disponibles")
    print("2. Ocupar espacio")
    print("3. Liberar espacio")
    print("4. Historial de ocupaciones")
    print("5. Salir")

    try:
        opcion = int(input("Ingresa una opcion: "))
        if opcion > 5 or opcion < 1:
            print("¡INVALIDO!, Debe ingresar una opcion entre 1 y 5.")
            continue
    except ValueError:
        print("¡ERROR!, Debe ingresar un número valido.")
        continue

    if opcion == 1:
        print(f"Cantidad de espacios disponibles: {espacios}")
        

    if opcion == 2:
        while True:
            try:
                espaciosOcupar = int(input("Ingrese la cantidad de espacios a ocupar: "))
                if espaciosOcupar <= 0:
                    print("La cantidad no puede ser igual o menor a 0.")
                    continue
                elif espaciosOcupar > espacios:
                    print("La cantidad no puede superar los espacios disponibles!")
                    continue
            except ValueError:
                print("ERROR!, Ingrese un número valido.")
                continue
            espacios -= espaciosOcupar
            historial += espaciosOcupar
            break

    if opcion == 3:
        while True:
            try:
                espaciosLiberar = int(input("Ingrese la cantidad de espacios a liberar: "))
                if espaciosLiberar <= 0:
                    print("La cantidad no puede ser igual o menor que 0.")
                    continue
                if espaciosLiberar > historial:
                    print("No puedes liberar más espacios de los ocupados actualmente.")
                    continue
            except ValueError:
                print("ERROR!, Ingrese un numero valido.")
                continue
            espacios += espaciosLiberar
            historial -= espaciosLiberar
            break

    
    if opcion == 4:
        print(f"La cantidad de espacios ocupados actualmente es de: {historial}")



    if opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break
