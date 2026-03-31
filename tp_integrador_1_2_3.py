##############################################################################################################
#Ejercicio 1 -- Caja del Kiosco
##############################################################################################################
#1. le pido el nombre al cliente y valido el texto ingresado
nombre = input("Cliente: ").strip()

while not nombre.isalpha():
    print("Error, el nombre no puede contener espacios y deben ser solo letras")
    nombre = input("Cliente: ")

#2. le pido la cantidad de productos al cliente y valido la info. ingresada
cantidad = input("Cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error, la cantidad ingresada solo puede contener un número entero positivo")
    cantidad = input("Ingrese la cantidad de productos que desea comprar: ")

cantidad = int(cantidad)

total_sin_descuento = 0
total_con_descuento = 0

#3. por cada producto, pido el precio y si tiene o no descuento. En caso de tener, lo aplico al precio del producto
for i in range(1,cantidad + 1):
    precio = input(f"Producto {i} - Precio: ")

    while not precio.isdigit() or int(precio) <= 0:
        print("Error, el precio ingresado solo puede ser un número entero positivo")
        precio = input(f"Producto {i} - Precio: ")

    precio = int(precio)

    descuento = input("Descuento (S/N): ").strip().lower()

    while  descuento != "s" and descuento != "n":
        print("Error, solo se puede ingresar s o n como respuesta")
        descuento = input("Descuento (S/N): ").strip().lower()
    
    total_sin_descuento += precio
    
    if descuento == "s":
        precio = precio * 0.9
        total_con_descuento += precio
    else:
        total_con_descuento += precio

ahorro = total_sin_descuento - total_con_descuento
promedio = total_sin_descuento / cantidad
#4. muestro los resultados finales
print()
print(f"Total sin descuento: ${total_sin_descuento}")
print(f"Total con descuento: ${total_con_descuento}")
print(f"Ahorro: ${ahorro}")
print(f"Promedio por producto: ${promedio:.2f}")

##############################################################################################################
#Ejercicio 2 -- Acceso al campus y Menú seguro
##############################################################################################################

usuario_correcto = "alumno"
clave_correcta = "python123"

cont = 1
usuario = input(f"Intento 1/3 - Usuario: ").strip()
clave = input("Clave: ").strip()
while not (clave == clave_correcta and usuario == usuario_correcto) and cont != 3:
    print("Error: credenciales inválidas")
    usuario = input(f"Intento {cont + 1}/3 - Usuario: ").strip()
    clave =input("Clave: ").strip()
    cont += 1

if cont == 3:
    print("Cuenta bloqueada")
else:
    print("Acceso concedido")
    print("1) Estado  2) Cambiar Clave  3) Mensaje  4) Salir")
    opcion = input("Opción: ").strip()

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
        if not opcion.isdigit() == True:
            print("Ingrese un número válido")
        else:
            print("Opción fuera de rango")
        print("1) Estado  2) Cambiar Clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ").strip()

    while int(opcion) != 4:
        if int(opcion) == 1:
            print("Inscripto")
        elif int(opcion) == 2:
            clave1 = input("Nueva clave: ")
            if len(clave1) < 6:
                print("Error: mínimo 6 caracteres")
            else:
                clave2 = input("Confirmar clave: ")
                if clave1 != clave2:
                    print("Las contrseñas deben coincidir!")
                else:
                    print("Clave cambiada exitosamente")
        elif int(opcion) == 3:
            print("Vamos que te recibís!! Vos podés!!")
        print("1) Estado  2) Cambiar Clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ").strip()
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            if not opcion.isdigit() == True:
                print("Ingrese un número válido")
            else:
                print("Opción fuera de rango")
                print("1) Estado  2) Cambiar Clave  3) Mensaje  4) Salir")
                opcion = input("Opción: ").strip()


##############################################################################################################
#Ejercicio 3 -- Agenda de Turnos con nombres
##############################################################################################################

Lunes1 = ""
Lunes2 = ""
Lunes3 = ""
Lunes4 = ""

Martes1 = ""
Martes2 = ""
Martes3 = ""

nombre_operador = input("Ingrese el nombre del operador: ").strip()

while not nombre_operador.isalpha():
    print("El nombre ingresado solo puede contener letras")
    nombre_operador = input("Ingrese el nombre del operador: ").strip()

print("1) Reservar turno   2) Cancelar turno   3) Ver agenda del día   4) Ver resumen general   5) Cerrar sistema")
opcion = input("Opción: ").strip()

while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
    if not opcion.isdigit() == True:
        print("Ingrese un número válido")
        opcion = input("Opción: ").strip()
    else:
        print("Opción fuera de rango")
        print("1) Reservar turno   2) Cancelar turno   3) Ver agenda del día   4) Ver resumen general   5) Cerrar sistema")
        opcion = input("Opción: ").strip()

while int(opcion) != 5:
    if int(opcion) == 1:
        dia = input("Elija un día: 1 = Lunes, 2 = Martes: ").strip()
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            if not dia.isdigit() == True:
                print("Ingrese un número válido")
                dia = input("Elija un día: 1 = Lunes, 2 = Martes: ").strip()
            else:
                print("Opción fuera de rango")
                dia = input("Elija un día: 1 = Lunes, 2 = Martes: ").strip()
        nombre_paciente = input("Ingrese el nombre del paciente: ").strip().lower()
        while not nombre_paciente.isalpha():
            print("El nombre ingresado solo puede contener letras")
            nombre_paciente = input("Ingrese el nombre del paciente: ").strip().lower()
        if int(dia) == 1:
            if nombre_paciente != Lunes1 and nombre_paciente != Lunes2 and nombre_paciente != Lunes3 and nombre_paciente != Lunes4:
                if Lunes1 == "":
                    Lunes1 = nombre_paciente
                    print(f"El turno del paciente {nombre_paciente} ha sido registrado exitosamente")
                elif Lunes2 == "":
                    Lunes2 = nombre_paciente
                    print(f"El turno del paciente {nombre_paciente} ha sido registrado exitosamente")
                elif Lunes3 == "":
                    Lunes3 = nombre_paciente
                    print(f"El turno del paciente {nombre_paciente} ha sido registrado exitosamente")
                elif Lunes4 == "":
                    Lunes4 = nombre_paciente
                    print(f"El turno del paciente {nombre_paciente} ha sido registrado exitosamente")
                else:
                    print("En el día Lunes ya han sido asignados todos los turnos disponibles")
            elif nombre_paciente == Lunes1 or nombre_paciente == Lunes2 or nombre_paciente == Lunes3 or nombre_paciente == Lunes4:
                print(f"El paciente {nombre_paciente} ya tiene un turno para este día")
        else:
            if nombre_paciente != Martes1 and nombre_paciente != Martes2 and nombre_paciente != Martes3:
                if Martes1 == "":
                    Martes1 = nombre_paciente
                    print(f"El turno del paciente {nombre_paciente} ha sido registrado exitosamente")
                elif Martes2 == "":
                    Martes2 = nombre_paciente
                    print(f"El turno del paciente {nombre_paciente} ha sido registrado exitosamente")
                elif Martes3 == "":
                    Martes3 = nombre_paciente
                    print(f"El turno del paciente {nombre_paciente} ha sido registrado exitosamente")
                else:
                    print("En el día Martes ya han sido asignados todos los turnos disponibles")
            elif nombre_paciente == Martes1 or nombre_paciente == Martes2 or nombre_paciente == Martes3:
                print(f"El paciente {nombre_paciente} ya tiene un turno para este día")
    if int(opcion) == 2:
        dia = input("Elija un día: 1 = Lunes, 2 = Martes: ").strip()
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            if not dia.isdigit() == True:
                print("Ingrese un número válido")
                dia = input("Elija un día: 1 = Lunes, 2 = Martes: ").strip()
            else:
                print("Opción fuera de rango")
                dia = input("Elija un día: 1 = Lunes, 2 = Martes: ").strip()
        nombre_paciente = input("Ingrese el nombre del paciente: ").strip().lower()
        while not nombre_paciente.isalpha():
            print("El nombre ingresado solo puede contener letras")
            nombre_paciente = input("Ingrese el nombre del paciente: ").strip().lower()
        if int(dia) == 1:
            if nombre_paciente != Lunes1 and nombre_paciente != Lunes2 and nombre_paciente != Lunes3 and nombre_paciente != Lunes4:
                print(f"El paciente {nombre_paciente} no tiene un turno para cancelar en este día")
            else:
                if nombre_paciente == Lunes1:
                    Lunes1 = ""
                    print(f"El turno del paciente {nombre_paciente} ha sido cancelado exitosamente")
                elif nombre_paciente == Lunes2:
                    Lunes2 = ""
                    print(f"El turno del paciente {nombre_paciente} ha sido cancelado exitosamente")
                elif nombre_paciente == Lunes3:
                    Lunes3 = ""
                    print(f"El turno del paciente {nombre_paciente} ha sido cancelado exitosamente")
                elif nombre_paciente == Lunes4:
                    Lunes4 = ""
                    print(f"El turno del paciente {nombre_paciente} ha sido cancelado exitosamente")
        else:
            if nombre_paciente != Martes1 and nombre_paciente != Martes2 and nombre_paciente != Martes3:
                print(f"El paciente {nombre_paciente} no tiene un turno para cancelar en este día")
            else:
                if nombre_paciente == Martes1:
                    Martes1 = ""
                    print(f"El turno del paciente {nombre_paciente} ha sido cancelado exitosamente")
                elif nombre_paciente == Martes2:
                    Martes2 = ""
                    print(f"El turno del paciente {nombre_paciente} ha sido cancelado exitosamente")
                elif nombre_paciente == Martes3:
                    Martes3 = ""
                    print(f"El turno del paciente {nombre_paciente} ha sido cancelado exitosamente")
    elif int(opcion) == 3:
        dia = input("Elija un día: 1 = Lunes, 2 = Martes: ").strip()
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            if not dia.isdigit() == True:
                print("Ingrese un número válido")
                dia = input("Elija un día: 1 = Lunes, 2 = Martes: ").strip()
            else:
                print("Opción fuera de rango")
                dia = input("Elija un día: 1 = Lunes, 2 = Martes: ").strip()
        if int(dia) == 1:
            if Lunes1 == "":
                print("Turno 1: Libre")
            else:
                print(f"Turno 1: {Lunes1}")
            if Lunes2 == "":
                print("Turno 2: Libre")
            else: 
                print(f"Turno 2: {Lunes2}")
            if Lunes3 == "":
                print("Turno 3: Libre")
            else: 
                print(f"Turno 3: {Lunes3}")
            if Lunes4 == "":
                print("Turno 4: Libre")
            else: 
                print(f"Turno 4: {Lunes4}")
        else:
            if Martes1 == "":
                print("Turno 1: Libre")
            else:
                print(f"Turno 1: {Martes1}")
            if Martes2 == "":
                print("Turno 2: Libre")
            else: 
                print(f"Turno 2: {Martes2}")
            if Martes3 == "":
                print("Turno 3: Libre")
            else: 
                print(f"Turno 3: {Martes3}")
    elif int(opcion) == 4:
        max_lunes = 0
        max_martes = 0
        print("Turnos del día Lunes: ")
        if Lunes1 == "":
            print("Turno 1: Libre")
        else:
            print("Turno 1: Ocupado")
            max_lunes += 1
        if Lunes2 == "":
            print("Turno 2: Libre")
        else: 
            print("Turno 2: Ocupado")
            max_lunes += 1
        if Lunes3 == "":
            print("Turno 3: Libre")
        else: 
            print("Turno 3: Ocupado")
            max_lunes += 1
        if Lunes4 == "":
            print("Turno 4: Libre")
        else: 
            print("Turno 4: Ocupado")
            max_lunes += 1
        print("Turnos del día martes: ")
        if Martes1 == "":
            print("Turno 1: Libre")
        else:
            print("Turno 1: Ocupado")
            max_martes += 1
        if Martes2 == "":
            print("Turno 2: Libre")
        else: 
            print("Turno 2: Ocupado")
            max_martes += 1
        if Martes3 == "":
            print("Turno 3: Libre")
        else: 
            print("Turno 3: Ocupados")
            max_martes += 1
        if max_lunes > max_martes:
            print("El día lunes es el día con más turnos")
        elif max_lunes < max_martes:
            print("El día martes es el día con más turnos")
        else:
            print("Ambos días poseen igual cantidad de turnos")

    print("1) Reservar turno   2) Cancelar turno   3) Ver agenda del día   4) Ver resumen general   5) Cerrar sistema")
    opcion = input("Opción: ").strip()

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        if not opcion.isdigit() == True:
            print("Ingrese un número válido")
            opcion = input("Opción: ").strip()
        else:
            print("Opción fuera de rango")
            print("1) Reservar turno   2) Cancelar turno   3) Ver agenda del día   4) Ver resumen general   5) Cerrar sistema")
            opcion = input("Opción: ").strip()

##############################################################################################################
#Ejercicio 4 -- "Escape Room: La Bóveda"
##############################################################################################################

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
bloqueo = False
anti_spam = 1

print("Historia:")
print("Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.")
print("Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.")

nombre_agente = input("Ingrese su nombre, agente: ")
while not nombre_agente.isalpha():
    print("El nombre ingresado solo puede contener letras")
    nombre_agente = input("Ingrese su nombre, agente: ").strip().lower()

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueo:
    print(f"Energía: {energia}, Tiempo: {tiempo}, Cerraduras Abiertas: {cerraduras_abiertas}, Alarma: {alarma}")
    print("Elija su movimiento: 1) Forzar Cerradura   2) Hackear panel   3) Descansar")
    movimiento = input("Movimiento: ").strip()
    while not movimiento.isdigit() or int(movimiento) < 1 or int(movimiento) > 3:
        if not movimiento.isdigit() == True:
            print("Ingrese un número válido")
            movimiento = input("Movimiento: ").strip()
        else:
            print("Opción fuera de rango")
            print("Elija su movimiento: 1) Forzar Cerradura   2) Hackear panel   3) Descansar")
            movimiento = input("Movimiento: ").strip()
    if int(movimiento) == 1:
        energia -= 20
        tiempo -= 2
        if anti_spam >= 3 or alarma == True:
            print("Ups! Parece que la puerta se bloqueó!! Se han activado las alarmas!!")
            alarma = True
            if tiempo <= 3:
                bloqueo = True
        elif energia < 40 and alarma == False:
            numero = input("Ingrese un número del 1 al 3:").strip()
            while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                if not numero.isdigit() == True:
                    print("Ingrese un número válido")
                    numero = input("Ingrese un número del 1 al 3: ").strip()
                else:
                    print("Opción fuera de rango")
                    numero = input("Ingrese un número del 1 al 3: ").strip()
            if numero == 3:
                print("Ups! Se han encendido las alarmas!!")
                alarma = True
                if tiempo <= 3:
                    bloqueo = True
            else:
                cerraduras_abiertas += 1
        else:
            cerraduras_abiertas += 1
        anti_spam += 1
    elif int(movimiento) == 2:
        anti_spam = 0
        energia -= 10
        tiempo -= 3
        for i in range(1,5):
            print(f"Paso {i}")
            letra = input("Ingrese una letra: ").strip()
            if len(letra) > 1:
                print("Solo puede ingresar una letra por paso")
                letra = input("Ingrese una letra: ").strip()
            while not letra.isalpha():
                print("Solo pueden ingresarse letras")
                letra = input("Ingrese una letra: ").strip()
            codigo_parcial += letra
            print(f"{codigo_parcial}")
        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
    else:
        anti_spam = 0
        tiempo -= 1
        if alarma == True:
            energia += 5
            if energia >= 100:
                print("Ya alcanzaste la energía máxima!!")
                energia = 100
        elif alarma == False:
            energia += 15
            if energia >= 100:
                print("Ya alcanzaste la energía máxima!!")
                energia = 100
    if alarma == True and tiempo <= 3:
            print("Se han bloqueado las cerraduras!!")
            bloqueo = True

if energia <= 0 or tiempo <= 0:
    print("Derrota")
elif bloqueo == True:
    print("Derrota por bloqueo")
else:
    print("GANASTE EL JUEGO!!")

##############################################################################################################
#Ejercicio 5 -- "Escape Room: La Arena del Gladiador"
##############################################################################################################

vida_gladiador = 100
vida_enemigo = 100
pociones_de_vida = 3
ataque_pesado = 15
daño_base_Enemigo = 12
Turno_gladiador = True

print("Historia:")
print("Sos un Gladiador y vas a enfrentarte contra un enemigo.")
print("El objetivo es reducir los puntos de vida del oponente antes de que él lo haga contigo.")

print("-------BIENVENIDO A LA ARENA-------")
nombre_gladiador = input("NOMBRE DEL GLADIADOR: ").strip()
while not nombre_gladiador.isalpha():
    print("Error: solo se permiten letras")
    nombre_gladiador = input("NOMBRE DEL GLADIADOR: ").strip().lower()
print("==== INICIO DEL COMBATE ====")
while vida_gladiador > 0 and vida_enemigo > 0:
    if Turno_gladiador == True:
        print(f"{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo: (HP: {vida_enemigo}) | Pociones: {pociones_de_vida} |")
        print("Elige un movimiento: 1) Ataque pesado   2) Ráfaga veloz   3) Curar")
        movimiento = input("Movimiento: ").strip()
        while not movimiento.isdigit() or int(movimiento) < 1 or int(movimiento) > 3:
            if not movimiento.isdigit() == True:
                print("Ingrese un número válido")
                movimiento = input("Movimiento: ").strip()
            else:
                print("Opción fuera de rango")
                print("Elige un movimiento: 1) Ataque pesado   2) Ráfaga veloz   3) Curar")
                movimiento = input("Movimiento: ").strip()
        if int(movimiento) == 1:
            if vida_enemigo < 20:
                print("Has causado un golpe crítico!")
                daño = ataque_pesado * 1.5
                vida_enemigo -= daño
                print(f"Atacaste al enemigo por {daño} puntos de daño!!")
            else:
                vida_enemigo -= ataque_pesado
                print(f"Atacaste al enemigo por {ataque_pesado} puntos de daño!!")
        elif int(movimiento) == 2:
            print("Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("Golpe conectado por 5 puntos de daño")
        else:
            if pociones_de_vida > 0:
                vida_gladiador += 30
                pociones_de_vida -= 1
            else: 
                print("No te quedan más pociones!!")
        Turno_gladiador = False
    else:
        vida_gladiador -= daño_base_Enemigo
        print("El enemigo te atacó por 12 puntos de daño!!")
        print("=== NUEVO TURNO ===")
        Turno_gladiador = True

if vida_gladiador > 0:
    print(F"VICTORIA!!! {nombre_gladiador.title()} ha ganado la batalla!!")
else:
    print("DERROTA: has caído en combate")

