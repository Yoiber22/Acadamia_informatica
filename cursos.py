from funciones import *

def verificar_nombre_curso(nombre):
    archivo = open(direc_cursos,'r')
    cursos = archivo.readlines()
    archivo.close()
    for curso in cursos:
        curso = curso.split(',')
        nombre_analizar = curso[1].rstrip('\n')
        if nombre_analizar == nombre:
            return True
    
    return False

def agregar_cursos():
    # Agrega cursos a un archivo .txt
    
    while True:
        if existe_archivo(direc_cursos):
            id_curso = ultima_clave(direc_cursos) + 1
            clear()
            titulo('Agregar curso')
            print('Nro curso: ',id_curso)
            while True:
                nombre_curso = input(COLOR_INPUT+'Ingrese nombre: ').title()
                if len(nombre_curso) > 0:
                    if not verificar_nombre_curso(nombre_curso):
                        break
                    else:
                        print(COLOR_ERROR+f'El nombre {nombre_curso} ya fue ingresado.')
                else:
                    print(COLOR_ERROR+'Campo obligatorio')

            if input(COLOR_INPUT+'¿Desea agregar este curso? (s/n): ').lower() =='s':
                archivo = open(direc_cursos,'a',encoding='utf-8')
                registro = f'{id_curso},{nombre_curso}\n'
                archivo.write(registro)
                archivo.close()
                print(COLOR_DESTACAR+'\nCurso agregado existosamente\n')
            
            else:
                print(COLOR_DESTACAR+'\nAgregado canselado\n')

            if input(COLOR_INPUT+'¿Desea agregar otro curso? (s/n): ').lower() !='s':
                break
        else:
            archivo = open(direc_cursos,'w')
            archivo.close()
            agregar_cursos()

def eliminar_cursos():
    # Elimina un curso que no está siendo cursado 
    # por ningún alumno
    if existe_archivo(direc_cursos):
        while True:
            try:
                clear()
                titulo('Eliminar curso')
                id_borrar = int(input(COLOR_INPUT+'Ingrese ID de curso a borrar: '))
                if not alumnos_curso(direc_alumnos, id_borrar):
                    curso = data_registro(direc_cursos, id_borrar)
                    if curso is not None:
                        nombre_curso = curso[1].rstrip('\n')
                        print('Curso a borrar: ', nombre_curso)

                        if input(COLOR_INPUT+'¿Seguro desea borrar este curso? (s/n): ').lower() == 's':
                            borrar_registros(direc_cursos, id_borrar)
                            print(COLOR_DESTACAR+'\nCurso borrado exitosamente\n')
                        else:
                            input(COLOR_DESTACAR+'Borrado cancelado.')
                    else:
                        input(COLOR_ERROR+'ID de curso inválido.')
                else:
                    input(COLOR_ERROR+'Hay alumnos en este curso.')

                if input(COLOR_INPUT+'¿Desea eliminar otro curso? (s/n): ').lower() != 's':
                    break

            except ValueError:
                input(COLOR_ERROR+'ID inválido.')
    else:
        input(COLOR_ERROR+'No hay cursos para eliminar.')
        menu_cursos()

def listar_cursos():
    # Muestra los cursos del archivo .txt

    if existe_archivo(direc_cursos):
        archivo = open(direc_cursos,'r')
        registros = archivo.readlines()
        archivo.close()
        lista_registros = []
        for registro in registros:
            registro = registro.split(',')
            lista_registros.append(registro)

        if len(registros) > 0:
            clear()
            titulo('Listado de cursos')
            encabezado = ['Id','+Cursos']
            print(tabulate(lista_registros,headers=encabezado,tablefmt='rounded_outline',numalign='center'))
            print()
            pausa()

        else:
            input(COLOR_ERROR+'No se encontraron cursos.')
    else:
        input(COLOR_ERROR+'No existe el archivo.')

def alumnos_curso(nombre_archivo,id_curso):
    # Me dice si algun alumno esta cursando el curso ingresado
    
    archivo = open(nombre_archivo,'r')
    alumnos = archivo.readlines()
    archivo.close()
    for alumno in alumnos:
        alumno = alumno.split(',')
        if int(alumno[6]) == id_curso:
            return True
    return False

def menu_cursos():
    while True:
        try:
            clear()
            titulo('Sistema de Cursos')
            print('1. Agregar cursos')
            print('2. Eliminar cursos')
            print('3. Listar cursos')
            print('0. Volver al menu principal\n')
            opcion = int(input(COLOR_INPUT+'Elija opcion: '))
            if opcion in range(0,4):

                if   opcion == 0: break
                elif opcion == 1: agregar_cursos()
                elif opcion == 2: eliminar_cursos()
                elif opcion == 3: listar_cursos()
            
            else:
                print(COLOR_ERROR+'Opcion no encontrda.')
        except ValueError:
            input(COLOR_ERROR+'Opcion invalida.')