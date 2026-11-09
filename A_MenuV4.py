
# Sistema de validación de documentos

print("===== BIENVENIDO =====")

opcion = ""

# Lista general de errores
errores = []

while opcion != "0":

    # Menú
    print("\nMENÚ")
    print("1. DNI")
    print("2. RUC")
    print("3. XML")
    print("4. Ver lista de errores")
    print("0. Salir")

    opcion = input("\nIngrese opción: ")

    match opcion:

        case "1":
            print("\n--- DNI ---")
            valido = False

            while valido == False:
                dni = input("Ingrese su DNI: ")

                cantidad_errores = 0
                ultimo_error = ""

                if dni == "":
                    ultimo_error = "Error: no puede estar vacío."
                    cantidad_errores = cantidad_errores + 1

                else:
                    if " " in dni:
                        ultimo_error = "Error: no puede tener espacios."
                        cantidad_errores = cantidad_errores + 1

                    if dni.isdigit() == False:
                        ultimo_error = "Error: solo números del 0 al 9."
                        cantidad_errores = cantidad_errores + 1

                    if len(dni) != 8:
                        ultimo_error = "Error: debe tener 8 dígitos."
                        cantidad_errores = cantidad_errores + 1

                    if len(dni) == 8 and dni == dni[0] * 8:
                        ultimo_error = "Error: no puede tener números repetidos."
                        cantidad_errores = cantidad_errores + 1

                    consecutivos = [
                        "01234567",
                        "12345678",
                        "23456789",
                        "76543210",
                        "87654321",
                        "98765432"
                    ]

                    if dni in consecutivos:
                        ultimo_error = "Error: no puede ser consecutivo."
                        cantidad_errores = cantidad_errores + 1

                if cantidad_errores == 0:
                    print("DNI válido:", dni)
                    valido = True
                    print("Gracias por consultar")

                else:
                    print(ultimo_error)
                    errores.append(dni + " [" + str(cantidad_errores) + "]")
                    print("Total de errores:", cantidad_errores)
                
                print("="*50)

        case "2":
            print("\n--- RUC ---")
            valido = False

            while valido == False:
                ruc = input("Ingrese su RUC: ")

                cantidad_errores = 0
                ultimo_error = ""

                if ruc == "":
                    ultimo_error = "Error: no puede estar vacío."
                    cantidad_errores = cantidad_errores + 1

                else:
                    if " " in ruc:
                        ultimo_error = "Error: no puede tener espacios."
                        cantidad_errores = cantidad_errores + 1

                    if ruc.isdigit() == False:
                        ultimo_error = "Error: solo números del 0 al 9."
                        cantidad_errores = cantidad_errores + 1

                    if len(ruc) != 11:
                        ultimo_error = "Error: debe tener 11 dígitos."
                        cantidad_errores = cantidad_errores + 1

                    if len(ruc) >= 2:
                        if ruc[0:2] != "10" and ruc[0:2] != "15" and ruc[0:2] != "16" and ruc[0:2] != "17" and ruc[0:2] != "20":
                            ultimo_error = "Error: debe empezar con 10, 15, 16, 17 o 20."
                            cantidad_errores = cantidad_errores + 1

                # Si el formato está bien, se calcula el dígito verificador
                if cantidad_errores == 0:
                    codigos = "5432765432"
                    suma = 0

                    # Paso 1: multiplicar los primeros 10 dígitos y sumar
                    for i in range(10):
                        suma = suma + int(ruc[i]) * int(codigos[i])

                    # Paso 2: residuo de dividir entre 11
                    resto = suma % 11

                    # Paso 3: 11 - residuo
                    verificador = 11 - resto

                    # Paso 4: condiciones
                    if verificador == 10:
                        verificador = 0
                    elif verificador == 11:
                        verificador = 1

                    print("Suma:", suma)
                    print("Resto:", resto)
                    print("Dígito verificador esperado:", verificador)

                    if verificador != int(ruc[10]):
                        ultimo_error = "Error: el dígito verificador es incorrecto."
                        cantidad_errores = cantidad_errores + 1

                if cantidad_errores == 0:
                    print("RUC válido:", ruc)
                    valido = True
                    print("Gracias por consultar")

                else:
                    print(ultimo_error)
                    errores.append(ruc + " [" + str(cantidad_errores) + "]")
                    print("Total de errores:", cantidad_errores)
                
                print("="*50)

        case "3":
            print("\n--- XML ---")
            valido = False

            while valido == False:
                xml = input("Ingrese el XML: ")

                cantidad_errores = 0
                ultimo_error = ""

                # Verificar que el XML inicie correctamente
                inicia = xml.startswith("<xml>")

                # Verificar que el XML termine correctamente
                termina = xml.endswith("</xml>")

                if inicia == False:
                    ultimo_error = "Error: el XML debe iniciar con <xml>."
                    cantidad_errores = cantidad_errores + 1

                if termina == False:
                    ultimo_error = "Error: el XML debe terminar con </xml>."
                    cantidad_errores = cantidad_errores + 1

                # Si las etiquetas están bien, extraer el RUC
                if cantidad_errores == 0:
                    ruc = xml[5:-6]

                    if ruc == "":
                        ultimo_error = "Error: el RUC no puede estar vacío."
                        cantidad_errores = cantidad_errores + 1

                    else:
                        print("RUC dentro del XML:", ruc)

                        # Validar que tenga 11 dígitos
                        if len(ruc) != 11:
                            ultimo_error = "Error: el RUC debe tener 11 dígitos."
                            cantidad_errores = cantidad_errores + 1

                        # Validar que solo tenga números
                        if ruc.isdigit() == False:
                            ultimo_error = "Error: el RUC solo puede tener números del 0 al 9."
                            cantidad_errores = cantidad_errores + 1

                        # Validar el inicio del RUC
                        if len(ruc) >= 2:
                            if ruc[0:2] != "10" and ruc[0:2] != "15" and ruc[0:2] != "16" and ruc[0:2] != "17" and ruc[0:2] != "20":
                                ultimo_error = "Error: el RUC debe empezar con 10, 15, 16, 17 o 20."
                                cantidad_errores = cantidad_errores + 1

                    # Si el RUC tiene buen formato, calcular el dígito verificador
                    if cantidad_errores == 0:
                        codigos = "5432765432"
                        suma = 0

                        for i in range(10):
                            suma = suma + int(ruc[i]) * int(codigos[i])

                        resto = suma % 11
                        verificador = 11 - resto

                        if verificador == 10:
                            verificador = 0
                        elif verificador == 11:
                            verificador = 1

                        print("Suma:", suma)
                        print("Resto:", resto)
                        print("Dígito verificador esperado:", verificador)

                        if verificador != int(ruc[10]):
                            ultimo_error = "Error: el dígito verificador del RUC es incorrecto."
                            cantidad_errores = cantidad_errores + 1

                if cantidad_errores == 0:
                    print("XML válido:", xml)
                    print("RUC válido:", ruc)
                    valido = True
                    print("Gracias por consultar")

                else:
                    print(ultimo_error)

                    if inicia == False or termina == False:
                        errores.append(xml + " [" + str(cantidad_errores) + "]")
                    else:
                        errores.append(ruc + " [" + str(cantidad_errores) + "]")

                    print("Total de errores:", cantidad_errores)

                print("="*50)

        case "4":
            print("\n===== LISTA DE ERRORES =====")

            if len(errores) == 0:
                print("No se han encontrado errores.")

            else:
                for i in range(len(errores)):
                    print(i + 1, "-", errores[i])

                print("\nTotal de documentos rechazados:", len(errores))
            print("="*50)

        case "0":
            print("\n¡Gracias por utilizar el sistema!")
            print("¡Hasta luego!")

        case _:
            print("\nOpción inválida.")
