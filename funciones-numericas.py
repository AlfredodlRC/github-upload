#print(type('7'))
#print(type(7))
#print(type(7.1))

#print(isinstance('7', str))
#print(isinstance(7, int))
#print(isinstance(7.1, float))

#print(isinstance(7, str))
#print(isinstance('7', int))
#print(isinstance('7.1', float))



#numeric_value = '7'
#print(numeric_value.isnumeric())

#string_value = 'Bob'
#print(string_value.isnumeric())

#numero=input('Introduce un numero:')

#if numero.isnumeric()==False:
#    print("No has introducido un numero")
#    exit()

#if numero.isdecimal()==True:
#    print("has introducido un numero entero")

numero=input('Introduce temperatura en faradais:')

if numero.isnumeric()==False:
    print("No has introducido un numero")
    exit()

resultado=((int(numero)-32)*5)/9
print("en celsius", resultado)



