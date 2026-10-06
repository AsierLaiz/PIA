def contar_vocales(frase):
    return len([c for c in frase.lower() if c in "aeiou"])

def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]
def invertir(frase):
    return frase[::-1]