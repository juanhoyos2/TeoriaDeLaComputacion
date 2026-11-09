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
