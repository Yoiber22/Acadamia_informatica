import os
from tabulate import tabulate
from datetime import datetime


nom_cursos      = 'data/cursos.txt'
nom_alumnos     = 'data/alumnos.txt'


FORMATO_FECHA   = '%d/%m/%Y'
FORMATO_HORA    = '&H:%M'
FORMATO_HORA_12 = '%I:%M %p'    
FORMATO_BD      = '%Y-%m-%d'

fecha_actual = datetime.now()
