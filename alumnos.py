from funciones import *

if existe_archivo(direc_alumnos):
    registro_alumnos = registros(direc_alumnos)

def agregar_alumno():
    # Agrega alumnos a un archivo .txt

    while True:
        if existe_archivo(direc_alumnos):
            id_alumno = ultima_clave(direc_alumnos) + 1
            clear()
            titulo('Agregar alumno')
            print('ID: ',id_alumno)

            while True:
                nombre_alumno = input(COLOR_INPUT+'Ingrese nombre: ').title()
                if len(nombre_alumno) > 0:
                    break
                else:
                    input(COLOR_ERROR+'Campo Obligatorio.')

            while True:
                apellido_alumno = input(COLOR_INPUT+'Ingrese apellido: ').title()
                if len(apellido_alumno) > 0:
                    break
                else:
                    input(COLOR_ERROR+'Campo Obligatorio.')

            while True:
                fecha_nac = input(COLOR_INPUT+'Ingrese fecha de nacimeiento (dd/mm/aaaa): ')
                if validar_fecha(fecha_nac):
                    edad_alumno = calcular_edad(fecha_nac)
                    if edad_alumno in range(1,110):
                        break
                    else:
                        input(COLOR_ERROR+'Edad fuera de rango.')
                else:
                    input(COLOR_ERROR+'Fecha invalida')

            while True:
                fecha_ingreso = input(COLOR_INPUT+'Ingrese fecha de ingreso (dd/mm/aaaa): ')
                if validar_fecha(fecha_ingreso):
                    fecha_ingreso = datetime.strptime(fecha_ingreso,FORMATO_FECHA)
                    if fecha_ingreso <= fecha_actual:
                        break
                    else:
                        input(COLOR_ERROR+'La fecha deve ser anterior a la actual')
                else:
                    input(COLOR_ERROR+'Fecha invalida.')

            while True:
                try:
                    curso_asiste = int(input(COLOR_INPUT+'Ingrese ID del curso al que asiste: '))
                    curso = data_registro(direc_cursos,curso_asiste)
                    if curso != None:
                        nombre_curso = curso[1].rstrip('\n')
                        print('Curso al que asiste: ', nombre_curso)
                        break
                    else:
                        input(COLOR_ERROR+'Curso no encotrado.')
                except ValueError:
                    input(COLOR_ERROR+'Opcion numerica.')

            while True:
                try:
                    nota_alumno = int(input(COLOR_INPUT+'Ingrese nota: '))
                    if nota_alumno in range(1,11):
                        break
                    else:
                        input(COLOR_ERROR+'Las notas van del 1 al 10')
                except ValueError:
                    input(COLOR_ERROR+'La nota es numerica.')

            while True:
                estado_alumno = input(COLOR_INPUT+'Ingrese estado (A/B): ').upper()
                if estado_alumno == 'A' or estado_alumno == 'B':
                    break
                else:
                    input(COLOR_ERROR+'Opcion invalida')

            clear()
            titulo('Alumno a ingresar')
            print('Id              : ',id_alumno)
            print('Nombre          : ',nombre_alumno)
            print('Apellido        : ',apellido_alumno)
            print('Fecha nacimeieto: ',fecha_nac)
            print('Edad            : ',edad_alumno)
            print('Fecha igreso    : ',fecha_ingreso)
            print('Curso asiste    : ',nombre_curso)
            print('Nota curso      : ',nota_alumno)
            print('Estado          : ',estado_alumno)

            if input(COLOR_INPUT+'¿Desea ingresar a este alumno? (s/n): ').lower() =='s':
                archivo = open(direc_alumnos,'a',encoding='utf-8')
                registro = f'{id_alumno},{nombre_alumno},{apellido_alumno},{fecha_nac},{edad_alumno},{fecha_ingreso},{curso_asiste},{nota_alumno},{estado_alumno}\n'
                archivo.write(registro)
                archivo.close()
                print(COLOR_DESTACAR+'\nAlumno agregado existosamente\n')
            if input(COLOR_INPUT+'¿Desea agregar a otro alumno? (s/n): ').lower() !='s':
                break
        
        else:
             archivo = open(direc_alumnos,'w')
             archivo.close()
             agregar_alumno() 
            

def eliminar_alumno():
    # Elimina a alumnos del archivo .txt

    if existe_archivo(direc_alumnos) and len(registro_alumnos) > 0:
        while True:
            try:
                clear()
                titulo('Eliminar alumno')
                id_borrar = int(input(COLOR_INPUT+'Ingrese ID de alumno a eliminar: '))
                cant_alumnos = ultima_clave(direc_alumnos) + 1
                if id_borrar in range(0,cant_alumnos):
                    nombre_alumno = data_registro(direc_alumnos,id_borrar)[1]
                    apellido_alumno = data_registro(direc_alumnos,id_borrar)[2]

                    if input(COLOR_INPUT+f'¿Seguro desea eliminar a {nombre_alumno} {apellido_alumno}? (s/n): ').lower() =='s':
                        borrar_registros(direc_alumnos,id_borrar)
                        print(COLOR_DESTACAR+'Alumno eliminado exitosamente.')
                    else:
                        print(COLOR_DESTACAR+'Borrardo cancelado.') 

                    if input(COLOR_INPUT+'¿Desea eliminar a otro alumno? (s/n): ').lower() !='s':
                        break
                else:
                    input(COLOR_ERROR+'Alumno no enontrado.')
            except ValueError:
                input(COLOR_ERROR+'ID invalida.')
    else:
        input(COLOR_ERROR+'No se encontraron alumnos.')

def listar_alumnos():
    # Muestra a los alumnos del archivo .txt

    if existe_archivo(direc_alumnos) and len(registro_alumnos) > 0:
        l_registros = []

        for registro in registro_alumnos:
            registro = registro.split(',')
            l_registros.append(registro)

        if len(registro) > 0:
            clear()
            titulo('Listado alumnos')
            encabezado = ['ID','Nombre','Apellido','Fecha nacimento','Edad','Fecha ingreso','Curso','Nota','Estado']
            print(tabulate(l_registros,headers=encabezado,tablefmt='rounded_outline',numalign='center'))
            print()
            pausa()
    else:
        input(COLOR_ERROR+'No se encontraron alumnos.')      

def consultar_alumno():
    # Muestra los datos de un alumno

    while True:
        try:
            clear()
            titulo('Consular alumno')
            id_consultar = int(input(COLOR_INPUT+('Ingrese codigo a cosultar: ')))
            data_alumno = data_registro(direc_alumnos,id_consultar)
            if data_alumno != None:
                titulo('Datos del alumno')
                print('Id              : ',data_alumno[0])
                print('Nombre          : ',data_alumno[1])
                print('Apellido        : ',data_alumno[2])
                print('Fecha nacimeieto: ',data_alumno[3])
                print('Edad            : ',data_alumno[4])
                print('Fecha ingreso   : ',data_alumno[5])
                print('Curso asiste    : ',data_alumno[6])
                print('Nota curso      : ',data_alumno[7])
                print('Estado          : ',data_alumno[-1])
            else:
                input(COLOR_ERROR+'Alumno no encontrado.')

            if input(COLOR_INPUT+('¿Desea consultar a otro alumno? (s/n): ')).lower() !='s':
                break
        except ValueError:
            input(COLOR_ERROR+'ID invalida.')

def listar_aprobaciones():
    # Muestra a los alumnos Aprobados y No Aprobados

    if existe_archivo(direc_alumnos) and len(registro_alumnos) > 0:
        while True:
            try:
                clear()
                print(COLOR_TITULO+'Aprobaciones\n')
                print('1. Litado de aprobados')
                print('2. Lisado de reprobados')
                opcion = int(input(COLOR_INPUT+'Ingrese opcion: '))
                if opcion in range(1,3):
                    break
                else:
                    input(COLOR_ERROR+'Opcion no encontrada.')
            except ValueError:
                input(COLOR_ERROR+'Opcion invalida.')

        l_registros = []

        if opcion == 1:
            titulo = COLOR_TITULO+'Aprobados\n'
            for registro in registro_alumnos: 
                registro = registro.split(',')
                if int(registro[7]) >= 5:
                    l_registros.append(registro)

        elif opcion == 2:
            titulo = COLOR_TITULO+'Reprobados\n'
            for registro in registro_alumnos: 
                registro = registro.split(',')
                if int(registro[7]) <= 4:
                    l_registros.append(registro)
        if len(l_registros) > 0:
            clear()
            print(titulo)
            encabezado = ['ID','Nombre','Apellido','Fecha nacimento','Edad','Fecha ingreso','Curso','Nota','Estado']
            print(tabulate(l_registros,headers=encabezado,tablefmt='rounded_outline',numalign='center'))
            pausa()
        else:
            input(COLOR_ERROR+'No hay alumnos en el listado.')
    else:
        input(COLOR_ERROR+'No se encontraron alumnos.')

def listar_estado():
    # Muestra que alumnos esta activos
    # y que alumnos estan dados de baja

    if existe_archivo(direc_alumnos) and len(registro_alumnos) > 0:
        while True:
            try:
                clear()
                print(COLOR_TITULO+'Listado de estado\n')
                print('1. Activos')
                print('2. De baja')
                opcion = int(input(COLOR_INPUT+'Ingrese opcion: '))
                if opcion in range(1,3):
                    break
                else:
                    input(COLOR_ERROR+'Opcion no encontrada.')
            except ValueError:
                input(COLOR_ERROR+'Opcion invalida.')

        l_registros = []

        if opcion == 1:
            titulo = COLOR_TITULO+'Activos\n'
            for registro in registro_alumnos: 
                registro = registro.split(',')
                if registro[-1].rstrip('\n') == 'A':
                    l_registros.append(registro)

        elif opcion == 2:
            titulo = COLOR_TITULO+'De baja\n'
            for registro in registro_alumnos: 
                registro = registro.split(',')
                if registro[-1].rstrip('\n') == 'B':
                    l_registros.append(registro)

        if len(l_registros) > 0:
            clear()
            print(titulo)
            encabezado = ['ID','Nombre','Apellido','Fecha nacimento','Edad','Fecha ingreso','Curso','Nota','Estado']
            print(tabulate(l_registros,headers=encabezado,tablefmt='rounded_outline',numalign='center'))
            pausa()
        else:
            input(COLOR_ERROR+'No hay alumnos en el listado.')
    else:
        input(COLOR_ERROR+'No se encontraron alumnos.')

def modificar_alumno():
    # Modifica el estado del alumno para dorlo de baja o activo
    
    if existe_archivo(direc_alumnos) and len(registro_alumnos) > 0:
        while True:
            try:
                clear()
                titulo('Modificar alumno')
                id_modificar = int(input(COLOR_INPUT+'Ingrese ID de alumno a modificar: '))
                data_alumno = data_registro(direc_alumnos,id_modificar)
                if data_alumno != None:
                    titulo('Datos del alumno')
                    print('Nombre          : ',data_alumno[1])
                    print('Apellido        : ',data_alumno[2])
                    print('Fecha nacimeieto: ',data_alumno[3])
                    print('Fecha ingreso   : ',data_alumno[5])
                    print('Curso asiste    : ',data_alumno[6])
                    print('Nota curso      : ',data_alumno[7])
                    print('Estado          : ',data_alumno[-1])
                    pausa()

                    id_alumno          = data_alumno[0]
                    nuevo_nombre       = data_alumno[1]
                    nuevo_apellido     = data_alumno[2]
                    nueva_fecha_nac    = data_alumno[3]
                    nueva_edad         = data_alumno[4]
                    nueva_fecha_ingeso = data_alumno[5]
                    nuevo_curso        = data_alumno[6]
                    nueva_nota         = data_alumno[7]
                    nuevo_estado       = data_alumno[-1]

                    while True:
                        try:
                            clear()
                            titulo('Campo a modificar')
                            print('1. Nombre')
                            print('2. Apellido')
                            print('3. Fecha nacimeieto')
                            print('4. Fecha ingreso')
                            print('5. Curso asiste')
                            print('6. Nota curso')
                            print('7. Estado')
                            print('0. Abandonar cambios\n')
                            opcion = int(input(COLOR_INPUT+'Ingrese opcion: '))
                            if opcion == 0:
                                break
                            elif opcion == 1:
                                while True:
                                    nuevo_nombre = input(COLOR_INPUT+'Ingrese nombre: ').title()
                                    if len(nuevo_nombre) > 0:
                                        break
                                    else:
                                        input(COLOR_ERROR+'Campo Obligatorio.')

                            elif opcion == 2:
                                while True:
                                    nuevo_apellido = input(COLOR_INPUT+'Ingrese apellido: ').title()
                                    if len(nuevo_apellido) > 0:
                                        break
                                    else:
                                        input(COLOR_ERROR+'Campo Obligatorio.')

                            elif opcion == 3:
                                while True:
                                    nueva_fecha_nac = input(COLOR_INPUT+'Ingrese fecha de nacimeiento (dd/mm/aaaa): ')
                                    if validar_fecha(nueva_fecha_nac):
                                        nueva_edad = calcular_edad(nueva_fecha_nac)
                                        if nueva_edad in range(1,110):
                                            break
                                        else:
                                            input(COLOR_ERROR+'Edad fuera de rango.')
                                    else:
                                        input(COLOR_ERROR+'Fecha invalida')

                            elif opcion == 4:
                                while True:
                                    nueva_fecha_ingeso = input(COLOR_INPUT+'Ingrese fecha de ingreso (dd/mm/aaaa): ')
                                    if validar_fecha(nueva_fecha_ingeso):
                                        nueva_fecha_ingeso = datetime.strptime(nueva_fecha_ingeso,FORMATO_FECHA)
                                        if nueva_fecha_ingeso <= fecha_actual:
                                            break
                                        else:
                                            input(COLOR_ERROR+'La fecha deve ser anterior a la actual')
                                    else:
                                        input(COLOR_ERROR+'Fecha invalida.')

                            elif opcion == 5:
                                while True:
                                    try:
                                        nuevo_curso = int(input(COLOR_INPUT+'Ingrese ID del curso al que asiste: '))
                                        curso = data_registro(direc_cursos,nuevo_curso)
                                        if curso != None:
                                            nombre_curso = curso[1].rstrip('\n')
                                            print('Curso al que asiste: ', nombre_curso)
                                            break
                                        else:
                                            input(COLOR_ERROR+'Curso no encotrado.')
                                    except ValueError:
                                        input(COLOR_ERROR+'Opcion numerica.')

                            elif opcion == 6:
                                while True:
                                    try:
                                        nueva_nota = int(input(COLOR_INPUT+'Ingrese nota: '))
                                        if nueva_nota in range(1,11):
                                            break
                                        else:
                                            input(COLOR_ERROR+'Las notas van del 1 al 10')
                                    except ValueError:
                                        input(COLOR_ERROR+'La nota es numerica.')

                            elif opcion == 7:
                                while True:
                                    nuevo_estado = input(COLOR_INPUT+'Ingrese estado (A/B): ').upper()
                                    if nuevo_estado == 'A' or nuevo_estado == 'B':
                                        break
                                    else:
                                        input(COLOR_ERROR+'Opcion invalida')

                            clear()
                            titulo('Alumno a ingresar')
                            print('Id              : ',id_alumno)
                            print('Nombre          : ',nuevo_nombre)
                            print('Apellido        : ',nuevo_apellido)
                            print('Fecha nacimeieto: ',nueva_fecha_nac)
                            print('Edad            : ',nueva_edad)
                            print('Fecha igreso    : ',nueva_fecha_ingeso)
                            print('Curso asiste    : ',nuevo_curso)
                            print('Nota curso      : ',nueva_nota)
                            print('Estado          : ',nuevo_estado)

                            if input(COLOR_INPUT+'¿Desea agrgar a este alumno? (s/n): ').lower() =='s':
                                borrar_registros(direc_alumnos,id_modificar)
                                archivo = open(direc_alumnos,'a',encoding='utf-8')
                                registro = f'{id_alumno},{nuevo_nombre},{nuevo_apellido},{nueva_fecha_nac},{nueva_edad},{nueva_fecha_ingeso},{nuevo_curso},{nueva_nota},{nuevo_estado}\n'
                                archivo.write(registro)
                                archivo.close()
                                input(COLOR_DESTACAR+'\nAlumno modificado existosamente\n')

                        except ValueError:
                            input(COLOR_ERROR+'Opcion invalida.')
        

                else:
                    input(COLOR_ERROR+'Alumno no encontrado.')

            except ValueError:
                input(COLOR_ERROR+'ID invalida.')

            if input(COLOR_INPUT+('¿Desea modificar a otro alumno? (s/n): ')).lower() !='s':
                break
    else:
        input(COLOR_ERROR+('No hay alumnos.'))

def menu_listados():
    while True:
        try:
            clear()
            titulo('Menu listados')
            print('1. Consultar alumno')
            print('2. Listado alumnos')
            print('3. Aprobaciones')
            print('4. Estado alumnos')
            print('0. Salir')
            opcion = int(input(COLOR_INPUT+'Ingrese opcion: '))
            if opcion in range(0,5):
                    
                if opcion   == 0: break
                elif opcion == 1: consultar_alumno()
                elif opcion == 2: listar_alumnos()
                elif opcion == 3: listar_aprobaciones()
                elif opcion == 4: listar_estado()

            else:
                input(COLOR_ERROR+'Opcion no encontrada.')
        except ValueError:
            input(COLOR_ERROR+'Opcion ivalida.')

def menu_alumnos():
    registro_cursos = registros(direc_cursos)
    if existe_archivo(direc_cursos) and  len(registro_cursos) > 0:
        while True:
            try:
                clear()
                titulo('Sistema de alumnos')
                print('1. Agregar alumno')
                print('2. Eliminar alumnos')
                print('3. Listados alumnos')
                print('4. Modificar alumno')
                print('0. Volver al menu pricipal\n')
                opcion = int(input(COLOR_INPUT+'Elija opcion: '))
                if opcion in range(0,5):

                    if opcion   == 0  : break
                    elif opcion == 1: agregar_alumno()
                    elif opcion == 2: eliminar_alumno()
                    elif opcion == 3: menu_listados()
                    elif opcion == 4: modificar_alumno()

                else:
                    input(COLOR_ERROR+'Opcion no encontrada.')             
            except ValueError:
                input(COLOR_ERROR+'Opcion invalida...')
    else:
        input(COLOR_ERROR+'Por favor agregue un curso antes de continuar.')

                