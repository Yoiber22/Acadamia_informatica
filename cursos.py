from funciones import *

def agregar_cursos():
    # Agrega cursos a un archivo .txt
    pass

def eliminar_cursos():
    # Elimina un curso que no esta siedo cursado 
    # Por ningun alumno
    pass

def listar_cursos():
    # Muestra los cursos del archivo .txt
    pass

def menu_cursos():
    while True:
        try:
            clear()
            print('Sistema de Cursos\n')
            print('1. Agregar cursos')
            print('2. Eliminar cursos')
            print('3. Listar cursos')
            print('0. Volver al menu principal\n')
            opcion = int(input('Elija opcion: '))
            if opcion in range(0,4):

                if opcion == 0: break
                elif opcion == 1: agregar_cursos()
                elif opcion == 2: eliminar_cursos()
                elif opcion == 3: listar_cursos()
            
            else:
                input('Opcion no encontrda.')
        except ValueError:
            input('Opcion invalida...')