"""5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva."""

def get_int():
    ingreso_correcto = False
    while not ingreso_correcto:
        user_input = input('Ingrese un número entero: ')
        try:
            valor = int(user_input)
        except ValueError:
            print('No es un entero válido. Intente nuevamente!')
        else:
            ingreso_correcto = True

    return valor


print(f"Número ingresado: {get_int()}")




