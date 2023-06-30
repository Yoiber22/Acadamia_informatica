from funciones import *
import cursos, alumnos

init(autoreset=True)

def salir_programa():
    clear()
    if input(COLOR_INPUT+'¿Seguro quiere salir del programa? (s/n): ').lower() =='s':
        clear()
        print(COLOR_DESTACAR+'Gracias por usar mi programa\n')
        sys.exit()


def menu_principal():
    while True:
        try:
            clear()
            titulo('Menu Principal')
            print('1. Sistema de Alumnos')
            print('2. Sistema de Cursos')
            print('0. Salir del Programa\n')
            opcion = int(input(COLOR_INPUT+'Ingrese opcion: '))
            if opcion in range(0,4):

                if   opcion == 0: salir_programa()
                elif opcion == 1: alumnos.menu_alumnos()
                elif opcion == 2: cursos.menu_cursos()

            else:
                input(COLOR_ERROR+'Opcion no encontrada.')
        except ValueError:
            input(COLOR_ERROR+'Opcion invalida.')

if __name__ == '__main__':
    menu_principal()