sueldo = int(input("Ingrese sueldo del mes: "))

print("---------Gestion de gastos---------")

luz = int(input("Costo de luz: "))
agua = int(input("Costo de agua: "))
internet = int(input("Costo internet: "))
telefono = int(input("Costo de telefono: "))
tarjeta = int(input("Costo de internet: "))
gas = int(input("Costo de gas: "))
locomocion = int(input("Costo de locomocion: "))


total = (luz + agua + internet + telefono + tarjeta + gas +locomocion)
restante = sueldo - total

print("El total de lo que hay que pagar es de: ", total)
print("Queda para el mes: ",restante)

print("Podrías ahorrar el %25 o el %50 de: ",restante)
ahorro = restante * 0.75
print("EL AHORRO DEL %25 ES = ",ahorro)
restantemes = restante - ahorro 
print("Si ahorras el %25 te quedaria para gastar en el mes: ",restantemes)
ahorro = restante * 0.50
print("EL AHORRO DEL %50 ES = ",ahorro)
restantemes =  restante - ahorro 
print("Si ahorras el %50 te quedaria para gastar en el mes: ",restantemes)