from funciones import *

def agregar_alumno():
    # Agrega alumnos a un archivo .txt

    while True:
        if existe_archivo(nom_alumnos):
            id_alumno = ultima_clave(nom_alumnos) + 1
            clear()
            print('Agregar alumno\n')
            print('ID: ',id_alumno)

            while True:
                nombre_alumno = input('Ingrese nombre: ').title()
                if len(nom_alumnos) > 0:
                    break
                else:
                    print('Campo Obligatorio.')

            while True:
                apellido_alumno = input('Ingrese apellido: ').title()
                if len(apellido_alumno) > 0:
                    break
                else:
                    print('Campo Obligatorio.')

            while True:
                fecha_nac = input('Ingrese fecha de nacimeiento (dd/mm/aaaa): ')
                if validar_fecha(fecha_nac):
                    edad_alumno = calcular_edad(fecha_nac)
                    if edad_alumno in range(1,110):
                        break
                    else:
                        input('Edad fuera de rango.')
                else:
                    input('Fecha invalida')

            while True:
                fecha_ingreso = input('Ingrese fecha de ingreso (dd/mm/aaaa): ')
                if validar_fecha(fecha_ingreso):
                    fecha_ingreso = datetime.strptime(fecha_ingreso,FORMATO_FECHA)
                    if fecha_ingreso <= fecha_actual:
                        break

            while True:
                try:
                    curso_asiste = int(input('Ingrese ID del curso al que asiste: '))
                    curso = data_registro(nom_cursos,curso_asiste)
                    if curso != None:
                        nombre_curso = curso[1].rstrip('\n')
                        print('Curso al que asiste: ', nombre_curso)
                        break
                    else:
                        input('Curso no encotrado')
                except ValueError:
                    input('\nOpcion numerica.')

            while True:
                try:
                    nota_alumno = int(input('Ingrese nota: '))
                    if nota_alumno in range(1,11):
                        break
                    else:
                        input('Las notas van del 1 al 10')
                except ValueError:
                    input('La nota es numerica.')

            while True:
                estado_alumno = input('Ingrese estado (A/B): ').upper()
                if estado_alumno == 'A' or 'B':
                    break
                else:
                    input('Opcion invalida')

            clear()
            print('Paciente a ingresar\n')
            print('Id              : ',id_alumno)
            print('Nombre          : ',nombre_alumno).z
            print('Apellido        : ',apellido_alumno)
            print('Fecha nacimeieto: ',fecha_nac)
            print('Edad            : ',edad_alumno)
            print('Fecha igreso    : ',fecha_ingreso)
            print('Curso asiste    : ',nombre_curso)
            print('Nota curso      : ',nota_alumno)
            print('Estado          : ',estado_alumno)

            if input('¿Desea ingresar a este alumno? (s/n): ').lower() =='s':
                archivo = open(nom_alumnos,'a',encoding='utf-8')
                registro = f'{id_alumno},{nombre_alumno},{apellido_alumno},{fecha_nac},{edad_alumno},{curso_asiste},{nota_alumno},{estado_alumno}\n'
                archivo.write(registro)
                archivo.close()
                print('\nAlumno gregado existosamente\n')
            if input('¿Desea agregar a otro alumno? (s/n): ').lower() !='s':
                break
        
        else:
             archivo = open(nom_alumnos,'w')
             archivo.close()
             agregar_alumno() 
            

def eliminar_alumno():
    # Elimina a alumnos del archivo .txt
    pass

def listar_alumnos():
    # Muestra a los alumnos del archivo .txt
    if existe_archivo(nom_alumnos):
        archivo = open(nom_alumnos,'r')
        registros = archivo.readlines()
        archivo.close()
        l_registros = []

        for registro in registros:
            registro = registro.split(',')
            l_registros.append(registro)

        if len(registro) > 0:
            clear()
            titulo = ['ID','Nombre','Apellido','Fecha nacimento','Fecha ingreso','Curso','Nota','Estado']
            print(tabulate(registro,headers=titulo,tablefmt='rounded_outline',numalign='center'))
            print()
            input('Pulse enter para continuar...')

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

                if opcion   == 0  : break
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

            