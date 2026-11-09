
# Sistema de validación de documentos

print("===== BIENVENIDO =====")

opcion = ""

while opcion != "0":

    # Menú
    print("\nMENÚ")
    print("1. DNI")
    print("2. RUC")
    print("3. XML")
    print("0. Salir")

    opcion = input("\nIngrese opción: ")

    match opcion:

        case "1":
            print("\n--- DNI ---")
            valido = False

            while valido == False:
                dni = input("Ingrese su DNI: ")

                errores = 0

                if dni == "":
                    print("Error: no puede estar vacío.")
                    errores = errores + 1
                else:
                    if " " in dni:
                        print("Error: no puede tener espacios.")
                        errores = errores + 1
                    if dni.isdigit() == False:
                        print("Error: solo números del 0 al 9.")
                        errores = errores + 1
                    if len(dni) != 8:
                        print("Error: debe tener 8 dígitos.")
                        errores = errores + 1
                    if len(dni) == 8 and dni == dni[0] * 8:
                        print("Error: no puede tener números repetidos.")
                        errores = errores + 1
                    if dni == "12345678" or dni == "87654321":
                        print("Error: no puede ser consecutivo.")
                        errores = errores + 1

                if errores == 0:
                    print("DNI válido:", dni)
                    valido = True
                    print("Gracias por consultar")
                    opcion = "0"
                else:
                    print("Total de errores:", errores)

        case "2":
            print("\n--- RUC ---")
            valido = False

            while valido == False:
                ruc = input("Ingrese su RUC: ")

                errores = 0

                if ruc == "":
                    print("Error: no puede estar vacío.")
                    errores = errores + 1
                else:
                    if " " in ruc:
                        print("Error: no puede tener espacios.")
                        errores = errores + 1
                    if ruc.isdigit() == False:
                        print("Error: solo números del 0 al 9.")
                        errores = errores + 1
                    if len(ruc) != 11:
                        print("Error: debe tener 11 dígitos.")
                        errores = errores + 1
                    if len(ruc) >= 2:
                        if ruc[0:2] != "10" and ruc[0:2] != "15" and ruc[0:2] != "16" and ruc[0:2] != "17" and ruc[0:2] != "20":
                            print("Error: debe empezar con 10, 15, 16, 17 o 20.")
                            errores = errores + 1

                # Si el formato está bien, se calcula el dígito verificador
                if errores == 0:
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
                        print("Error: el dígito verificador es incorrecto.")
                        errores = errores + 1

                if errores == 0:
                    print("RUC válido:", ruc)
                    valido = True
                    print("Gracias por consultar")
                    opcion = "0"
                else:
                    print("Total de errores:", errores)

        case "3":
            print("\n--- XML ---")
            valido = False

            while valido == False:
                xml = input("Ingrese el XML: ")

                errores = 0

                # Verificar que el XML inicie correctamente
                inicia = xml.startswith("<xml>")

                # Verificar que el XML termine correctamente
                termina = xml.endswith("</xml>")

                if inicia == False:
                    print("Error: el XML debe iniciar con <xml>.")
                    errores = errores + 1

                if termina == False:
                    print("Error: el XML debe terminar con </xml>.")
                    errores = errores + 1

                # Si las etiquetas están bien, extraer el RUC
                if errores == 0:
                    ruc = xml[5:-6]

                    # Validar que el RUC no esté vacío
                    if ruc == "":
                        print("Error: el RUC no puede estar vacío.")
                        errores = errores + 1

                    else:
                        print("RUC dentro del XML:", ruc)

                        # Validar que tenga 11 dígitos
                        if len(ruc) != 11:
                            print("Error: el RUC debe tener 11 dígitos.")
                            errores = errores + 1

                        # Validar que solo tenga números
                        if ruc.isdigit() == False:
                            print("Error: el RUC solo puede tener números del 0 al 9.")
                            errores = errores + 1

                        # Validar el inicio del RUC
                        if len(ruc) >= 2:
                            if ruc[0:2] != "10" and ruc[0:2] != "15" and ruc[0:2] != "16" and ruc[0:2] != "17" and ruc[0:2] != "20":
                                print("Error: el RUC debe empezar con 10, 15, 16, 17 o 20.")
                                errores = errores + 1

                    # Si el RUC tiene buen formato, calcular el dígito verificador
                    if errores == 0:
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
                            print("Error: el dígito verificador del RUC es incorrecto.")
                            errores = errores + 1

                if errores == 0:
                    print("XML válido:", xml)
                    print("RUC válido:", ruc)
                    valido = True
                    print("Gracias por consultar")
                    opcion = "0"
                else:
                    print("Total de errores:", errores)

        case "0":
            print("\n¡Hasta luego!")

        case _:
            print("\nOpción inválida.")
