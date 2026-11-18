from datetime import datetime

from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import Atencion

EDAD_MINIMA = 0
EDAD_MAXIMA = 120


# ======================= PARADIGMA ESTRUCTURADO =======================
def mostrar_menu():
    print("\n===== SISTEMA KAWSAY =====")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Buscar por código")
    print("4. Programar cita")
    print("5. Registrar atención")
    print("6. Mostrar atenciones registradas")
    print("7. Salir")


def leer_codigo(mensaje):
    return input(mensaje).strip().upper()


# Patrón Factory sencillo: centraliza la creación de Paciente y Medico
def crear_persona(tipo, codigo, nombre, dato):
    if tipo == "paciente":
        return Paciente(codigo, nombre, dato)
    if tipo == "medico":
        return Medico(codigo, nombre, dato)
    return None


# RF03 - Buscar por código: devuelve el objeto o None si no existe
def buscar_por_codigo(coleccion, codigo):
    return coleccion.get(codigo)


# RF01 - Registrar paciente
def registrar_paciente(pacientes, codigo, nombre, edad_texto):
    if codigo == "":
        return None, "El código no puede estar vacío."
    if buscar_por_codigo(pacientes, codigo) is not None:
        return None, "El código ya está registrado."
    if nombre.strip() == "":
        return None, "El nombre no puede estar vacío."
    try:
        edad = int(edad_texto)
    except ValueError:
        return None, "La edad debe ser un número entero."
    if edad < EDAD_MINIMA or edad > EDAD_MAXIMA:
        return None, f"La edad debe estar entre {EDAD_MINIMA} y {EDAD_MAXIMA}."
    paciente = crear_persona("paciente", codigo, nombre.strip(), edad)
    pacientes[codigo] = paciente
    return paciente, "El paciente se registró correctamente."


# RF02 - Registrar médico
def registrar_medico(medicos, codigo, nombre, especialidad):
    if codigo == "":
        return None, "El código no puede estar vacío."
    if buscar_por_codigo(medicos, codigo) is not None:
        return None, "El código ya está registrado."
    if nombre.strip() == "":
        return None, "El nombre no puede estar vacío."
    if especialidad.strip() == "":
        return None, "La especialidad no puede estar vacía."
    medico = crear_persona("medico", codigo, nombre.strip(), especialidad.strip())
    medicos[codigo] = medico
    return medico, "El médico se registró correctamente."


# RF04 - Programar cita
def programar_cita(citas, pacientes, medicos, codigo, cod_paciente, cod_medico, fecha):
    if codigo == "":
        return None, "El código de la cita no puede estar vacío."
    if buscar_por_codigo(citas, codigo) is not None:
        return None, "El código de la cita ya está registrado."
    paciente = buscar_por_codigo(pacientes, cod_paciente)
    if paciente is None:
        return None, "El paciente no existe."
    medico = buscar_por_codigo(medicos, cod_medico)
    if medico is None:
        return None, "El médico no existe."
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
    except ValueError:
        return None, "La fecha debe tener el formato dd/mm/aaaa."
    cita = Cita(codigo, paciente, medico, fecha)
    citas[codigo] = cita
    return cita, "La cita se programó correctamente."


# RF05 - Registrar atención
def registrar_atencion(atenciones, citas, codigo, cod_cita, motivo):
    if codigo == "":
        return None, "El código de la atención no puede estar vacío."
    if buscar_por_codigo(atenciones, codigo) is not None:
        return None, "El código de la atención ya está registrado."
    cita = buscar_por_codigo(citas, cod_cita)
    if cita is None:
        return None, "La cita no existe."
    if motivo.strip() == "":
        return None, "El motivo no puede estar vacío."
    atencion = Atencion(codigo, cita, motivo.strip())
    atenciones[codigo] = atencion
    return atencion, "La atención se registró correctamente."


# ======================= OPCIONES DEL MENÚ =======================
def opcion_buscar(pacientes, medicos, citas, atenciones):
    print("Buscar en: 1. Pacientes  2. Médicos  3. Citas  4. Atenciones")
    tipo = input("Seleccione dónde buscar: ").strip()
    colecciones = {"1": pacientes, "2": medicos, "3": citas, "4": atenciones}
    if tipo not in colecciones:
        print("Tipo de búsqueda no válido.")
        return
    codigo = leer_codigo("Ingrese el código a buscar: ")
    objeto = buscar_por_codigo(colecciones[tipo], codigo)
    if objeto is None:
        print("No se encontró ningún registro con ese código.")
    else:
        print(objeto.resumen())


def main():
    pacientes = {}
    medicos = {}
    citas = {}
    atenciones = {}

    # Datos ficticios de ejemplo
    registrar_paciente(pacientes, "P001", "Juan", "22")
    registrar_medico(medicos, "M001", "Oscar Torres", "Cardiologia")
    programar_cita(citas, pacientes, medicos, "C001", "P001", "M001", "04/11/2026")

    opcion = ""
    while opcion != "7":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = leer_codigo("Ingrese el código del paciente: ")
            nombre = input("Ingrese el nombre del paciente: ")
            edad = input("Ingrese la edad del paciente: ")
            _, mensaje = registrar_paciente(pacientes, codigo, nombre, edad)
            print(mensaje)
        elif opcion == "2":
            codigo = leer_codigo("Ingrese el código del médico: ")
            nombre = input("Ingrese el nombre del médico: ")
            especialidad = input("Ingrese la especialidad: ")
            _, mensaje = registrar_medico(medicos, codigo, nombre, especialidad)
            print(mensaje)
        elif opcion == "3":
            opcion_buscar(pacientes, medicos, citas, atenciones)
        elif opcion == "4":
            codigo = leer_codigo("Ingrese el código de la cita: ")
            cod_paciente = leer_codigo("Ingrese el código del paciente: ")
            cod_medico = leer_codigo("Ingrese el código del médico: ")
            fecha = input("Ingrese la fecha (dd/mm/aaaa): ").strip()
            _, mensaje = programar_cita(citas, pacientes, medicos,
                                        codigo, cod_paciente, cod_medico, fecha)
            print(mensaje)
        elif opcion == "5":
            codigo = leer_codigo("Ingrese el código de la atención: ")
            cod_cita = leer_codigo("Ingrese el código de la cita: ")
            motivo = input("Ingrese el motivo de atención: ")
            _, mensaje = registrar_atencion(atenciones, citas, codigo, cod_cita, motivo)
            print(mensaje)
        elif opcion == "6":
            if len(atenciones) == 0:
                print("Todavía no hay atenciones registradas.")
            else:
                for atencion in atenciones.values():
                    print(atencion.resumen())
        elif opcion == "7":
            print("Gracias por utilizar Sistema Kawsay.")
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
