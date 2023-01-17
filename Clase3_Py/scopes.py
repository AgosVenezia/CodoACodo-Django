primer_numero = 23
segundo_numero = 34

primerNumero = 55

print(f"La suma es {primerNumero+segundo_numero}")

def suma(a,b):
    return a+b

print(f"La suma es {suma(primer_numero,segundo_numero)}")

def suma_operacion(a,b):
    resultado = a+b
    return resultado

print(f"La suma es {suma_operacion(primer_numero,segundo_numero)}")


#Global Scope
x = 0
def funcion():
    #Enclosed Scope
    x = 1
    def funcion_interna():             #declaración de la función
        #Local Scope
        x = 2
        print(f"Local Scope x={x}")

    funcion_interna()                  #llamada a la función
    print(f"Enclosed Scope x={x}")

funcion()
print(f"Global Scope x={x}")
        