print("Hotel Corporativo Internacional")
while True:
    cont = 0
    HabitacionEstandar = 0
    habitacionEjecutiva = 0
    try:
        cantHabitaciones = int(input("Ingrese cuantas habitaciones desea registrar: "))
        if cantHabitaciones <= 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
            continue
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        continue
    
    
    while cont < cantHabitaciones:
        while True:
            habitacion = input("Ingrese número de habitacion: ")
            if len(habitacion) < 6:
                print("El número de habitacion debe tener al menos 6 caracteres.")
                continue
            elif " " in habitacion:
                print("El número de habitacion no debe incluir espacios.")
                continue
            else:
                break
        
        while True:        
            try:
                tarifaNocturna = int(input("Ingrese la tarifa nocturna de la habitacion: "))
                if tarifaNocturna <= 0:
                    print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")
                    continue
            except ValueError:
                    print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")
                    continue
            else:
                break
        
        if tarifaNocturna > 90000:
            habitacionEjecutiva += 1
        else:
            HabitacionEstandar += 1 
        
        cont += 1        

    print(f"¡El hotel cuenta con {habitacionEjecutiva} habitaciones ejecutivas y {HabitacionEstandar} habitaciones estandar!")
    print("¡Check-in disponible!")
    break
