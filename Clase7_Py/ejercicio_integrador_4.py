"""4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia."""

def contar_palabras(texto):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - texto: Es una cadena de caracteres.
    Devuelve: 
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    texto = texto.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def mas_repetida(palabras_dict):
    max_palabra = ''
    max_freq = 0
    for palabra, freq in palabras_dict.items():
        if freq > max_freq:
            max_palabra = palabra
            max_freq = freq
    return max_palabra, max_freq

texto = 'Como quieres que te quiera si el que quiero que me quiera no me quiere \
    como quiero que me quiera'
print(f"Cantidad de palabras: {contar_palabras(texto)}")
print(
    f"(Palabra más repetida, frecuencia) -> {mas_repetida(contar_palabras(texto))}")