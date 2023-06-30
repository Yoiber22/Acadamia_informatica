import os
import sys
from tabulate import tabulate
from colorama import Fore, init
from datetime import datetime

# Direccion archivos
direc_cursos      = 'data/cursos.txt'
direc_alumnos     = 'data/alumnos.txt'

# Formato fecha y hora
FORMATO_FECHA   = '%d/%m/%Y'
FORMATO_HORA    = '&H:%M'
FORMATO_HORA_12 = '%I:%M %p'    
FORMATO_BD      = '%Y-%m-%d'

# Fecha actual
fecha_actual = datetime.now()

# Colores
COLOR_TITULO   = Fore.LIGHTGREEN_EX
COLOR_INPUT    = Fore.LIGHTBLUE_EX
COLOR_ERROR    = Fore.LIGHTRED_EX
COLOR_DESTACAR = Fore.LIGHTCYAN_EX
