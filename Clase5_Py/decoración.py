#El decorador es una función que añade una funcionalidad extra a otras

#La función decoradora está formada por tres funciones
def funcion_decoradora(funcion_parametro):

    def funcion_interior():

        #acciones adicionales que decoran
        print("Se inicia el cálculo")
        funcion_parametro()
        print("Se ha terminado el cálculo")

    return funcion_interior

@funcion_decoradora
def suma():
    #print(a+b)
    print(10+2)

@funcion_decoradora
def resta():
    #print(a-b)
    print(23-4)

suma()
resta()