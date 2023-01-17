import sys

#Llamar excepciones RAISE
class DivisorNegativoError(Exception):
    #Excepción lanzada si se divide por un número negativo
    #Como no reconoce el nombre, lo manda a ex
    pass

def mostrar_division_entera(dividendo,divisor):
    try:
        #Palabra reservada que valida si pasa algo
        assert divisor >= 0, "Mandaron un número negativo"
        if divisor < 0:
            raise DivisorNegativoError("Mandaron un número negativo en el divisor")
        print("Intentando resolver la division")
        resultado = dividendo / divisor
        print(f"El resultado de la división es: {resultado}")
    except AssertionError as assert_error:
        print(assert_error)
        print("Le erraste a un dato...")
    except TypeError:
        #logica de capturar error
        print("Error, divisor o dividendo no son numéricos")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(exc_type)
        print(exc_value)
        print(exc_traceback)
    except ZeroDivisionError as DZeroException:
        print(f"Error {DZeroException}")
    except DivisorNegativoError:
        print("Error, pasó algo con el divisor que es negativo")
    except Exception as ex:
        print(f"Algo anda mal: {ex}")
    else:
        print("Este programa nunca falla...")
    finally:
        print("El cálculo se realizó correctamente")

mostrar_division_entera(2,-1)
mostrar_division_entera(4,0)     #ZeroDivisionError: division by zero
mostrar_division_entera(8,"4")    #TypeError: unsupported operand type(s) for /: 'int' and 'str'
print("Finalización del programa")