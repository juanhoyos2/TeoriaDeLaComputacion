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
