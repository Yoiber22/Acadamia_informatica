from config import *


clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
pausa = lambda: input(COLOR_DESTACAR+'\nPulse enter para continuar')

def titulo(string):
    largo = len(string)
    print(COLOR_TITULO+'-' * largo)
    print(COLOR_TITULO+string)
    print(COLOR_TITULO+'-' * largo)
    print()

def existe_archivo(nom_archivo):
    try:
        archivo = open(nom_archivo, 'r')
        archivo.close()
        return True
    except FileNotFoundError:
        return False
    
def ultima_clave(nom_archivo):
    archivo = open(nom_archivo,'r')
    registros = archivo.readlines()
    archivo.close()
    ultima_clave = len(registros)
    return ultima_clave

def data_registro(nombre_archivo, clave): # Recisbe un string y un int
    archivo = open(nombre_archivo,'r')
    registros = archivo.readlines()
    archivo.close()

    for registro in registros:
        registro = registro.split(',')
        if int(registro[0]) == clave:
            return registro
        
    return None

def registros(nombre_archivo):
    archivo = open(nombre_archivo,'r')
    registros = archivo.readlines()
    archivo.close()
    return registros
        
def data_registro_nombre(nombre_archivo, nombre):
    archivo = archivo.open(nombre_archivo,'r',encoding='utf-8')
    registros = archivo.readlines()
    archivo.close()

    for registro in registros:
        registro = registro.split(',')
        if registro[1].lower().strip('\n') == nombre.lower():
            return registro
        
    return None

def borrar_registros(nombre_archivo, codigo_borrar):
    archivo = open(nombre_archivo,'r',encoding='utf-8')
    registros = archivo.readlines()
    archivo.close()
    archivo = open(nombre_archivo,'w',encoding='utf-8')
    for registro in registros:
        registro = registro.split(',')
        if int(registro[0]) != codigo_borrar:
            registro = ','.join(registro)
            archivo.write(registro)
    archivo.close()

def validar_fecha(fecha):
    try:
        objeto_fecha = datetime.strptime(fecha, FORMATO_FECHA)    
        return True
    except ValueError:
        return False
    
def validar_hora(hora):
    try:
        datetime.strptime(hora, FORMATO_HORA)
        return True
    except ValueError:
        return False

def calcular_edad(fecha):
    fecha_actual = datetime.now()
    fecha_nacimiento = datetime.strptime(fecha, FORMATO_FECHA)
    edad = fecha_actual.year - fecha_nacimiento.year
    if fecha_actual.month < fecha_nacimiento.month or (fecha_actual.month == fecha_nacimiento.month and fecha_actual.day < fecha_nacimiento.day):  
        edad -= 1 
   
    return edad