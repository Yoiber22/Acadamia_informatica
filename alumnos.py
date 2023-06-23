from funciones import *

def agregar_alumno():
    # Agrega alumnos a un archivo .txt
    pass

def eliminar_alumno():
    # Elimina a alumnos del archivo .txt
    pass

def listar_alumnos():
    # Muestra a los alumnos del archivo .txt
    pass

def consultar_alumno():
    # Muestra 
    pass

def listar_aprobaciones():
    # Muestra a los alumnos Aprobados y No Aprobados
    pass

def listar_estado_curso():
    # Muestra que alumnos esta activos
    # y que alumnos estan dados de baja
    pass

def modificar_estado():
    # Modifica el estado del alumno para dorlo de baja o activo
    pass


def menu_alumnos():
    while True:
        try:
            clear()
            print('Sistema de alumnos\n')
            print('1. Agregar alumno')
            print('2. Eliminar alumnos')
            print('3. Consultar alumno')
            print('4. Listar alumnos')
            print('5. Listado de aprobaciones')
            print('6. Listado de estado en el curso')
            print('7. Modificar estado de alumno')
            print('0. Volver al menu pricipal\n')
            opcion = int(input('Elija opcion: '))
            if opcion in range(0,8):

                if opcion == 0  : break
                elif opcion == 1: agregar_alumno()
                elif opcion == 2: eliminar_alumno()
                elif opcion == 3: consultar_alumno()
                elif opcion == 4: listar_alumnos()
                elif opcion == 5: listar_aprobaciones()
                elif opcion == 6: listar_estado_curso()
                elif opcion == 7: modificar_estado()

            else:
                input('Opcion no encontrada.')             
        except ValueError:
            input('Opcion invalida...')

            