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

                errores = []

                if dni == "":
                    errores.append("No puede estar vacío.")
                else:
                    if " " in dni:
                        errores.append("No puede tener espacios.")
                    if dni.isdigit() == False:
                        errores.append("Solo números del 0 al 9.")
                    if len(dni) != 8:
                        errores.append("Debe tener 8 dígitos.")
                    if len(dni) == 8 and dni == dni[0] * 8:
                        errores.append("No puede tener números repetidos.")
                    if dni == "12345678" or dni == "87654321":
                        errores.append("No puede ser consecutivo.")

                if len(errores) == 0:
                    print("DNI válido:", dni)
                    valido = True
                    print("Gracias por consultar")
                    opcion = "0"
                else:
                    print("\nErrores encontrados:")
                    for error in errores:
                        print("-", error)

                    print("Total de errores:", len(errores))

        case "2":
            print("\n--- RUC ---")
            valido = False

            while valido == False:
                ruc = input("Ingrese su RUC: ")

                errores = []

                if ruc == "":
                    errores.append("No puede estar vacío.")
                else:
                    if " " in ruc:
                        errores.append("No puede tener espacios.")
                    if ruc.isdigit() == False:
                        errores.append("Solo números del 0 al 9.")
                    if len(ruc) != 11:
                        errores.append("Debe tener 11 dígitos.")
                    if len(ruc) >= 2:
                        if ruc[0:2] != "10" and ruc[0:2] != "15" and ruc[0:2] != "16" and ruc[0:2] != "17" and ruc[0:2] != "20":
                            errores.append("Debe empezar con 10, 15, 16, 17 o 20.")

                # Calcular dígito verificador
                if len(errores) == 0:
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
                        errores.append("El dígito verificador es incorrecto.")

                if len(errores) == 0:
                    print("RUC válido:", ruc)
                    valido = True
                    print("Gracias por consultar")
                    opcion = "0"
                else:
                    print("\nErrores encontrados:")
                    for error in errores:
                        print("-", error)

                    print("Total de errores:", len(errores))

        case "3":
            print("\n--- XML ---")
            valido = False

            while valido == False:
                xml = input("Ingrese el XML: ")

                errores = []

                inicia = xml.startswith("<xml>")
                termina = xml.endswith("</xml>")

                if inicia == False:
                    errores.append("El XML debe iniciar con <xml>.")

                if termina == False:
                    errores.append("El XML debe terminar con </xml>.")

                if len(errores) == 0:
                    ruc = xml[5:-6]

                    if ruc == "":
                        errores.append("El RUC no puede estar vacío.")

                    else:
                        print("RUC dentro del XML:", ruc)

                        if len(ruc) != 11:
                            errores.append("El RUC debe tener 11 dígitos.")

                        if ruc.isdigit() == False:
                            errores.append("El RUC solo puede tener números del 0 al 9.")

                        if len(ruc) >= 2:
                            if ruc[0:2] != "10" and ruc[0:2] != "15" and ruc[0:2] != "16" and ruc[0:2] != "17" and ruc[0:2] != "20":
                                errores.append("El RUC debe empezar con 10, 15, 16, 17 o 20.")

                    # Calcular dígito verificador
                    if len(errores) == 0:
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
                            errores.append("El dígito verificador del RUC es incorrecto.")

                if len(errores) == 0:
                    print("XML válido:", xml)
                    print("RUC válido:", ruc)
                    valido = True
                    print("Gracias por consultar")
                    opcion = "0"
                else:
                    print("\nErrores encontrados:")
                    for error in errores:
                        print("-", error)

                    print("Total de errores:", len(errores))

        case "0":
            print("\n¡Hasta luego!")

        case _:
            print("\nOpción inválida.")
