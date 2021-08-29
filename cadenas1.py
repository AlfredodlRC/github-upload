#primera_cadena="Hola mundo"
#segunda_cadena='Hola Mundo'
#print(primera_cadena == segunda_cadena)
#tercera_cadena="una cadena con 'comillas simples'"
#cuarta_cadena='una cadena con "comillas dobles"'
#print(tercera_cadena)
#print(cuarta_cadena)
#quinta_cadena='una cadena con una \' comilla simple escapada'
#sexta_cadena="una cadena con una \" comilla doble escapada"
#septima_cadena="una linea con un \n salto de linea escapada"
#octava_cadena="una lina con una \t tabulación escapada"
#print(quinta_cadena)
#print(sexta_cadena)
#print(septima_cadena)
#print(octava_cadena)
#novena_cadena=r"unacadena con un \n salto de linea escapado en crudo"
#print(novena_cadena)
#decima_cadena="""esta es una
#cadena textural
#que contiene varias lineas entre doble comillas"""
#undecima_cadena='''esta es una
#cadena textural
#que contiene varias lineas entre comillas simples'''
#print(decima_cadena)
#print(undecima_cadena)
#uno="05"
#dos="08"
#tres="2021"
#print(uno)
#print(uno,dos)
#print(uno,dos,tres)
#print(uno,dos,tres,sep="-")
#print(uno,dos,tres,sep="/")
#print(uno,dos,tres,sep="-",end=".")
#print("\n")
#mensaje=str.capitalize(tercera_cadena)
#print(mensaje)
#mensaje="otro mensaje trasformado".capitalize()
#print(mensaje)
#print(tercera_cadena.capitalize())

#print(primera_cadena)
#print(primera_cadena.lower())
#print(primera_cadena.upper())
#print(primera_cadena.title())
#print(primera_cadena.swapcase())
#print(primera_cadena.count("o"))
#print(len(primera_cadena))
#print(primera_cadena.startswith("la"))
#print(primera_cadena.startswith("h"))
#print(primera_cadena.startswith("Ho"))
#print(primera_cadena.endswith("ho"))
#print(primera_cadena.endswith("do"))
#print(primera_cadena.endswith("o"))

#print(primera_cadena.find("o"))
#print(primera_cadena.find("d"))
#print(primera_cadena.find("i"))
#mensaje="     medio     "
#print("."+mensaje+".")
#print("."+mensaje.lstrip()+".")
#print("."+mensaje.rstrip()+".")
#print("."+mensaje.strip()+".")
#print("."+mensaje.replace("medio","cambiado")+".")
#print(mensaje.rjust(30))
#print(mensaje.rjust(30, '-'))
#print(mensaje.ljust(30))
#print(mensaje.ljust(30, '-'))

#medicine = 'Coughussin'
#dosage = 5
#duration = 4.5
#instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
#print(instructions)
#instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
#print(instructions)
#instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)
#print(instructions)

#nombre="Juan"
#mensaje =f"hola, {nombre}"
#print(mensaje)
#total=5
#valor=20.5
#mensaje=f"total:{total}, multiplicado por {valor}"
#print(mensaje)

#value = 'hola'

#print(f'.{value:<25}.')
#print(f'.{value:>25}.')
#print(f'.{value:^25}.')
#print(f'.{value:-^25}.')




first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = first_value.strip()
first_value = first_value.lower()
first_value = first_value.title()
first_value = f'{first_value:^30}'

# Second challenge
second_value = second_value.replace('-', '')
second_value = second_value.strip()
second_value = second_value.capitalize()

# Third challenge
third_value = third_value.replace(' ', '')
third_value = third_value.replace('-', ' ')
third_value = third_value.swapcase()
third_value = f'{third_value:>30}'

print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fifth challenge - use only a single print() function. Create tabs and new lines using f-strings.
print(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')











