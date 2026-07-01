pacientes = {}

def menu_principal():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar paciente")
    print("2. Buscar paciente")
    print("3. Eliminar paciente")
    print("4. Actualizar estado")
    print("5. Mostrar pacientes")
    print("6. Salir")
    print("=====================================")

def opcion_seleccionada():
    opcion = input("Seleccione una opción (1-6): ")
    if opcion in ["1", "2", "3", "4", "5", "6"]:
        return opcion
    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1-6).")

def buscar_paciente():
      nombre_buscar = input("Ingrese el nombre del paciente a buscar: ")
      if nombre_buscar in pacientes:
          print(f"Paciente encontrado: {nombre_buscar}")
          print(f"Edad: {pacientes[nombre_buscar]['edad']}")
          print(f"Temperatura: {pacientes[nombre_buscar]['temperatura']}")
      else:
          print("Paciente no encontrado.")

def eliminar_paciente():
    nombre_eliminar = input("Ingrese el nombre del paciente a eliminar: ")
    if nombre_eliminar in pacientes:
        del pacientes[nombre_eliminar]
        print(f"Paciente {nombre_eliminar} eliminado.")
    else:
        print("Paciente no encontrado.")

def actualizar_estado_pacientes(pacientes_lista):
    for nombre, datos in pacientes_lista.items():
        if datos["temperatura"] > 37.0:
            datos["atendido"] = False
        else:
            datos["atendido"] = True

def mostrar_pacientes(pacientes_lista):
    for nombre, datos in pacientes_lista.items():
        print("=== LISTA DE PACIENTES ===")
        print(f"Nombre: {nombre}")
        print(f"Edad: {datos['edad']}")
        print(f"Temperatura: {datos['temperatura']}")
        print(f"Estado: {'ATENDIDO' if datos['atendido'] else 'REQUIERE ATENCION'}")
        print("********************************************")

while True:

  menu_principal()

  if opcion_seleccionada() == "1":
    while True:
      try:
        nombre_paciente = input("Ingrese el nombre del paciente: ")

        if nombre_paciente.strip() == "":
            print("Error: El nombre del paciente no puede estar vacío.")
        else:
          pacientes[nombre_paciente] = {}
          break
      except ValueError:
        print("Error: El nombre del paciente debe ser una cadena de texto.")
        
    while True:
      try:
        edad_paciente = int(input("Ingrese la edad del paciente: "))

        if edad_paciente < 0:
            print("Error: La edad del paciente debe ser un número entero positivo mayor a cero.")
        else:
            pacientes[nombre_paciente]["edad"] = edad_paciente
            break
      except ValueError:
        print("Error: La edad del paciente debe ser un número entero positivo mayor a cero.")
        
    while True:
      try:

        temperatura_paciente = float(input("Ingrese la temperatura del paciente: "))

        if temperatura_paciente < 35 or temperatura_paciente > 42:
            print("Error: La temperatura del paciente debe ser un número decimal entre 35 y 42 grados Celsius.")
        else:
            pacientes[nombre_paciente]["temperatura"] = temperatura_paciente
            break
      except ValueError:
        print("Error: La temperatura del paciente debe ser un número decimal entre 35 y 42 grados Celsius.")


  elif opcion_seleccionada() == "2":
    buscar_paciente()


  elif opcion_seleccionada() == "3":
    eliminar_paciente()


  elif opcion_seleccionada() == "4":
    actualizar_estado_pacientes(pacientes)
    print("Estado de los pacientes actualizado.")
          
  elif opcion_seleccionada() == "5":
    mostrar_pacientes(pacientes)

  elif opcion_seleccionada() == "6":
    print("Gracias por usar el sistema. Vuelva Pronto")
    exit()
