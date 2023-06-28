from funciones import *

def agregar_cursos():
    # Agrega cursos a un archivo .txt
    
    while True:
        if existe_archivo(nom_cursos):
            id_curso = ultima_clave(nom_cursos) + 1
            clear()
            print('Agregar curso\n')
            print('Nro curso: ',id_curso)
            while True:
                nombre_curso = input('Ingrese nombre: ').title()
                if len(nombre_curso) > 0:
                    break
                else:
                    input('Campo obligatorio.')

            if input('¿Desea agregar este curso? (s/n): ').lower() =='s':
                archivo = open(nom_cursos,'a',encoding='utf-8')
                registro = f'{id_curso},{nombre_curso}\n'
                archivo.write(registro)
                archivo.close()
                print('\nCurso agregado existosamente\n')
            
            else:
                print('\nAgregado canselado\n')

            if input('¿Desea agregar otro curso? (s/n): ').lower() !='s':
                break
        else:
            archivo = open(nom_cursos,'w')
            archivo.close()
            agregar_cursos()

def eliminar_cursos():
    # Elimina un curso que no esta siedo cursado 
    # por ningun alumno
    while True:
        try:
            clear()
            print('Elimanar curso\n')
            id_borrar = int(input('Ingrese ID de curso a borrar: '))
            if not alumnos_curso(nom_alumnos,id_borrar):
                nombre_curso = data_registro(nom_cursos,id_borrar)[1]
                print('Curso a borrar: ',nombre_curso)

                if input('¿Seguro desea borrar este curso? (s/n): ').lower() =='s':
                    borrar_registros(nom_cursos,id_borrar)
                    print('\nCurso borrado exitosmente\n')
                else:
                    input('Borrrado cancelado.')

            else:
                input('Hay alumnos en este curso.')

            if input('¿Desea eliminar otro curso? (s/n): ').lower() !='s':
                break

        except ValueError:
            input('ID invalida.')
        

def listar_cursos():
    # Muestra los cursos del archivo .txt

    if existe_archivo(nom_cursos):
        archivo = open(nom_cursos,'r')
        registros = archivo.readlines()
        archivo.close()
        lista_registros = []
        for registro in registros:
            registro = registro.split(',')
            lista_registros.append(registro)

        if len(registros) > 0:
            clear()
            print('Listado de cursos\n')
            encabezado = ['Id','+Cursos']
            print(tabulate(lista_registros,headers=encabezado,tablefmt='rounded_outline',numalign='center'))
            print()
            input('Puse enter para continuar...')

        else:
            ('No se encontraron cursos.')
    else:
        ('No existe el archivo.')

def alumnos_curso(nombre_archivo,id_curso):
    # Me dice si algun alumno esta cursando el curso ingresado
    
    archivo = open(nombre_archivo,'r')
    alumnos = archivo.readlines()
    archivo.close()
    for alumno in alumnos:
        alumno = alumno.split(',')
        if int(alumno[5]) == id_curso:
            return True
    return False
    

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

                if   opcion == 0: break
                elif opcion == 1: agregar_cursos()
                elif opcion == 2: eliminar_cursos()
                elif opcion == 3: listar_cursos()
            
            else:
                input('Opcion no encontrda.')
        except ValueError:
            input('Opcion invalida.')