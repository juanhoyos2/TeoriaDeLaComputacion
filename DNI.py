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

