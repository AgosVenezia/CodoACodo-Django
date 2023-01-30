primer_numero = 23
segundo_numero = 34

print(f'La suma es {primer_numero+segundo_numero}')

def suma_operacion(a,b):
    resultado = a+b
    return resultado

print(f"La suma con una funcion es {suma_operacion(primer_numero,segundo_numero)}")

#scope global
x=0

def funcion():
    #scope enclosed
    x = 1

    def funcion_interna(): #declaracion de la funcion
        #scope local
        #global x
        x = 2
        print(f"El scope local de x={x}")

    funcion_interna() # llamada a la funcion
    print(f"Enclosed de x={x}")

funcion()
print(f"Scope global x={x}")

    