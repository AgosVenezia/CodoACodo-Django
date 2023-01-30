"""5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva."""

from re import A


def get_int():
    user_input = input('Por favor ingrese un número: ')
    try:
        value = int(user_input)
    except ValueError:
        print('No es un entero válido. Intente nuevamente!')
        return get_int()
    else:
        return value


print(f"Número ingresado: {get_int()}")
