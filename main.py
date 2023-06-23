from funciones import *
import cursos, alumnos

def menu_principal():
    while True:
        try:
            clear()
            print('Menu Principal\n')
            print('1. Sistema de Alumnos')
            print('2. Sistema de Cursos')
            print('0. Salir del Programa\n')
            opcion = int(input('Ingrese opcion: '))
            if opcion in range(0,4):

                if opcion == 0: break
                elif opcion == 1: alumnos.menu_alumnos()
                elif opcion == 2: cursos.menu_cursos()

            else:
                input('Opcion no encontrada.')
        except ValueError:
            input('Opcion invalida...')

if __name__ == '__main__':
    menu_principal()